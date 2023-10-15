from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly

@api_view(['GET'])
@permission_classes([])
def api(request):
    try:
        student_obj=Student.objects.all()
        # import ipdb;ipdb.set_trace()
        serializer=StudentSerializer(student_obj,many=True)
        print(serializer)
        return Response({'status':200,  'payload': serializer.data})
    except:
        return Response({"error": "Something went wrong"})

@api_view(['POST'])
def post_student(request):
    data=request.data
    # print(data)
    serializer=StudentSerializer(data=request.data)
    # print(serializer)
    if request.data['roll']<18:
        return Response({'status':403,'message':'age must be 18'})
    if serializer.is_valid():
        serializer.save()
        return Response({'status':200,'payload':data,'message':'you sent'})

@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj=Student.objects.get(id = id)
        print(student_obj)
        data=request.data
        serializer=StudentSerializer(student_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200,'payload':data,'message':'you sent'})
        else:
            return Response({'status':403,'message':'invalid try'})
    except Exception as e:
        print(e)
        return Response({'status':403,'message':'invalid id'})

@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student_obj=Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status':200,'message':'deleted success'})
    except Exception as e:
        print(e)
        return Response({'status':200,'message':'invalid id'})
    