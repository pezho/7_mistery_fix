from math import sqrt
import sys


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
    
    
if __name__ == '__main__':
    print('First root is: "{}"\nSecond root is: "{}"'
          .format(*get_roots(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))))
