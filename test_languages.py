import unittest
from languages import get_message, preferred_language, set_preferred_language

class TestLanguagesSupported(unittest.TestCase):

  def test_set_preferred_language(self):
    set_preferred_language("english")
    self.assertEqual(set_preferred_language,"english")
    set_preferred_language("german")
    self.assertEqual(set_preferred_language,"english")
    
  def test_english(self):
    self.assertEqual(get_message("english","temperature"),"Temperature is out of range")
    self.assertEqual(get_message("english","soc"),"Temperature is out of range")
    self.assertEqual(get_message("english","charge"),"Temperature is out of range")

  def test_german(self):
    self.assertEqual(get_message("german","temperature"),"Die Temperatur liegt außerhalb des zulässigen Bereichs")
    self.assertEqual(get_message("german","soc"),"Der SOC liegt außerhalb des zulässigen Bereichs")
    self.assertEqual(get_message("german","charge"),"Die Ladung liegt außerhalb der Reichweite")

if __name__ == '__main__':
    unittest.main()
