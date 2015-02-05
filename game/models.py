from django.db import models
from django.conf import settings

class WordSubmission(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    word = models.TextField()
    
    def score(self):
        return len(self.world);

