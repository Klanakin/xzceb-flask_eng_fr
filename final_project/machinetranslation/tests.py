import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """ Test Translators """
    tracemalloc.start()

    def test_english_to_french(self):
        """ Test function returns French translation and not null """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french(""), None)

    def test_french_to_english(self):
        """ Test function returns English translation and not null """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english(""), None)


if __name__ == '__main__':
    unittest.main()