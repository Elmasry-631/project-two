from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Board)
class Admin_boards(admin.ModelAdmin):
    list_display =('board_name','board_description',)
    
@admin.register(Post)
class Admin_posts(admin.ModelAdmin):
    list_display =('post_name','post_description','created_at','board','created_by')
    ordering = ('-created_at',)