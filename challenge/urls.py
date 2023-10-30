from django.contrib import admin
from django.urls import path

from challenge.apps.users.api.v1.views import UserDataListCreateAPIView
from challenge.apps.users.api.v1.views import UserDataRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", UserDataListCreateAPIView.as_view(), name="Users"),
    path("api/v1/users/<str:pk>/", UserDataRetrieveUpdateDestroyAPIView.as_view(), name="Users"),
]
