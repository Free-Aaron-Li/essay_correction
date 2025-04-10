#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
import json
from datetime import datetime

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View

from menu.models import RoleMenu
from role.models import Role, RoleSerializer, UserRole


class ListAllView(View):
    """
    查询所有角色信息
    """

    @staticmethod
    def get(request):
        role_list = Role.objects.all().values()
        role_list = list(role_list)
        return JsonResponse({'code': 200, 'role_list': role_list})


class SearchView(View):
    """
    角色信息查询
    """

    @staticmethod
    def post(request):
        data = json.loads(request.body.decode('utf-8'))
        page_num = data['page_num']
        page_size = data['page_size']
        query = data['query']
        role_list_page = Paginator(Role.objects.filter(name__contains=query), page_size).page(page_num)
        roles = role_list_page.object_list.values()  # 转换为字典
        roles = list(roles)
        total = Role.objects.filter(name__contains=query).count()
        return JsonResponse({'code': 200, 'role_list': roles, 'total': total})


class SaveView(View):
    @staticmethod
    def post(request):
        data = json.loads(request.body.decode('utf-8'))
        # 添加
        if data['id'] == -1:
            role = Role(name=data['name'], code=data['code'], remark=data['remark'])
            role.create_time = datetime.now().date()
            role.save()
        # 修改
        else:
            role = Role(id=data['id'], name=data['name'], code=data['code'], remark=data['remark'],
                        create_time=data['create_time'], update_time=data['update_time'])
            role.save()
        return JsonResponse({'code': 200})


class ActionView(View):
    """
    角色基本操作
    """

    @staticmethod
    def get(request):
        id = request.GET.get('id')
        role = Role.objects.get(id=id)
        return JsonResponse({'code': 200, 'role': RoleSerializer(role).data})

    @staticmethod
    def delete(request):
        id_list = json.loads(request.body.decode("utf-8"))
        UserRole.objects.filter(role_id__in=id_list).delete()
        RoleMenu.objects.filter(role_id__in=id_list).delete()
        Role.objects.filter(id__in=id_list).delete()
        return JsonResponse({'code': 200})


class MenusView(View):
    """
    根据角色查询菜单权限
    """

    @staticmethod
    def get(request):
        id = request.GET.get('id')
        menu_list = RoleMenu.objects.filter(role_id=id).values('menu_id')
        menu_id_list = [m['menu_id'] for m in menu_list]
        print(menu_id_list)
        return JsonResponse({'code': 200, 'menu_id_list': menu_id_list})


class GrantMenu(View):
    @staticmethod
    def post(request):
        data = json.loads(request.body.decode("utf-8"))
        id = data['id']
        menu_id_list = data['menu_ids']
        RoleMenu.objects.filter(role_id=id).delete()
        for menu_id in menu_id_list:
            role_menu = RoleMenu(role_id=id, menu_id=menu_id)
            role_menu.save()
        return JsonResponse({'code': 200})
