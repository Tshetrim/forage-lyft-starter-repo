import unittest
import sys
sys.path.append('./')

from datetime import datetime
from batteries.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_should_be_serviced_5_years(self):
        """
        Test that the spindler battery needs to be serviced
        If 2 years has passed, should return true
        """
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5) #5 years in the past
        spindler_battery = SpindlerBattery(last_service_date, today)
        result = spindler_battery.needs_service()
        self.assertTrue(result)
    
    def test_spindler_battery_should_be_serviced_1_year(self):
        """
        Test that the spindler battery needs to be serviced
        If 2 years has not passed, should return false
        """
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1) #1 year in the past
        spindler_battery = SpindlerBattery(last_service_date, today)
        result = spindler_battery.needs_service()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()