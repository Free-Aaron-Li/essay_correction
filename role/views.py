#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
from django.http import JsonResponse
from django.views import View

from role.models import Role


class ListAllView(View):
    """
    查询所有角色信息
    """

    @staticmethod
    def get(request):
        role_list = Role.objects.all().values()
        role_list = list(role_list)
        return JsonResponse({'code': 200, 'role_list': role_list})
