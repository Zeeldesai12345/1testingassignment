import unittest

def classify_triangle(a, b, c):
    # Using the following statement to check if it's a valid triangle or not:
    if a + b <= c or b + c <= a or a + c <= b:                   
        return "This is not a triangle"

    # Following shows which type of triangle:
    if a == b == c:
        return "This is an Equilateral triangle" 
    elif a == b or b == c or a == c:
        return "This is an Isosceles triangle"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "This is a right angle triangle"  
    else:
        return "This is a Scalene triangle"

if __name__ == "__main__":
    # Take user input
    a = int(input("Enter the length of side a: "))
    b = int(input("Enter the length of side b: "))
    c = int(input("Enter the length of side c: "))

    type_of_triangle = classify_triangle(a, b, c)
    print(f" {type_of_triangle}")

# Unit tests for the classify_triangle function
class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "This is an Equilateral triangle")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "This is an Isosceles triangle")

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "This is a right angle triangle")  

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "This is not a triangle")

    def test_scalene_not_right_angle(self):
        self.assertEqual(classify_triangle(7, 9, 11), "This is a Scalene triangle")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
