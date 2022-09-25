import requests

params = {'name': 'mkmore',
'createdby':'more'}
response = requests.get('http://127.0.0.1:8000/',
            params=params)
print(response.url)
user2 = User2.objects.get(id=pk)
        serializer = User2Serializer(user2, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)