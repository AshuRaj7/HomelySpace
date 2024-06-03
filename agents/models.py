from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='agent_profiles/')
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.name
