import unittest
import sys
sys.path.append('./')

from datetime import datetime
from batteries.nubbin_battery import NubbinBattery
class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced_5_years(self):
        """
        Test that the nubbin battery needs to be serviced when it should
        If 4 years has passed, should return true 
        """
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5) #5 years in the past
        nubbin_battery = NubbinBattery(last_service_date, today)
        result = nubbin_battery.needs_service()
        self.assertTrue(result)

    def test_nubbin_battery_should_be_serviced_2_years(self):
        """
        Test that the nubbin battery needs to be serviced when it should not
        If 4 years has not passed, should return false 
        """
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2) #2 years in the past
        nubbin_battery = NubbinBattery(last_service_date, today)
        result = nubbin_battery.needs_service()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()