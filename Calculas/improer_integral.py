from sympy import *
from sympy.plotting import plot3d
init_printing()

t = Symbol('t', positve=True)
lamda = Symbol('lamda', positve=True)

pdf = lamda * exp(-lamda * t)
xi = Integral(pdf, (t, 0, oo)).doit()
print(xi)
p1 = plot(pdf.subs(lamda, 1), xlim=[0, 3], ylim=[
          0, 2.5], legend=True, line_color='green')
p2 = plot(pdf.subs(lamda, 2), xlim=[0, 3], ylim=[
          0, 2.5], legend=True, line_color='red')
p3 = plot(pdf.subs(lamda, 3), xlim=[0, 3], ylim=[
          0, 2.5], legend=True, line_color='blue')
