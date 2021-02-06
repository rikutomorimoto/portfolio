from django.shortcuts import render

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.contrib.auth.models import User

from .models import BigThree
from rest_framework import viewsets
from .serializers import UserSerializer,BigThreeSerializer
from .ownpermissions import ProfilePermission

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ProfilePermission,)

class ManageUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

class BigThreeViewSet(viewsets.ModelViewSet):
    queryset = BigThree.objects.all()
    serializer_class = BigThreeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)