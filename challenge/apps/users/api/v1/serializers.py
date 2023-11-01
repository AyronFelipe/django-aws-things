from rest_framework import serializers

from challenge.apps.users.models import UserData


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["id", "name", "email", "age", "year_of_birthday"]
