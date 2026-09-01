# 1. Print numbers from 1 to 5
for i in range(1, 6):
    print(i)
# 2. Sum of numbers from 1 to 10
total = 0

for i in range(1, 11):
    total += i

print(total)
# 3. Print even numbers from 1 to 10
for i in range(2, 11, 2):
    print(i)
# 4. Factorial of a number
n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)
# 5. Print elements of a list
numbers = [10, 20, 30, 40, 50]

for i in numbers:
    print(i)
# 6. Find maximum value in a list
numbers = [10, 45, 23, 67, 12]
maximum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i

print(maximum)
# 7. Print characters in a string
name = "Python"

for i in name:
    print(i)
# 8. Count vowels in a string
text = input("Enter string: ")
count = 0

for i in text:
    if i in "aeiouAEIOU":
        count += 1

print(count)
# 9. Print dictionary key-value pairs
student = {"name": "Nandhini", "age": 21, "course": "Python"}

for key, value in student.items():
    print(key, value)
# 10. Pattern using nested for loops
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
# 11. Sum of even numbers from 1 to 100
total = 0

for i in range(2, 101, 2):
    total += i

print(total)
# 12. First 10 Fibonacci numbers
a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b