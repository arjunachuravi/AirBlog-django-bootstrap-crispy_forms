from django.db import models

from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.ForeignKey(User, verbose_name="related_user", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username