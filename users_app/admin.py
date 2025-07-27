from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ToDoUser
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

@admin.register(ToDoUser)
class ToDoUserAdmin(UserAdmin):
    model = ToDoUser

    def colored_is_active(self, obj):
        color = 'green' if obj.is_active else 'red'
        text = 'Active' if obj.is_active else 'Inactive'
        return format_html('<span style="color: {}; font-weight: bold;">{}</span>', color, text)
    colored_is_active.short_description = 'Активний'
    colored_is_active.admin_order_field = 'is_active'

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'colored_is_active', 'date_joined')

    list_editable = ('is_active', 'is_staff')
    
    list_filter = ('is_active', 'is_staff')

    search_fields = ('email', 'first_name', 'last_name')

    ordering = ('last_name', 'first_name', 'date_joined')

    list_per_page = 10

    fieldsets = (
        (_('Основна інформація'), {'fields': ('email', 'password')}),
        (_('Персональні дані'), {'fields': ('first_name', 'last_name', 'phone_number', 'date_of_birth')}),
        (_('Права доступу'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Додатково'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

admin.site.site_header = "ToDo Control Center 💼"
admin.site.site_title = "ToDo Admin"
admin.site.index_title = "Панель керування завданнями"
