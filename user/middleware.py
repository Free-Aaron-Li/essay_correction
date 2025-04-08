#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from jwt import ExpiredSignatureError, InvalidTokenError, PyJWTError
from rest_framework_jwt.settings import api_settings


class JwtAuthenticationMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        """
        中间件：JWT身份验证逻辑
        """
        # 请求白名单（即无需Token验证的路径列表）
        white_list = ['/user/login']  # 可扩展，添加更多路径
        path = request.path

        # 白名单路径和 /media 目录下的内容无需验证
        if path in white_list or path.startswith('/media'):
            return None

        # 以下路径需要验证
        token = request.META.get('HTTP_AUTHORIZATION')  # 从请求头获取Token
        try:
            jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
            jwt_decode_handler(token)  # 验证Token
        except ExpiredSignatureError:
            return HttpResponse('Token过期，请重新登陆！')
        except InvalidTokenError:
            return HttpResponse('Token验证失败！')
        except PyJWTError:
            return HttpResponse('Token验证异常！')
        except Exception as e:
            print(e)
            # 返回一个通用错误信息
            return HttpResponse('验证过程中发生错误！')

        return None
