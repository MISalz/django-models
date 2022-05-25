from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
  name = models.CharField(max_length=256)
  description = models.CharField(max_length=256)
  purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#adds names to items in db
  def __str__(self):
      return self.name