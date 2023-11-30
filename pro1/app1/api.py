from . models import * 
from . serializers import * 
from rest_framework import generics 

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    
      git config --global user.email "yogeshyadav7723@gmail.com"
      
        git config --global user.name "Yogesh-7723"