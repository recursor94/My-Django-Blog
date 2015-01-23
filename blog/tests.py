from django.test import TestCase
from django.utils import timezone
from blog.models import Post
import datetime

# Create your tests here.
class PostMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for posts whose
        pub_date is in the future"
        """
        time = timezone.now() + datetime.timedelta(days=30) #one month in future
        future_post = Post(pub_date=time)
        self.assertEqual(future_post.was_published_recently(), False)

    def test_was_published_recently_with_distant_past_question(self):
        """
        was published_recently() should return False
        for posts whose pub_date is in the distant future
        """
        time = timezone.now() - datetime.timedelta(days=30)
        distant_past_post = Post(pub_date=time)
        self.assertEqual(distant_past_post.was_published_recently(), False)
