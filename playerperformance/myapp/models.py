from django.db import models

class PlayerInput(models.Model):
    pace = models.FloatField()
    shooting = models.FloatField()
    passing = models.FloatField()
    dribbling = models.FloatField()
    defending = models.FloatField()
    physic = models.FloatField()
    prediction = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
