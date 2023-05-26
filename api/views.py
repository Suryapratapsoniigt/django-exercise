from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator
from django.views import View

# Create your views here. 
# This is function view 
# @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data=request.body
#         stream = io.BytesIO(json_data)
#         pythonData = JSONParser().parse(stream)
#         id = pythonData.get('id', None)

#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='applicatio/json')
        
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='applicatio/json')
#     if request.method == 'POST':
#         stream = io.BytesIO(request.body)
#         pythonData = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythonData)

#         if serializer.is_valid():
#             data1 = serializer.save()
#             print(serializer, 'serilizer', data1)
#             res = {'msg' : 'data created', 'data': serializer.data}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data ,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data ,content_type='application/json')
    
#     if request.method == 'PUT':
#         stream = io.BytesIO(request.body)
#         pythonData = JSONParser().parse(stream)
#         id = pythonData.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=pythonData, partial=True)
#         print(serializer, 'serializer')
#         print('before save')
#         if serializer.is_valid():
#             serializer.save()   
#             res = {'msg' : 'Data updated', 'data' : serializer.data}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == "DELETE":
#         stream = io.BytesIO(request.body)
#         pythonData = JSONParser().parse(stream)
#         print(pythonData, 'pythonData')
#         id = pythonData.get('id')
#         print(id, 'id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         print(stu)
#         res = {'msg' : 'Data deleted'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')


# class based view 
@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *agrs,**kwargs):
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='applicatio/json')
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='applicatio/json')
    
    def post(self, request, *agrs,**kwargs):
        stream = io.BytesIO(request.body)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythonData)

        if serializer.is_valid():
            data1 = serializer.save()
            print(serializer, 'serilizer', data1)
            res = {'msg' : 'data created', 'data': serializer.data}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data ,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data ,content_type='application/json')
    
    def put(self, request, *agrs,**kwargs):
        stream = io.BytesIO(request.body)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythonData, partial=True)
        print(serializer, 'serializer')
        print('before save')
        if serializer.is_valid():
            serializer.save()   
            res = {'msg' : 'Data updated', 'data' : serializer.data}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
    def delete(self, request, *agrs,**kwargs):
        stream = io.BytesIO(request.body)
        pythonData = JSONParser().parse(stream)
        print(pythonData, 'pythonData')
        id = pythonData.get('id')
        print(id, 'id')
        stu = Student.objects.get(id=id)
        stu.delete()
        print(stu)
        res = {'msg' : 'Data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')