from django.db import models

# Create your models here.
class Post(models.Model):
    title_text = models.CharField(max_length = 500)
    pub_date = models.DateTimeField('date published');
    content =  models.TextField();


    

    


