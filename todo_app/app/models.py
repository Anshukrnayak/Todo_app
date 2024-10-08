from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskModel(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_done=models.BooleanField(default=False)

    def __str__(self): return self.name

