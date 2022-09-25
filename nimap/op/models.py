from django.db import models

# Create your models here.
class User2(models.Model):
    name = models.CharField(max_length = 100)
    createdby = models.CharField(max_length = 100)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class User(models.Model):
    user_name = models.CharField(max_length = 100)
    def __str__(self):
        return self.user_name
class project(models.Model):
    project_name = models.CharField(max_length = 100)
    client_id = models.IntegerField()
    user_id = models.IntegerField()
    project_createdby = models.CharField(max_length = 100)
    project_createdat = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.project_name
    
    