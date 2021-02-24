from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model



from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username='Jack123')
    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user = User.objects.first(),
            content = 'Some Random Content'
        )
        self.assertTrue(obj.content == 'Some Random Content')
        self.assertTrue(obj.id == 1)
        
        absolute_url = reverse("tweet:detail" , kwargs={"pk":1})
        self.assertEqual(obj.get_absolute_url() , absolute_url)

    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user = User.objects.first(),
            content = 'Some Random Content'
        )

        absolute_url = reverse("tweet:detail" ,kwargs={"pk":obj.pk})
        self.assertEqual(obj.get_absolute_url() , absolute_url)

# Create your tests here.
