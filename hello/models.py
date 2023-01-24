import uuid
from django.db import models

# Create your models here.
class slider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ImageField(upload_to="./static/img/media")
    title = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.title