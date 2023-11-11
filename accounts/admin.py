from django.contrib import admin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'is_active', 'is_admin', 'jtime', 'jlast_login')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('is_active', 'is_admin')

    fieldsets = (
        ('Authentication', {'fields': ('name', 'password')}),
        ('Personal Info', {'fields': ('phone', 'email', 'profile_img')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_student')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'phone', 'email', 'password1', 'password2'),
        }),
    )
    
    ordering = ('name',)

    readonly_fields = ('date_created', 'jtime', 'jlast_login')

admin.site.register(User, CustomUserAdmin)
