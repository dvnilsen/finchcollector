from django.db import models
from django.urls import reverse 

# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  gender = models.CharField(max_length=100)
  location = models.CharField(max_length=100)

# changing this instance method does not impact the database, 
# therefore no "makemigrations" is necessary 
  def __str__(self):
    return f"{self.name} ({self.id})"
  
  def get_absolute_url(self):
    return reverse("detail", kwargs={"finch_id": self.id})