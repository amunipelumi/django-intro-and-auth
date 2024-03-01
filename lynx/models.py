from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=128)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:

        return self.title
    
    class Meta:

        verbose_name_plural = 'Blog Posts'
        
