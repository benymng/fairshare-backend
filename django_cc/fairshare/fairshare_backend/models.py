from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published testing')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"Comment by {self.author} on '{self.post.title}'"
