from django.db import models


class Follower(models.Model):
    email = models.EmailField(unique=True, max_length=100)

    def __str__(self) -> str:
        return self.email

