#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
from django.urls import path

from user.views import TestView, JwtTestView, LoginView, SaveView, PwdView, ImageView, AvatarView, SearchView, \
    ActionView, CheckView, StatusView, ResetPasswordDefault, GrantRole

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('save', SaveView.as_view(), name='save'),
    path('update_user_pwd', PwdView.as_view(), name='update_user_pwd'),
    path('upload_image', ImageView.as_view(), name='upload_image'),
    path('update_avatar', AvatarView.as_view(), name='update_avatar'),
    path('search', SearchView.as_view(), name='search'),
    path('action', ActionView.as_view(), name='action'),
    path('check', CheckView.as_view(), name='check'),
    path('reset_pwd_default', ResetPasswordDefault.as_view(), name='resetPassword'),
    path('grant_role', GrantRole.as_view(), name='grant_role'),
    path('status', StatusView.as_view(), name='status'),
    path('test', TestView.as_view(), name='test'),
    path('jwt_test', JwtTestView.as_view(), name='jwt_test')
]
