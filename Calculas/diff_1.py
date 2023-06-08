import math
import sympy
from sympy import *
init_printing()

x = symbols('x')
f = sin(x)/x
plot(f, xlim=(-10, 10), ylim=(-1, 1))
L = limit(f, x, 0, '+')
print(L)
