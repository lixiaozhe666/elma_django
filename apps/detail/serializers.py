# -*- coding:utf-8 -*-
from rest_framework import serializers
from apps.detail.models import TaskModel,SellerModel


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ('id', 'title', 'description', 'completed', 'create_date')


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerModel
        fields = ('id','name','description','deliveryTime','score','serviceScore',
                  'foodScore','rankRate','minPrice','deliveryPrice','ratingCount',
                  'sellCount','bulletin','avatar','pics','infos','supports')