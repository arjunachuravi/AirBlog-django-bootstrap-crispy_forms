from django.db import models

class myprojectblog(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.TextField(max_length=100)
    tech  = models.CharField(max_length=50)
    time  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title