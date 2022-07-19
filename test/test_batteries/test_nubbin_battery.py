import unittest
import sys
sys.path.append('./')

from datetime import datetime
from batteries.nubbin_battery import NubbinBattery
class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        """
        Test that the nubbin battery needs to be serviced when it should
        """
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5) #5 years in the past
        battery = NubbinBattery(last_service_date, today)
        result = battery.needs_service()
        self.assertTrue(result)

    def test_needs_service_false(self):
        """
        Test that the nubbin battery needs to be serviced when it should not
        """
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2) #2 years in the past
        battery = NubbinBattery(last_service_date, today)
        result = battery.needs_service()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()