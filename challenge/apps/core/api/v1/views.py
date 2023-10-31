from rest_framework import generics

from challenge.apps.core.api.v1.serializers import MessageSerializer
from challenge.apps.core.models import Message


class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
