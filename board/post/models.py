from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    board_name = models.CharField(max_length=20, unique=True)
    board_description = models.TextField(max_length=200)
def __str__(self):
    return self.board_name
class Post(models.Model):
    post_name = models.CharField(max_length=20)
    post_description = models.TextField(max_length=200)
    board = models.ForeignKey(Board,related_name='posts',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.post_name
class Post_comment(models.Model):
    comment_content = models.TextField(max_length=200)
    comments = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment_content