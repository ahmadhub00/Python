num1= 2
num2= 3
a=b=c = 10
num3,num4 = 30,40

result = num1 ** num2 # for exponnentiation

result1 = num3 // num4 # for floor division
# print(result)
# print(result1)

# Operators precedence
# - ()
# - **
# - / * // %
# - + -

result3 = num1 == num2 # for comparison
result4 = num1 != num2
result5 = num1 > num2
#answer will be in boolean true or false
print(result3)
print(type(result3))

result6 = result3 or result4 # for logical or
# T T  True
# T F  True
# F T  True
# F F  False

result7 = not(result3 and result4) # for logical and
# T T  True
# T F  False    
# F T  False
# F F  False

# Assignment operators

a= 10
a += 5 # a = a + 5
a -= 10 # a = a - 10
a *= 2 # a = a * 2
a **= 3 # a = a ** 3
a /= 2 # a = a / 2
a //= 3 # a = a // 3
print(a)

# Membership operators
userName = "Ahmad Taimur"
value = 'A' in userName
value = 'a' not in userName
print(value) # True

#  identity operators
x = 5
y = 5
z = 10
print(x is y) # True
print(x is not z) # True