from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator



class Genre(models.TextChoices):
    HIP_HOP ='HH'
    SYNTH_POP ='SP'
    ALTERNATIVE_ROCK ='AR'



class Band(models.Model):
    
    # like_new =models.fields.BooleanField(default=False)   
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=5, choices=Genre.choices)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.IntegerField(validators= [MinValueValidator(1900),MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True,blank=True)
    
    
    def __str__(self):
        return f'{self.name}'
    
    
class Listing(models.Model):
    
     
    class ListingType(models.TextChoices):
         RECORDS ='R'
         CLOTHING ='C'
         POSTER ='P'
         NISC ='N'
         
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True,blank=True, default=2004)
    type= models.fields.CharField(choices=ListingType.choices,max_length=5)
    band =models.ForeignKey("Band",null=True ,on_delete=models.SET_NULL)
    
    
    def __str__(self):
        return self.title
    