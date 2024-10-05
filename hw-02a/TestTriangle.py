# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput', '0,0,0 InvalidInput')
        self.assertEqual(classifyTriangle(201,3,4), 'InvalidInput', '201,3,4 InvalidInput')
        self.assertEqual(classifyTriangle(-2,-2,-2), 'InvalidInput', '-2,-2,-2 InvalidInput')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(2,4,8), 'NotATriangle', '2,4,8  NotATriangle')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(8,6,4), 'Scalene', '8,6,4 is a Scalene triangle')
    
    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(3,3,4), 'Isoceles', '3,3,4 is an Isoceles triangle')
    


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(argv=[''], exit=False)

