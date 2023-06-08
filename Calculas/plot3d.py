from sympy import *
from sympy.plotting import plot3d
from sympy.abc import x, y
init_printing()
F = x**2 + y**2-2*x-6*y+14
plot3d(F, (x, -3, 5), (y, 0, 6))
