def sum(a,b):
    c = a + b
    return c
print(globals()) # shows all the global variables including functions
print(locals()) # shows all the local variables including functions

result = sum(3,4)
print(result)

output = sum(sum(10,result),6) # 23
print(output)
# function can have unlimited parameters but only one return statement

input1 = input("Enter first number: ")
# to get integer input from user
input2 = input("Enter second number: ")
result = sum(input1,input2)
print(type(input1))
print(result)