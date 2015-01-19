import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title_text = models.CharField(max_length = 500)
    pub_date = models.DateTimeField('date published');
    content =  models.TextField();

    #methods
    def __unicode__(self):
        return self.title_text + "\n"+ self.pub_date.__str__() + "\n" + self.content
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1);

    

    


