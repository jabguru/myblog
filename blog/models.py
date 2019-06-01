from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile', null=True)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, unique=True)
    featured_image = models.ImageField(upload_to='featured-images/', null=True, blank=True)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    is_featured = models.BooleanField(null=True,default=False)

    def __str__(self):

        return '{} pubished on {}'.format(self.title, self.published.strftime('%d %B, %Y'))

class Featured_Post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='featured')

    def __str__(self):
        return self.post.title


class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default = True)

    def __str__ (self):
        return 'comment by {} on {}'.format(self.name, self.post)