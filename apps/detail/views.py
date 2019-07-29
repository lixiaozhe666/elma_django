# -*- coding:utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from apps.detail.models import TaskModel,SellerModel
from apps.detail.serializers import TaskSerializer,SellerSerializer


# 第一种方式：APIView
class TaskList(APIView):
    def get(self, request, format=None):
        tasks = TaskModel.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerList(APIView):
    def get(self, request, format=None):
        tasks = SellerModel.objects.all()
        serializer = SellerSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)