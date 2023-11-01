from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView

from challenge.apps.core.api.v1.views import MessageListCreateAPIView
from challenge.apps.core.api.v1.views import MessageRetrieveUpdateDestroyAPIView
from challenge.apps.users.api.v1.views import UserDataListCreateAPIView
from challenge.apps.users.api.v1.views import UserDataRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", UserDataListCreateAPIView.as_view(), name="users-create-list"),
    path("api/v1/users/<str:pk>/", UserDataRetrieveUpdateDestroyAPIView.as_view(), name="users-retrieve-update-delete"),
    path("api/v1/messages/", MessageListCreateAPIView.as_view(), name="messages-create-list"),
    path(
        "api/v1/messages/<str:pk>/",
        MessageRetrieveUpdateDestroyAPIView.as_view(),
        name="messages-retrieve-update-delete",
    ),
    path("iapi/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("iapi/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("iapi/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
