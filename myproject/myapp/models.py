#Importing models 
from django.db import models

# Making a register model
class Register(models.Model):
    fname = models.CharField(max_length = 50)
    username = models.CharField(max_length = 500, unique = True)
    email  = models.EmailField(max_length = 50)
    passw =  models.CharField(max_length=100)
    # Whenever any sql query is performed on register we get username displayed for each
    def __str__(self):
        return self.username
    
# Making a quiz model

class Quiz(models.Model):
    category = models.CharField(max_length = 50)
    question = models.CharField(max_length = 10000, unique = True)
    option_a = models.CharField(max_length = 1000)
    option_b = models.CharField(max_length = 1000)
    option_c = models.CharField(max_length = 1000)
    option_d = models.CharField(max_length = 1000)
    solution = models.IntegerField()
    
    def __str__(self):
        return self.category
    
# Making a model for the scores 
class Score(models.Model):
    category = models.CharField(max_length = 50)
    user = models.CharField(max_length = 50)
    score = models.IntegerField()