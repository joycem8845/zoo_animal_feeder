from django.db import models

# Create your models here.

class AnimalType(models.Model):
    """Type of animal that can classify the animal"""
    a_type = models.CharField(max_length=50)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.a_type

class Animal(models.Model):
    """The actual animal, embeded in animaltype"""
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        if len(self.name)>20:
            return self.name[:20] + "..."
        else:
            return self.name

class Schedule(models.Model):
    """Model for animal eating schedule"""
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
