from rest_framework import serializers
from .models import User2,User,project

class User2Serializer(serializers.ModelSerializer):
    class Meta:
        model = User2
        fields='__all__'
    def create(self,validate_data):
        return User2.objects.create(**validate_data)
    def update(self,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.createdby=validate_data.get('createdby',instance.createdby)
        instance.createdat=validate_data.get('createdat',instance.createdat)
        instance.updatedat=validate_data.get('updatedat',instance.updatedat)
        instance.save()
        return instance
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
    def create(self,validate_data):
        return User.objects.create(**validate_data)
    def update(self,instance,validate_data):
        instance.user_name=validate_data.get('user_name ',instance.user_name )
        return instance


class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields='__all__'
    def update(self,instance,validate_data):
        instance.project_name=validate_data.get('project_name',instance.project_name)
        instance.client_id=validate_data.get('client_id',instance.client_id)
        instance.user_id=validate_data.get('user_id',instance.user_id)
        instance.project_createdby=validate_data.get('project_createdby',instance.project_createdby)
        instance.project_createdat=validate_data.get('project_createdat',instance.project_createdat)
        instance.save()
        return instance