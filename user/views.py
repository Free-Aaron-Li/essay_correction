#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
import json
from datetime import datetime
from typing import List

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View
from rest_framework_jwt.settings import api_settings

from essay_correction import settings
from menu.models import Menu, MenuSerializer
from role.models import Role, UserRole
from user.models import User, UserSerializer


class LoginView(View):
    @staticmethod
    def get_user_roles(user: User) -> List[Role]:
        """
        根据用户对象，获取并返回角色列表。

        :param user: 当前用户对象
        :return: 角色对象列表
        """
        # 查询用户的角色列表
        role_list = Role.objects.raw(
            "select id, name from roles where id in (select role_id from user_role where user_id=%s);", [user.id]
        )
        return list(role_list)

    @staticmethod
    def get_sorted_menu_list(user: User) -> List[Menu]:
        """
        根据用户对象，获取并返回排序后的菜单列表。

        :param user: 当前用户对象
        :return: 排序后的菜单列表
        """
        # 获取用户的角色列表
        role_list = LoginView.get_user_roles(user)

        # 初始化存储菜单列表
        merged_menu_list: list[Menu] = []
        for role in role_list:
            # 针对每个角色查询对应菜单
            menu_list_raw = Menu.objects.raw(
                "select id, name, icon, parent_id, order_num, perms, create_time, update_time, remark "
                "from menus where id in (select menu_id from role_menu where role_id=%s);", [role.id]
            )
            # 转换 RawQuerySet 为 list 并进行合并
            menu_list = list(menu_list_raw)
            merged_menu_list.extend(menu_list)

        # 根据 order_num 进行排序
        sorted_menu_list = sorted(merged_menu_list, key=lambda menu: menu.order_num)

        return sorted_menu_list

    @staticmethod
    def build_tree_menu(sorted_menu_list):
        result_menu_list: list[Menu] = list()
        for menu in sorted_menu_list:
            # 寻找子节点
            for child in sorted_menu_list:
                if child.parent_id == menu.id:
                    if not hasattr(menu, 'children'):
                        menu.children = list()
                    menu.children.append(child)

            # 判断父节点，添加到集合
            if menu.parent_id == 0:
                result_menu_list.append(menu)
        return result_menu_list

    def post(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            # 获取token
            token = jwt_encode_handler(payload)
            # 获取菜单
            sorted_menu_list = self.get_sorted_menu_list(user)
            # 构造菜单树
            menu_list = self.build_tree_menu(sorted_menu_list)
            # 序列化操作
            serializer_menu_list = list()
            for menu in menu_list:
                serializer_menu_list.append(MenuSerializer(menu).data)

        except Exception as e:
            print(e)
            return JsonResponse({'code': 500, 'info': '用户名或密码错误！'})

        # 获取当前用户所有角色，逗号隔开
        roles = "，".join([role.name for role in self.get_user_roles(user)])
        return JsonResponse({'code': 200, 'user': UserSerializer(user).data, 'token': token, 'info': '登陆成功！',
                             'menu_list': serializer_menu_list, 'roles': roles})


class SaveView(View):
    @staticmethod
    def post(request):
        data = json.loads(request.body.decode('utf-8'))
        # 添加
        if data['id'] == -1:
            user = User(username=data['username'], password=data['password'], email=data['email'], phone=data['phone'],
                        status=data['status'], remark=data['remark'], user_type=data['user_type'])
            user.created_at = datetime.now().date()
            user.avatar = 'default.jpg'
            user.password = '123456'
            user.save()
        # 修改
        else:
            user = User(id=data['id'], username=data['username'], password=data['password'],
                        avatar=data['avatar'], email=data['email'], phone=data['phone'],
                        last_login_time=data['last_login_time'], status=data['status'], created_at=data['created_at'],
                        updated_at=data['updated_at'], remark=data['remark'], user_type=data['user_type'])
            user.update_time = datetime.now().date()
            user.save()
        return JsonResponse({'code': 200})


class ActionView(View):
    @staticmethod
    def get(request):
        id = request.GET.get('id')
        user = User.objects.get(id=id)
        return JsonResponse({'code': 200, 'user': UserSerializer(user).data})

    @staticmethod
    def delete(request):
        id_list = json.loads(request.body.decode("utf-8"))
        UserRole.objects.filter(user_id__in=id_list).delete()
        User.objects.filter(id__in=id_list).delete()
        return JsonResponse({'code': 200})


class CheckView(View):
    @staticmethod
    def post(request):
        data = json.loads(request.body.decode("utf-8"))
        username = data['username']
        if User.objects.filter(username=username).exists():
            return JsonResponse({'code': 500})
        else:
            return JsonResponse({'code': 200})


class PwdView(View):
    @staticmethod
    def post(request):
        data = json.loads(request.body.decode("utf-8"))
        id = data['id']
        old_password = data['oldPassword']
        new_password = data['newPassword']
        obj_user = User.objects.get(id=id)
        if obj_user.password == old_password:
            obj_user.password = new_password
            obj_user.update_time = datetime.now().date()
            obj_user.save()
            return JsonResponse({'code': 200})
        else:
            return JsonResponse({'code': 500, 'error_info': '原密码错误！'})


class ResetPasswordDefault(View):
    @staticmethod
    def get(request):
        id = request.GET.get('id')
        user = User.objects.get(id=id)
        user.password = '123456'
        user.updated_at = datetime.now().date()
        user.save()
        return JsonResponse({'code': 200})


class StatusView(View):
    @staticmethod
    def post(request):
        data = json.loads(request.body.decode("utf-8"))
        id = data['id']
        status = data['status']
        user = User.objects.get(id=id)
        user.status = status
        user.save()
        return JsonResponse({'code': 200})


class ImageView(View):
    @staticmethod
    def post(request):
        file = request.FILES.get('avatar')
        if file:
            file_name = file.name
            suffix_name = file_name[file_name.rfind("."):]
            new_file_name = datetime.now().strftime('%Y%m%d%H%M%S') + suffix_name
            file_path = str(settings.MEDIA_ROOT) + "/user_avatar/" + new_file_name
            try:
                with open(file_path, 'wb') as f:
                    for chunk in file.chunks():
                        f.write(chunk)
                return JsonResponse({'code': 200, 'title': new_file_name})
            except Exception as e:
                print(e)
                return JsonResponse({'code': 500, 'error_info': '上传头像失败'})


class AvatarView(View):
    @staticmethod
    def post(request):
        data = json.loads(request.body.decode("utf-8"))
        id = data['id']
        avatar = data['avatar']
        obj_user = User.objects.get(id=id)
        obj_user.avatar = avatar
        obj_user.save()
        return JsonResponse({'code': 200})


class SearchView(View):
    @staticmethod
    def post(request):
        data = json.loads(request.body.decode("utf-8"))
        page_num = data['pageNum']  # 当前页
        page_size = data['pageSize']  # 每页大小
        query = data['query']  # 查询参数
        user_list_page = Paginator(User.objects.filter(username__icontains=query), page_size).page(page_num)  # 模糊查询
        # 转换为字典格式
        user_list_page = user_list_page.object_list.values()
        # 外层容器转换为 list
        user_list = list(user_list_page)

        # 获取用户对应的所有角色
        for user in user_list:
            role_list = Role.objects.raw(
                "select id, name from roles where id in (select role_id from user_role where user_id=%s);",
                str(user['id']))
            role_list_dict = []
            for role in role_list:
                role_dict = {'id': role.id, 'name': role.name}
                role_list_dict.append(role_dict)
            user['role_list'] = role_list_dict
        total = User.objects.filter(username__icontains=query).count()
        return JsonResponse({'code': 200, 'user_list': user_list, 'total': total})


class GrantRole(View):
    """
    用户角色授权
    """

    @staticmethod
    def post(request):
        data = json.loads(request.body.decode("utf-8"))
        user_id = data['id']
        role_id_list = data['role_ids']
        UserRole.objects.filter(user_id=user_id).delete()
        for role_id in role_id_list:
            user_role = UserRole(user_id=user_id, role_id=role_id)
            user_role.save()
        return JsonResponse({'code': 200})


class TestView(View):
    @staticmethod
    def get(request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token is not None and token != '':
            user_list_obj = User.objects.all()  # 获取对象
            user_list_dict = user_list_obj.values()  # 转存字典
            user_list = list(user_list_dict)  # 将外层容器转存List

            return JsonResponse({'code': 200, 'info': '测试！', 'data': user_list})
        else:
            return JsonResponse({'code': 401, 'info': '没有访问权限！'})


class JwtTestView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username='admin', password='123456')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # 将用户对象传递，获取到该对象的属性值
        payload = jwt_payload_handler(user)
        # 将属性值编码成jwt格式的字符串
        token = jwt_encode_handler(payload)
        return JsonResponse({'code': 200, 'token': token})
