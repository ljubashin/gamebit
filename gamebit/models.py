from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class Category(models.Model):
    caption=models.CharField(max_length=40)

    def __str__(self):
        return self.caption


class gameStudio(models.Model):
    studioname= models.CharField(max_length=80)
    studioname2= models.CharField(max_length=80, blank=True)

    def full_name(self):
        return f"{self.studioname} {self.studioname2}"

    def __str__(self):
        return self.full_name()

class Game(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to='games-titles', null=True)
    additionalImage = models.ImageField(upload_to='games', blank=True)
    backgroundImage = models.ImageField(upload_to='gamesbackground', null=True)
    date=models.DateTimeField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    gameStudio=models.ForeignKey(gameStudio,on_delete=models.SET_NULL,null=True,related_name="games")
    tag=models.ManyToManyField(Category)
    operating=models.CharField(max_length=100)
    processor=models.CharField(max_length=100)
    memory=models.CharField(max_length=100)
    graphics=models.CharField(max_length=100)
    storage=models.CharField(max_length=100)
    additional=models.CharField(max_length=100)
    downloadlink=models.URLField(max_length=200)   

    def __str__(self):
        return self.title
        
class Review(models.Model):
    user_name = models.CharField(max_length= 50)
    text = models.CharField(max_length=300)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="reviews")
    like = models.BooleanField()
    dislike = models.BooleanField(default = False)