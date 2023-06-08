"""for j in range(1, 6):
    print()
    for i in range(1, 6):
        print("*", end='')

num = int(input("\nEnter a number "))
for row in range(1, num+1):
    print()
    for col in range(1, row+1):
        print("*", end='')

num = int(input("\nEnter a number "))
for row in range(num, 0, -1):
    print()
    for col in range(1, row+1):
        print("*", end='')

num = int(input("\nEnter a number "))
for row in range(num, 0, -1):
    print()
    for col in range(1, row+1):
        print("*", end=' ')"""

num = int(input("\nEnter a number "))
for row in range(1, num+1):
    print()
    for col in range(1, num-row+1):
        print(end=" ")
    for col in range(1, row+1):
        print("*", end=' ')

num = int(input("\nEnter a number "))
for row in range(num, 0, -1):
    print()
    for col in range(1, num-row+1):
        print(end=" ")
    for col in range(1, row+1):
        print("*", end=' ')
