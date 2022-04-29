from django.db import models

# Create your models here.
#Creatig models to post tweet and retweet the tweets & Timeline ofor user
from accounts.models import UserManagement


def post_directory_path(instance, filename):
    print(instance)
    return 'post_{0}/{1}'.format(instance, filename)


class Post(models.Model):
    tweet = models.TextField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    post_img = models.ImageField(upload_to='postimg',blank=True)
    user_id = models.ForeignKey(UserManagement,models.DO_NOTHING)
    #
    def __str__(self):
        return self.tweet

    def get_absolute_url(self):
        return reverse('postimg', args=[self.slug])



class Retweet(models.Model):
    tweet_id = models.ForeignKey(Post,models.DO_NOTHING)
    user_id = models.ForeignKey(UserManagement,models.DO_NOTHING)
    retweet_stamp = models.DateTimeField(auto_now_add=True)
    retweet_text = models.TextField(max_length=150,blank=True)


class Timeline(models.Model):
    post_id = models.ForeignKey(Post,models.DO_NOTHING)
    retweet_id = models.ForeignKey(Retweet,models.DO_NOTHING)
