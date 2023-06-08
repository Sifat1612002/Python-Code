import sympy as sp
from sympy import *
init_printing()

x = sp.symbols('x')
f = 105*(x**2)*(1-x)**4
# sp.plot(f, xlim=[0, 1], ylim=[0, 2.5], show=True)
i = Integral(x*f, (x, 0, 1)).doit()
ii = Integral((x**2)*f, (x, 0, 1)).doit()
sd = (ii-i**2)**0.5
print(sd)
