from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Профили'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

# Перерегистрируем стандартную модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)