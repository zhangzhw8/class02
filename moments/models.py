from django.db import models
# Create your models here.
from django.conf import settings


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    text = models.CharField(max_length=280)
    pics = models.CharField(max_length=100, null=True, blank=True)
    pub_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-id"]

class Reply(models.Model):
    status = models.ForeignKey(Status, models.CASCADE)
    author = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=[("0", "like"),("1", "comment")])
    at_person = models.CharField(max_length=50, null=True, blank=True)
    text = models.CharField(max_length=280, null=True, blank=True)

    def __str__(self):
        return "{} on {}".format(self.author, self.status.text)