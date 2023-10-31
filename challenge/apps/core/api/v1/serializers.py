from rest_framework import serializers

from challenge.apps.core.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "destination", "body", "status"]
