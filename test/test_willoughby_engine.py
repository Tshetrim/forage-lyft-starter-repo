import unittest
import sys
sys.path.append('./')

from engines import willoughby_engine
from engines import willoughby_engine

from engines.willoughby_engine import WilloughbyEngine
class TestCapuletEngine(unittest.TestCase):
    def test_willoughby_engine_should_be_serviced_5_years(self):
        """
        Test that the capulet engine needs to be serviced when it should
        If it has been more than 60,000 miles since last servicing, should return true
        """
        current_mileage = 100000
        last_service_mileage = 10000
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        result = willoughby_engine.needs_service()
        self.assertTrue(result)

    def test_willoughby_engine_should_be_serviced_2_years(self):
        """
        Test that the capulet engine needs to be serviced when it should
        If it has been less than 60,000 miles since last servicing, should return false  
        """
        current_mileage = 20000
        last_service_mileage = 10000
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        result = willoughby_engine.needs_service()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()