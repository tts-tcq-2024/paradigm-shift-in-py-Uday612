import unittest
from languages import get_message, preferred_language, set_preferred_language

class TestLanguagesSupported(unittest.TestCase):

  def test_set_preferred_language(self):
    set_preferred_language("english")
    self.assertEqual(preferred_language,"english")
    set_preferred_language("german")
    self.assertEqual(preferred_language,"german")
    
  def test_english(self):
    set_preferred_language("english")
    self.assertEqual(get_message("temperature"),"Temperature is out of range")
    self.assertEqual(get_message("soc"),"Temperature is out of range")
    self.assertEqual(get_message("charge"),"Temperature is out of range")

  def test_german(self):
    set_preferred_language("german")
    self.assertEqual(get_message("temperature"),"Die Temperatur liegt außerhalb des zulässigen Bereichs")
    self.assertEqual(get_message("soc"),"Der SOC liegt außerhalb des zulässigen Bereichs")
    self.assertEqual(get_message("charge"),"Die Ladung liegt außerhalb der Reichweite")

if __name__ == '__main__':
    unittest.main()
