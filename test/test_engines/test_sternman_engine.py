import unittest
import sys
sys.path.append('./')
from engines import sternman_engine

from engines.sternman_engine import SternmanEngine
class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        """
        Test that the capulet engine needs to be serviced when it should
        """
        warning_light = True
        engine = SternmanEngine(warning_light)
        result = engine.needs_service()
        self.assertTrue(result)

    def test_needs_service_false(self):
        """
        Test that the capulet engine needs to be serviced when it should not
        """
        warning_light = False
        engine = SternmanEngine(warning_light)
        result = engine.needs_service()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()