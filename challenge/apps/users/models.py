from typing import Dict

from django.db import models

from challenge.apps.core.models import StandardModelMixin
from challenge.support.decorators import send


@send(queue_name="UserDataDestination")
class UserData(StandardModelMixin):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Name of User")
    email = models.EmailField(verbose_name="E-mail of user", null=False, blank=False)
    age = models.PositiveIntegerField(verbose_name="Age of User", null=False, blank=False)
    year_of_birthday = models.PositiveIntegerField(verbose_name="Year of birthday of User", blank=True, null=True)

    def body_to_sent(self) -> Dict:
        return {"name": self.name, "email": self.email, "age": self.age, "year_of_birthday": self.year_of_birthday}
