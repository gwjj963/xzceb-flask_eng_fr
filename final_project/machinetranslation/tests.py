import unittest
from translator import french_to_english
from translator import english_to_french

class Testtranslator_f2e(unittest.TestCase):
      '''Test French to English translation'''
      def test_french_to_english(self):
          self.assertEqual(french_to_english('Bonjour'),'Hello')
          self.assertNotEqual(french_to_english('None'),'')

class Testtranslator_e2f(unittest.TestCase):
      '''Test English to French translation'''
      def test_english_to_french(self):
          self.assertEqual(english_to_french('Hello'),'Bonjour')
          self.assertNotEqual(english_to_french('None'),'')

unittest.main()
          