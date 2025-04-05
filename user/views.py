from django.http import JsonResponse
from django.views import View

from user.models import User


class TestView(View):
    @staticmethod
    def get(request):
        user_list_obj = User.objects.all()  # 获取对象
        user_list_dict = user_list_obj.values()  # 转存字典
        user_list = list(user_list_dict)  # 将外层容器转存List

        return JsonResponse({'code': 200, 'info': '测试', 'data': user_list})
