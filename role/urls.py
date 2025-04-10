#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
from django.urls import path

from role.views import ListAllView

urlpatterns = [
    path('list_all', ListAllView.as_view(), name='list_all'),
]
