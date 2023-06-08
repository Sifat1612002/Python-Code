def rev(num):                                 # reversing a number
    #num = int(input("Enter a number: "))
    x = num
    sum = 0
    n = len(str(num))
    while (num > 0):
        rem = num % 10
        sum += rem ** n
        num = num//10

    if (x == sum):
        print(x, " is Armstrong Number")
   # else:
       # print(x, " is Not an armstrong number")


i = 0
while (i < 100000000):
    i += 1
    rev(i)
