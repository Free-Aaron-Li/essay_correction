#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
from django.http import JsonResponse
from django.views import View

from menu.models import Menu, MenuSerializer


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
