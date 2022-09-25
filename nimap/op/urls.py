from django.urls import path
#now import the views.py file into this code
from op import views
urlpatterns=[
  path('client/',views.Client_list),
  
  path('user/',views.log_user_list),
  
  path('project/',views.project_list)
  
  
]