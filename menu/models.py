#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
from django.db import models
from rest_framework import serializers

from role.models import Role


# Create your models here.

# 菜单类
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, verbose_name="菜单名称")
    icon = models.CharField(max_length=100, null=True, verbose_name="菜单图标")
    parent_id = models.IntegerField(null=True, verbose_name="父菜单ID")
    order_num = models.IntegerField(null=True, verbose_name="显示顺序")
    path = models.CharField(max_length=200, null=True, verbose_name="路由地址")
    component = models.CharField(max_length=255, null=True, verbose_name="组件路径")
    menu_type = models.CharField(max_length=1, null=True, verbose_name="菜单类型（M目录 C菜单 F按钮）")
    perms = models.CharField(max_length=100, null=True, verbose_name="权限标识")
    create_time = models.DateField(null=True, verbose_name="创建时间", )
    update_time = models.DateField(null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=500, null=True, verbose_name="备注")

    def __lt__(self, other):
        return self.order_num < other.order_num

    class Meta:
        db_table = "menus"


class MenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        print("111")
        if hasattr(obj, "children"):
            serializerMenuList: list[MenuSerializer2] = list()
            for menu in obj.children:
                serializerMenuList.append(MenuSerializer2(menu).data)
            return serializerMenuList

    class Meta:
        model = Menu
        fields = '__all__'


class MenuSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


# 系统角色菜单关联类
class RoleMenu(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)

    class Meta:
        db_table = "role_menu"


class RoleMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleMenu
        fields = '__all__'
