from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=0)
    order = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)