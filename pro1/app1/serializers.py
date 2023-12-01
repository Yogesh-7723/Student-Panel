from rest_framework import serializers 
from . models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addcourse 
        fields = "__all__"