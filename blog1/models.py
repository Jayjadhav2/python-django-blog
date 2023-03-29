from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title

        
    def get_absolute_url(self):
        return reverse('home')
        return reverse('post-detail',kwargs={'pk':self.pk})
        

    '''
    Django DateTimeField represents the timestamp with timezone in the database. 
    That means it displays the date and time in one of the default formats 
    (unless otherwise stated).
    '''
    '''
    What are primary and foreign keys SQL?
    A primary key is used to ensure data in the specific column is unique.
    A foreign key is a column or group of columns
    in a relational database table that provides a link between data in two tables.
    It uniquely identifies a record in the relational database table.    
    '''
    '''
    Cascade emulates the SQL constraint of ON DELETE CASCADE.
    Whenever the referenced object (post) is deleted, the objects referencing it (comments) are deleted as well. This behaviour is a reasonable default and makes sense for most relationships — for this one as well.
    You don’t want orphaned comments lying around in your database 
    when the associated post is deleted.
    
    '''
    '''
    What is the difference between migrate and Makemigrations in Python?
    So the difference between makemigrations and migrate is this: 
    makemigrations auto generates migration files containing changes 
    that need to be applied to the database, 
    but doesn't actually change anyhting in your database. 
    migrate will make the actual modifications to your database, based on the migration files.

    OR 

    Makemigrations: 
    This command prepares a makemigrations file for our new model, or creates 
    a new migrations file for any changes if the models have been modified.
    This command does not create or affect these changes to the database.

    Migrate:
    The migrate command runs the instructions defined in the recent migrations file on the database.
    
    
    '''
   