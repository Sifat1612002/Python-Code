# # Importing the sympy library
# import sympy as sp
# from sympy import *
# init_printing(pretty_print=True)
# # Defining the mathematical function by using sp.symbols()
# x, y, z = sp.symbols('x y z')
# expr1 = sp.sin(x)
# # This is just to check out the graph of the mathematical function(This is not a must at all!)
# sp.plot(expr1)
# # Differentiating the given function
# diff1 = sp.diff(expr1, x)
# # Equating the derivative function to 0 and obtaining the value at which minima and maxima occurs
# check1 = sp.solve(diff1, x)
# # Differentiating the function one more to determine at what value of x do the maxima and minima occurs
# diff2 = sp.diff(diff1, x)
# # Evaluating and storing exactly at what values of x do the maxima and minima occurs
# maxmin1 = diff2.subs(x, check1[0])
# maxmin2 = diff2.subs(x, check1[1])
# # Storing the value at which maxima and minima occurs
# if maxmin1 < 0:
#     max = check1[0]
#     min = check1[1]
# elif maxmin1 > 0:
#     max = check1[1]
#     min = check1[0]
# # Substituting the value at which maxima and minima occurs in the given function we are working with
# maxval = expr1.subs(x, max)
# minval = expr1.subs(x, min)
# # this print(f"") is just a fancy formatting technique. You can print it as you please!
# print(f"Maxima is {maxval} and Minima is {minval}")
import sympy as sp
from sympy import *
init_printing(pretty_print=True)

x, y, z = sp.symbols('x y z')

expr1 = x**4-2/3*x**3-2*x**2+2*x

diff1 = sp.diff(expr1, x)
diff2 = sp.diff(diff1, x)
check1 = sp.solve(diff1, x)

soln = []
for i in range(0, len(check1)):
    if im(check1[0]) != 0:
        continue
    else:
        if (check1[i] >= 0 and check1[i] <= 3):
            soln.append(check1[i])
        else:
            continue

if len(soln) > 0:
    for k in range(0, len(soln)):
        maxmin1 = diff2.subs(x, soln[k])
        if maxmin1 < 0:
            max = soln[k]
            maxval = expr1.subs(x, max)
        elif maxmin1 > 0:
            min = soln[k]
            minval = expr1.subs(x, min)
    print(f"Maxima is {maxval} and Minima is {minval}")
else:
    print('No maxima or minima is found')
