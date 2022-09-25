from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import User2,User,project
from .serializers import User2Serializer,projectSerializer,userSerializer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Client_list(request):
    if request.method == 'GET':
        user2 = User2.objects.all()
        serializer = User2Serializer(user2, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = User2Serializer(data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id=data.get('id')
        user=User2.objects.get(id=id)
        serializer = User2Serializer(user,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id=data.get('id')
        record_for_delete=User2.objects.get(id=id)
        record_for_delete.delete()
        res={'msg':'data deleted!!'}
        return JsonResponse(res, status=201)


@csrf_exempt
def log_user_list(request):   
    if request.method == 'GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id=data.get('id')
        all_project_of_log_user= project.objects.filter(user_id=id)
        serializer_project_of_log_user = projectSerializer(all_project_of_log_user,many=True)
        return JsonResponse(serializer_project_of_log_user.data, safe=False) 
        

@csrf_exempt
def project_list(request):   
    if request.method == 'GET':
        final={}
        json_data=request.body
        stream=io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id=data.get('id')
        user2 = User2.objects.get(id=id)
        serializer_client = User2Serializer(user2)
        projects= project.objects.filter(client_id=id)
        serializer_project = projectSerializer(projects,many=True)
        final=serializer_client.data
        final['projects']=serializer_project.data
        return JsonResponse(final, safe=False)     
    
    elif request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = projectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
   
