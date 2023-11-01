from django.conf import settings
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from challenge.apps.users.api.v1.serializers import UserDataSerializer
from challenge.apps.users.models import UserData
from challenge.support.utils import call_lambda


class UserDataListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance: UserData = serializer.save()
        result = call_lambda(
            function_name=settings.LAMBDA_FUNCTION_CALCULATE_DATE_OF_BIRTH_FUNCTION, body=instance.body_to_sent()
        )

        instance.year_of_birthday = result
        instance.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDataRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
