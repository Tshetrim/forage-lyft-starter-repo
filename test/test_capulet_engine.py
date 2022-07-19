import unittest
import sys
sys.path.append('./')
from engines import capulet_engine

from engines.capulet_engine import CapuletEngine
class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine_should_be_serviced_5_years(self):
        """
        Test that the capulet engine needs to be serviced when it should
        If it has been more than 30,000 miles since last servicing, should return true
        """
        current_mileage = 50000
        last_service_mileage = 10000
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        result = capulet_engine.needs_service()
        self.assertTrue(result)

    def test_capulet_engine_should_be_serviced_2_years(self):
        """
        Test that the capulet engine needs to be serviced when it should
        If it has been less than 30,000 miles since last servicing, should return false  
        """
        current_mileage = 20000
        last_service_mileage = 10000
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        result = capulet_engine.needs_service()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()