import unittest
import sys
sys.path.append('./')

from engines import willoughby_engine
from engines import willoughby_engine

from engines.willoughby_engine import WilloughbyEngine
class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        """
        Test that the capulet engine needs to be serviced when it should
        """
        current_mileage = 100000
        last_service_mileage = 10000
        battery = WilloughbyEngine(last_service_mileage, current_mileage)
        result = battery.needs_service()
        self.assertTrue(result)

    def test_needs_service_false(self):
        """
        Test that the capulet engine needs to be serviced when it should not
        """
        current_mileage = 20000
        last_service_mileage = 10000
        battery = WilloughbyEngine(last_service_mileage, current_mileage)
        result = battery.needs_service()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()