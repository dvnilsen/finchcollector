from django.db import models
from django.urls import reverse 
from datetime import date

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

##### START ----->
class Tree(models.Model):
  kind = models.CharField(max_length=50)

  def __str__(self):
    return self.kind

  def get_absolute_url(self):
    return reverse('trees_detail', kwargs={'pk': self.id})
##### END

##### START -----> 
class Finch(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  gender = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  # Add the M:M relationship
  trees = models.ManyToManyField(Tree)

# changing this instance method does not impact the database, 
# therefore no "makemigrations" is necessary 
  def __str__(self):
    return f"{self.name} ({self.id})"
  
  def get_absolute_url(self):
    return reverse("detail", kwargs={"finch_id": self.id})
##### END

##### START ----->
class Feeding(models.Model):
  date = models.DateField("Feeding Date")
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
  # Create a cat_id FK
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"
##### END