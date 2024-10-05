from django.contrib import admin

from src.users.models.users import UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'created_at', 'updated_at')
