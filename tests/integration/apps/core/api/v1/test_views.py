import pytest

from django.urls import reverse
from rest_framework import status

from challenge.apps.core.models import Message


@pytest.mark.django_db
class TestCreateMessageEndpoint:
    endpoint_url = reverse("messages-create-list")

    def test_should_return_201_when_message_is_created(self, api_client):
        body = {"destination": "SomeQueueDestination", "body": {"key": "value"}}
        res = api_client.post(self.endpoint_url, body, format="json")
        assert Message.objects.count() == 1
        assert res.status_code == status.HTTP_201_CREATED

    def test_should_return_400_when_body_is_empty(self, api_client):
        body = {}
        res = api_client.post(self.endpoint_url, body, format="json")
        assert Message.objects.count() == 0
        assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_should_return_200_when_get_is_made(self, api_client):
        message = Message.objects.create(destination="SomeQueueDestination", body={"key": "value"})
        res = api_client.get(self.endpoint_url, format="json")
        assert res.status_code == status.HTTP_200_OK
        assert res.json() == [
            {
                "id": str(message.id),
                "destination": "SomeQueueDestination",
                "body": {"key": "value"},
                "status": 1,
            }
        ]
