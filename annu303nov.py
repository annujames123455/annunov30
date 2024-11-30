'''
author name:annu james
date:30/11/24
'''
from operator import truediv


def is_right_angle_triangle(side1,side2,side3):
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
       return True
    return False

side1=int(input("enter the side1 of the triangle:"))
side2=int(input("enter the side2 of the triangle:"))
side3=int(input("enter the side3 of the triangle:"))
if is_right_angle_triangle(side1,side2,side3):
    print(f"the given sides are part of the right angle triangle")
else:
    print(f" the given sides are not part of the right angle triangle")







