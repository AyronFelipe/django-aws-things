import pytest

from django.urls import reverse
from rest_framework import status

from challenge.apps.core.models import Message
from challenge.apps.users.models import UserData


@pytest.mark.django_db
class TestCreateUsersEndpoint:
    endpoint_url = reverse("users-create-list")

    def test_should_return_201_when_post_is_made(self, api_client, mocker):
        mocker.patch("challenge.support.decorators.send")
        mocker.patch("challenge.apps.users.api.v1.views.call_lambda", return_value=1995)
        body = {"name": "Name", "email": "email@gmail.com", "age": "28"}
        res = api_client.post(self.endpoint_url, body, format="json")
        assert UserData.objects.count() == 1
        assert Message.objects.count() == 2
        assert res.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
class TestRetrieveUpdateDestroyUsersEndpoint:
    @pytest.fixture
    def user_data(self):
        user_data = UserData.objects.create(**{"name": "Name", "email": "email@gmail.com", "age": "28"})
        return user_data

    @pytest.mark.django_db
    def test_retrieve_user_data(self, api_client, user_data):
        response = api_client.get(reverse("users-retrieve-update-delete", args=[user_data.id]))
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_update_user_data(self, api_client, user_data):
        new_data = {"name": "New Value"}
        response = api_client.patch(
            reverse("users-retrieve-update-delete", args=[user_data.id]), new_data, format="json"
        )
        assert response.status_code == status.HTTP_200_OK

        user_data.refresh_from_db()
        assert user_data.name == "New Value"

    @pytest.mark.django_db
    def test_delete_user_data(self, api_client, user_data):
        response = api_client.delete(reverse("users-retrieve-update-delete", args=[user_data.id]))
        assert UserData.objects.count() == 0
        assert response.status_code == status.HTTP_204_NO_CONTENT
