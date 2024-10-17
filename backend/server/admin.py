from django.contrib import admin
from . models import Courses, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'is_staff', 'is_superuser','is_proffesor')
    search_fields = ('email', 'name')
    ordering = ('email',)
    fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Personal info', {'fields': ('name',)}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser','is_proffesor', 'groups', 'user_permissions')}),
    ('Important dates', {'fields': ('last_login',)}),  # Removed 'date_joined'
)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )





admin.site.register(Courses)