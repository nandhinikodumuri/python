# 1. Single-line Comment
print("Hello")
# 2. Multi-line Comment
"""
This is
multi-line text
"""
print("Python")
# 3. Variable
name = "Nandhini"
age = 22
print(name, age)
# 4. Swap Using Temporary Variable
a = 10
b = 20

temp = a
a = b
b = temp

print(a, b)
# 5. Swap Without Third Variable
a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a, b)
# 6. String
name = "Python"
print(name[0])
# 7. Integer
age = 22
print(type(age))
# 8. Float
price = 99.5
print(type(price))
# 9. Complex
z = 4 + 5j
print(z.real)
print(z.imag)
# 10. List
items = ["Pen", "Book", "Bag"]
print(items[0])
# 11. Tuple
colors = ("Red", "Blue")
print(colors[1])
# 12. Single-Element Tuple
x = ("Python",)
print(type(x))
# 13. Range
numbers = range(5)
print(list(numbers))
# 14. Check Data Type
x = 100
print(type(x))