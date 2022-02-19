from django.db import models
from django import forms

# Create your models here.


class Board(models.Model):
    FOOD_CATEGORY = [
        ('KR', '한식'), 
        ('EA', '양식'), 
        ('CH', '중식'), 
        ('JP', '일식'), 
        ('SF', '분식'), 
        ('BR', '베이커리'), 
        ('BEV', '커피음료'), 
        ('OTHERS', '그외'),
    ]
    REVIEW_POINT_CHOICES = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    ]
    category = models.CharField(max_length=200, choices = FOOD_CATEGORY)
    title = models.CharField(max_length=200)
    points = models.CharField(max_length=200, choices=REVIEW_POINT_CHOICES, default='5')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]