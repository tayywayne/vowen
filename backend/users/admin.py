from django.contrib import admin
from .models import UserProfile
from .models import FriendshipPair

admin.site.register(UserProfile)
admin.site.register(FriendshipPair)