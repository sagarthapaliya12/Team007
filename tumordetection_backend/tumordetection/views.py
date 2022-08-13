from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from tumordetection.models import ImageModel

from tumordetection.serializers import ImageSerializer
# Create your views here.

class ImageView(APIView):
  def post(self,request,format=None):
    serializer = ImageSerializer(data=request.data)
    if(serializer.is_valid()):
      serializer.save()
      return Response({"msg":"Profile Data Saved Sucessfully",'status':'success','candidate':serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

  def get(self,request,format=None):
    try:
      candidate =ImageModel.objects.get()
      serializer = ImageSerializer(candidate)
      return Response({"status":"success","candidates":serializer.data},status=status.HTTP_200_OK)
    except:
      return Response({"status":"failed",},status=status.HTTP_404_NOT_FOUND)
