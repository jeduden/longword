from django.db import models
from django.conf import settings
import enchant;

englishDict = enchant.Dict('en_US')

def acceptWord(word):
    if len(word) == 0:
        return False
    else:
        return englishDict.check(word)

class WordSubmission(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    word = models.TextField()
    
    def score(self):
        return len(self.world);

