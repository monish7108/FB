from django.contrib import admin
from .models import *

admin.site.register(UserInfo)
admin.site.register(PostsByUser)
admin.site.register(FriendList)