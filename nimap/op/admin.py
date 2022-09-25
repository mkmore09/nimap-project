from django.contrib import admin
from .models import User2,User,project

   
admin.site.register(User2)
class ClientAdmin(admin.ModelAdmin):
    list_display= [
        'name',
        'createdby',
        'createdat',
        'updatedat',
        
        ]
admin.site.register(User)
class ClientAdmin(admin.ModelAdmin):
    list_display= [
        'name',
        ]
admin.site.register(project)
class ClientAdmin(admin.ModelAdmin):
    list_display= [
        'name',
        'client_id',
        'user_id',
        'createdby',
        'createdat',
        'updatedat',
        
        ]
    
    