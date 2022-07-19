import unittest
import sys
sys.path.append('./')
from engines import sternman_engine

from engines.sternman_engine import SternmanEngine
class TestSternmanEngine(unittest.TestCase):
    def test_sernman_engine_should_be_serviced_5_years(self):
        """
        Test that the capulet engine needs to be serviced when it should
        If warning light is on, should return true
        """
        warning_light = True
        sternman_engine = SternmanEngine(warning_light)
        result = sternman_engine.needs_service()
        self.assertTrue(result)

    def test_sternman_engine_should_be_serviced_2_years(self):
        """
        Test that the capulet engine needs to be serviced when it should
        If warning light is off, should return false
        """
        warning_light = False
        sternman_engine = SternmanEngine(warning_light)
        result = sternman_engine.needs_service()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()