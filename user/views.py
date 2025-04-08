#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
from typing import List

from django.http import JsonResponse
from django.views import View
from rest_framework_jwt.settings import api_settings

from menu.models import Menu, MenuSerializer
from role.models import Role
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
    def get(self, request):
        user = User.objects.get(username='admin', password='123456')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # 将用户对象传递，获取到该对象的属性值
        payload = jwt_payload_handler(user)
        # 将属性值编码成jwt格式的字符串
        token = jwt_encode_handler(payload)
        return JsonResponse({'code': 200, 'token': token})
