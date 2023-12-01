from . models import * 
from . serializers import * 
from rest_framework import generics 

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class CourseList(generics.ListCreateAPIView):
    queryset = Addcourse.objects.all()
    serializer_class = CourseSerializer   
