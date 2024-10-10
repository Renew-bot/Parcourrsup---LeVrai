from django.db import models

class Bonjour(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)
