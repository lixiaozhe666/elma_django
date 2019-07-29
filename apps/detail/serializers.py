# -*- coding:utf-8 -*-
from rest_framework import serializers
from apps.detail.models import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ('id', 'title', 'description', 'completed', 'create_date')