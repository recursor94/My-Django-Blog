from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
import datetime


# Create your models here.
class Post(models.Model):
    title_text = models.CharField(max_length = 500)
    pub_date = models.DateTimeField('date published')
    content =  models.TextField()
    slug = models.SlugField(max_length=100, db_index=True, blank=True)

    #methods
    def __unicode__(self):
        return self.title_text + "\n"+ self.pub_date.__str__() + "\n" + self.content
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title_text)    #newly created object, set slug
        super(Post, self).save(*args, **kwargs)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'




    
