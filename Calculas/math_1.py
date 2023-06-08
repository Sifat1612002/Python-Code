
# import math
import sympy

from sympy import *
# a = math.sqrt(8)
# print(a)
# b = sympy.sqrt(8)
# print(b)
# init_printing(use_unicode=True)
# c = sqrt(8)
# print(c)

x, y, z = symbols('x y z')
# d = factor(x**2 + 2*x*y + y**2)
# print(d)

# e = expand((x+y+z)**2)
# print(e)

p = symbols('p')
f = p*(1-p)
plot(f, xlim=(-0.2, 1.2), ylim=(0, 0.25))
s = solveset(Eq(f))
print(s)
