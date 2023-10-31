from django.contrib import admin
from django.urls import path

from challenge.apps.core.api.v1.views import MessageListCreateAPIView
from challenge.apps.core.api.v1.views import MessageRetrieveUpdateDestroyAPIView
from challenge.apps.users.api.v1.views import UserDataListCreateAPIView
from challenge.apps.users.api.v1.views import UserDataRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", UserDataListCreateAPIView.as_view(), name="Users"),
    path("api/v1/users/<str:pk>/", UserDataRetrieveUpdateDestroyAPIView.as_view(), name="Users"),
    path("api/v1/messages/", MessageListCreateAPIView.as_view(), name="messages"),
    path("api/v1/messages/<str:pk>/", MessageRetrieveUpdateDestroyAPIView.as_view(), name="messages"),
]
