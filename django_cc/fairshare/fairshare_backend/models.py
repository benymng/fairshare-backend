from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published testing')

    def __str__(self):
        return self.title

class Users(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
