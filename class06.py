isGreater = 50 > 10
if isGreater:
    print("50 is greater than 10")

# if/else only works with boolean values

num1 = int(input("Enter a number: "))
if num1 % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# write a program to check if the number is positive, negative or zero
num2 = int(input("enter a number"))
if num2 > 0:
    print("Positive number")
elif num2 < 0:
    print("Negative number")
else:
    print("Zero")