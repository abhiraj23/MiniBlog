from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    user_post = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    