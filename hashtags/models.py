from django.db import models
from tweets.models import Tweet
from django.urls import reverse_lazy
# Create your models here.
class HashTag(models.Model):
    tag = models.CharField(max_length = 120)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse_lazy("hashtags",kwargs={"hashtags":self.tag})

    def get_tweets(self):
        return Tweet.objects.filter(content__icontains="#"+self.tag)