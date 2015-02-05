from django.test import TestCase

from game.models import acceptWord;

class TestAcceptWord(TestCase):
    
    def test_empty_not_accepted(self):
        self.assertFalse(acceptWord(''));


    def test_simple_english_accepted(self):
        self.assertTrue(acceptWord('cat'));
        self.assertTrue(acceptWord('mouse'));


    def test_english_words_with_space_rejected(self):
        self.assertFalse(acceptWord('high school students'));


    def test_english_words_with_hyphens_rejected(self):
        self.assertFalse(acceptWord('high-risk'));

    def test_non_english_words_rejected(self):
        self.assertFalse(acceptWord('hfwfwuibfwisk'));
       
    def test_english_word_plus_non_english_rejected(self):
        self.assertFalse(acceptWord('cat hfwfwuibfwisk'));
