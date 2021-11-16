from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    last_modified = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.id})
        


