# test_triangle.py

"""import another class"""
import unittest
from Triangle import classifyTriangle  # type: ignore

class TestTriangles(unittest.TestCase):
    """here test cases for the classifyTriangle function."""

    def test_right_triangle_a(self):
        """Test that 3, 4, 5 is classified as a Right triangle."""
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """Test that 5, 3, 4 is classified as a Right triangle."""
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        """Test that 1, 1, 1 is classified as an Equilateral triangle."""
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 is an Equilateral')

    def test_invalid_input(self):
        """Test invalid inputs for the classifyTriangle function."""
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 is an InvalidInput')
        self.assertEqual(classifyTriangle(201, 3, 4), 'InvalidInput', '201,3,4 is an InvalidInput')
        self.assertEqual(classifyTriangle(-2, -2, -2), 'InvalidInput', '-2,-2,-2 is an InvalidInput')

    def test_not_a_triangle(self):
        """Test that 2, 4, 8 does not form a triangle."""
        self.assertEqual(classifyTriangle(2, 4, 8), 'NotATriangle', '2,4,8 is a NotATriangle')

    def test_scalene_triangle(self):
        """Test that 8, 6, 4 is classified as a Scalene triangle."""
        self.assertEqual(classifyTriangle(8, 6, 4), 'Scalene', '8,6,4 is a Scalene')

    def test_isosceles_triangle(self):
        """Test that 3, 3, 4 is classified as an Isosceles triangle."""
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isoceles', '3,3,4 is an Isoceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(argv=[''], exit=False)
