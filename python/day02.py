# 1. Tokens Example
# Identifier
name = "Nandhini"

# Literal
age = 21

# Operator
result = age + 5

# Keyword
if result > 20:
    print(result)
# 2. Statements
x = 10
print(x)

if x > 5:
    print("x is greater than 5")
# 3. Identifiers
student_name = "Nandhini"
roll_no = 101

print(student_name)
print(roll_no)
# 4. Comments
# Single-line comment

"""
This is
a multi-line
comment
"""

print("Comments Example")
# 5. Variables
x = 100
name = "Python"
price = 99.99

print(x)
print(name)
print(price)
# 6. Multiple Assignment
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)
#  7. Same Value Assignment
x = y = z = 50

print(x)
print(y)
print(z)
# 8. Reassignment
x = 5
print(x)

x = 15
print(x)
# 9. Swapping Variables
a = 10
b = 20

print("Before:", a, b)

a, b = b, a

print("After:", a, b)
# 10. Delete Variable
x = 100

print(x)

del x

# Uncomment to see the error
# print(x)
# 11. Display All Python Keywords
import keyword

print(keyword.kwlist)