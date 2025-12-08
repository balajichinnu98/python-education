import unittest
from p2hw import Cylinder

class TestClassLine(unittest.TestCase):
    def test_surface_area(self):
       cylinder = Cylinder(3,3)
       self.assertAlmostEqual(cylinder.surface_area(), 113.09724) 

    def test_volume(self):
       cylinder = Cylinder(3,3)
       self.assertAlmostEqual(cylinder.volume(), 84.82293)   
    
if __name__ == "__main__":
    unittest.main()



