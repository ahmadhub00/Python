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
    
# Write a program that takes the user input number
# and verify its even if its even check number is
# greater than 50 if so print the number

num3 = int (input("Enter a number: "))
isEven = num3 % 2 == 0
if isEven:
        print("Even number")
        if num3 > 50:
            print("Number is greater than 50:", num3)
