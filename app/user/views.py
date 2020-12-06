from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateeAPIView):
    """ create a newe user in the system """
    serializer_class = UserSerializer
    

