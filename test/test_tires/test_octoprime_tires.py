import unittest
import sys

sys.path.append('./')

from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        """
        Test that the carrigan tires needs to be serviced
        """
        tireList = [.1,.1,.1,0]
        tires = OctoprimeTires(tireList)
        result = tires.needs_service()
        self.assertTrue(result)
    
    def test_needs_service_false(self):
        """
        Test that the carrigan tires needs to be serviced
        """
        tireList = [0,0,.1,.1]
        tires = OctoprimeTires(tireList)
        result = tires.needs_service()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()