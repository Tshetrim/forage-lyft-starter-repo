import unittest
import sys

sys.path.append('./')

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        """
        Test that the carrigan tires needs to be serviced when it should
        """
        tireList = [.1,.1,.1,.9]
        tires = CarriganTires(tireList)
        result = tires.needs_service()
        self.assertTrue(result)
    
    def test_needs_service_false(self):
        """
        Test that the carrigan tires needs to be serviced when it should not
        """
        tireList = [.1,.1,.1,.1]
        tires = CarriganTires(tireList)
        result = tires.needs_service()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()