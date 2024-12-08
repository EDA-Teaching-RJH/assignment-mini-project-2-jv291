import unittest
from word_game import WordGame, ExtendedWordGame

class TestWordGame(unittest.TestCase):
    def setUp(self):
        self.game + WordGame(['python', 'java', 'ruby'])

    def test_guess_word_correct(self):
        self.game.current_word = 'python'
        self.assertTrue(self.game.guess_word('Python'))

    def test_guess_word_incorrect(self):
        self.game.current_word = 'python'
        self.assertFalse(self.game.guess_word('Java'))
    
    def test_guess_word_invalid(self):
        self.assertFalse(self.game.guess_word('123'))

class TestExtendedWordGame(unittest.TestCase):
    def setUp(self):
        self.game = ExtendedWordGame(['python', 'java', 'ruby'])
        self.game.current_word = 'python'

    def test_provide_hint(self):
        self.assertEqual(self.game.provide_hint(), "Hint: The word start with 'p'.")
if __name__ == '__main__':
    unittest.main()