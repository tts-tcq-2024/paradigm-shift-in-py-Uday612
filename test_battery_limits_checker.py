import unittest
from check_limits import battery_is_ok

class TestBatteryIsOk(unittest.TestCase):

  def test_temperatureOutOfRange(self):
    self.assertEqual(battery_is_ok(50, 50, 0.7),False)

  def test_socOutOfRange(self):
    self.assertEqual(battery_is_ok(40, 10, 0),False)

  def test_chargeRateOutOfRange(self):
    self.assertEqual(battery_is_ok(30, 50, 0.9),False)

  def test_prametersInRange(self):
    self.assertEqual(battery_is_ok(40, 60, 0.7),True)
