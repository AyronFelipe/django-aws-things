from uuid import uuid4

from django.db import models


class BaseModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name="Updated at")

    class Meta:
        abstract = True


class StandardModelMixin(BaseModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name="ID")

    class Meta:
        abstract = True
