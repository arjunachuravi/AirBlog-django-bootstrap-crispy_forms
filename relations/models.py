from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class relativity(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc  = models.TextField(max_length=100)
    tech  = models.CharField(max_length=50)
    time  = models.DateTimeField(auto_now_add=True)

    def thetitle(self,*args, **kwargs):
        return "%s : %s" %(self.author.username,self.title)

    def __str__(self):
        return self.thetitle(self)

    def get_absolute_url(self):
        return reverse("", kwargs={"pk": self.pk})