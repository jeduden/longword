from django.test import TestCase

from game.models import acceptWord,normalizeWord;

class TestAcceptWord(TestCase):
    
    def test_empty_not_accepted(self):
        self.assertFalse(acceptWord(''))


    def test_simple_english_accepted(self):
        self.assertTrue(acceptWord('cat'))
        self.assertTrue(acceptWord('mouse'))


    def test_english_words_with_space_rejected(self):
        self.assertFalse(acceptWord('high school students'))


    def test_english_words_with_hyphens_rejected(self):
        self.assertFalse(acceptWord('high-risk'))


    def test_non_english_words_rejected(self):
        self.assertFalse(acceptWord('hfwfwuibfwisk'))

       
    def test_english_word_plus_non_english_rejected(self):
        self.assertFalse(acceptWord('cat hfwfwuibfwisk'))



class TestNormalizeWord(TestCase):
    
    def test_empty_maps_to_empty(self):
        self.assertEquals(normalizeWord(''),'')


    def test_just_whitespace_maps_to_empty(self):
        self.assertEquals(normalizeWord('   \t\n'),'')

    def test_no_whitespace_leaves_word_intact(self):
        self.assertEquals(normalizeWord('hello'),'hello')


    def test_whitespace_world_is_collapsed_into_single(self):
        self.assertEquals(normalizeWord('hello\t\nworld'),'hello world')

    def test_remove_whitespace_at_the_beginning_and_end(self):
        self.assertEquals(normalizeWord('  hello  '),'hello')


