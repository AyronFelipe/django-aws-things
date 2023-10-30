from rest_framework import generics

from challenge.apps.users.api.v1.serializers import UserDataSerializer
from challenge.apps.users.models import UserData


class UserDataListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class UserDataRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
