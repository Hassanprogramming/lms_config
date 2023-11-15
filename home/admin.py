from django.contrib import admin
from .models import AboutUs, ContactUs, Comment

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'text', 'timestamp')
    search_fields = ('user_name', 'email')

