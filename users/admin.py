from django.contrib import admin
from .models import User,Following
# Register your models here.

admin.site.register(Following)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username','first_name','last_name','verified','email']
    search_fields = ['username', 'first_name','last_name']
