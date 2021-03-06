from django.db import models
from django.conf import settings
import enchant
import re

englishDict = enchant.Dict('en_US')

def acceptWord(word):
    if len(word) == 0:
        return False
    else:
        return englishDict.check(word)

def normalizeWord(word):
    return re.sub( '\s+', ' ', word ).strip()

class WordSubmission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    word = models.TextField()
    score = models.IntegerField()
    submitted = models.DateField(auto_now_add=True)
