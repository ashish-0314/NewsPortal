# from django.db import models

# # Create your models here.


from django.db import models

class Article(models.Model):

    headline = models.CharField(max_length=200)

    body = models.TextField()

    author_name = models.CharField(max_length=100)

    published = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ('can_publish', 'Can publish article'),
        ]

    def __str__(self):
        return self.headline