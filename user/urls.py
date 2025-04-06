#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
from django.urls import path

from user.views import TestView, JwtTestView

urlpatterns = [
    path('test', TestView.as_view(), name='test'),
    path('jwt_test', JwtTestView.as_view(), name='jwt_test')
]
