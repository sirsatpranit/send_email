from rest_framework import serializers
from employee import models


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.employee
        fields = "__all__"


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.event
        fields = "__all__"


class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.log
        fields = "__all__"