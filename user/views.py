#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
from django.http import JsonResponse
from django.views import View
from rest_framework_jwt.settings import api_settings

from role.models import Role
from user.models import User, UserSerializer


class LoginView(View):
    def post(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            role_list = Role.objects.raw(
                "select id, name from roles where id in (select role_id from user_role where user_id=" + str(
                    user.user_id) + ")")
            print(role_list)
            for row in role_list:
                print(row.id, row.name)
        except Exception as e:
            print(e)
            return JsonResponse({'code': 500, 'info': '用户名或密码错误！'})
        return JsonResponse({'code': 200, 'user': UserSerializer(user).data, 'token': token, 'info': '登陆成功！'})


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
