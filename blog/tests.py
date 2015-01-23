from django.test import TestCase
from django.utils import timezone
from blog.models import Post
import datetime

# Create your tests here.

#helper functions

def create_post(title_text, days):
    """
    Creates a post with title as title_text and number of days offset to now
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Post.objects.create(title_text=title_text, pub_date=time)
    
class PostMethodTests(TestCase):
    def test_was_published_recently_with_future_post(self):
        """
        was_published_recently() should return False for posts whose
        pub_date is in the future"
        """
        time = timezone.now() + datetime.timedelta(days=30) #one month in future
        future_post = Post(pub_date=time)
        self.assertEqual(future_post.was_published_recently(), False)

    def test_was_published_recently_with_distant_past_post(self):
        """
        was published_recently() should return False
        for posts whose pub_date is in the distant future
        """
        time = timezone.now() - datetime.timedelta(days=30)
        distant_past_post = Post(pub_date=time)
        self.assertEqual(distant_past_post.was_published_recently(), False)

        def test_was_published_recently_with_near_past_post(self):
            """
            was published_recently should return True for posts whose pub_date
            was in the recent past--in this case less than or equal to one day
            old
            """
            time=timezone.now() - datetime(days=1)
            near_past_post = Post(pub_date=time)
            self.assertEqual(distant_past_post.was_published_recently(), True)

        def test_index_view_with_a_future_post(self):

            """Questions with a pub_date in the future should not be
            displayed on the index page"""

            create_post(question_text="Future Post", days=30)
            response = self.client.get(reverse('blog:index'))
            self.assertContains(response, "No posts are available",
                                status_code = 200)
            slef.assertQuerysetEqual(response.context['post_list'],
                                     [])
            

