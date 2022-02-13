from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title