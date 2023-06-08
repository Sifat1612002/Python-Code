from sympy import *
from sympy.abc import x, y
init_printing()

# idx = idiff(x**2+y**2-25, y, x)
# print(idx)
num = (5**x)+(5**(-x))
den = (5**x)-(5**(-x))
f = num/den
# plot(f, xlim=(-9, 9), ylim=(-2, 2))
lim = limit(f, x, -oo)
print(lim)
