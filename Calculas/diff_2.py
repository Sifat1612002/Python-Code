from sympy import *
init_printing()

x = symbols('x')
xmod = Piecewise((-x, x < 0), (x, x >= 0))
plot(xmod, xlim=(-4, 4), ylim=(0, 5), adaptive=False)
dx = diff(xmod, x)
print(dx)
