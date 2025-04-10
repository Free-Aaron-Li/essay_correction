#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
import json
from datetime import datetime

from django.http import JsonResponse
from django.views import View

from menu.models import Menu, MenuSerializer, RoleMenu


class TreeListView(View):
    # 构造菜单树
    @staticmethod
    def build_tree_menu(menu_list):
        result_menu_list: list[Menu] = list()
        for menu in menu_list:
            # 寻找子节点
            for e in menu_list:
                if e.parent_id == menu.id:
                    if not hasattr(menu, "children"):
                        menu.children = list()
                    menu.children.append(e)
            # 判断父节点，添加到集合
            if menu.parent_id == 0:
                result_menu_list.append(menu)
        return result_menu_list

    def get(self, request):
        menu_query_set = Menu.objects.order_by("order_num")
        # 构造菜单树
        menu_list: list[Menu] = self.build_tree_menu(menu_query_set)
        serializer_menu_list: list[MenuSerializer] = list()
        for menu in menu_list:
            serializer_menu_list.append(MenuSerializer(menu).data)
        return JsonResponse({'code': 200, 'tree_list': serializer_menu_list})


class SaveView(View):

    @staticmethod
    def post(request):
        data = json.loads(request.body.decode("utf-8"))
        # 添加
        if data['id'] == -1:
            menu = Menu(name=data['name'], icon=data['icon'],
                        parent_id=data['parent_id'], order_num=data['order_num'], path=data['path'],
                        component=data['component'], menu_type=data['menu_type'], perms=data['perms'],
                        remark=data['remark'])
            menu.create_time = datetime.now().date()
            menu.save()
        # 修改
        else:
            menu = Menu(id=data['id'], name=data['name'], icon=data['icon'],
                        parent_id=data['parent_id'], order_num=data['order_num'], path=data['path'],
                        component=data['component'], menu_type=data['menu_type'], perms=data['perms'],
                        remark=data['remark'], create_time=data['create_time'],
                        update_time=data['update_time'])
            menu.update_time = datetime.now().date()
            menu.save()
        return JsonResponse({'code': 200})


class ActionView(View):

    @staticmethod
    def get(request):
        """
        根据id获取权限信息
        """
        id = request.GET.get("id")
        menu_object = Menu.objects.get(id=id)
        return JsonResponse({'code': 200, 'menu': MenuSerializer(menu_object).data})

    @staticmethod
    def delete(request):
        """
        删除操作
        """
        id = json.loads(request.body.decode("utf-8"))
        if Menu.objects.filter(parent_id=id).count() > 0:
            return JsonResponse({'code': 500, 'msg': '请先删除子菜单！'})
        else:
            RoleMenu.objects.filter(menu_id=id).delete()
            Menu.objects.get(id=id).delete()
            return JsonResponse({'code': 200})
