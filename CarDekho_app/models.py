from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

isalphaNumeric=RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')



class ShowRoomList(models.Model):
    name= models.CharField(max_length=50)
    location= models.CharField(max_length=100)
    website= models.URLField(max_length=100)

    def __str__(self):
        return self.name



class CarList(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    chassisNumber=models.CharField(max_length=100,blank=True,null=True,validators=[isalphaNumeric])
    price=models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    showroom=models.ForeignKey(ShowRoomList,on_delete=models.CASCADE,related_name="Showrooms",null=True)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    rating=models.IntegerField(validators = [MaxValueValidator,MinValueValidator])
    comments=models.CharField(max_length = 200,null = True)
    car=models.ForeignKey(CarList,on_delete = models.CASCADE,related_name='Reviews',null=True)
    created=models.DateTimeField(auto_now_add = True)
    updated=models.DateTimeField(auto_now = True)

    def __str__(self):
        return "The rating of " + self.car.name + ":--- " + str(self.rating) 