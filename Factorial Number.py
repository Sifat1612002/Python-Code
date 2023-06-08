import math
num = int(input("Enter the number :"))
n = math.factorial(num)
print("The factorial of", num, "is : " + str(n))


def fact(num):
    f = 1
    for i in range(num, 0, -1):
        f = f*i
    print("The factorial of", num, "is : ", f)


x = int(input("Enter another number :"))
fact(x)
