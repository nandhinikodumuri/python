#Conditional statements

#if
a = 10
if a > 5:
    print("Hello")

#if - else
num = 16
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#elif
a=19
b=20
c=50
if a>b and a>c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
else:
    print("c is largest")

#Nested if
age =20
weight = 53
if age >=18:
    if weight >= 50:
        print("eligible")
    else:
        print(" not eligible")
else:
    print("not eligible")

#Loops

#for loop
l=[1,2,3,4,5]
for i in l:
    print(i)

#Jumping statements
for i in range(1,6,1):
    if i == 4:
        break
    print(i)

#continue

for i in range(1,6,1):
    if i == 4:
        continue
    print(i)

num1 = 100
num2 = 50

if num1 > num2:
    print("Greater number is:", num1)
else:
    print("Greater number is:", num2)

num = int(input("Entre a number:"))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


num = 101
if num % 3 == 0 and num % 5 ==  0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")

char = "aeiou"
if char in "aeiouAEIOU":
    print("Character is vowel")
else:
    print("Character is consonant")


num = 5
if num == 0:
    print("number is zero")
else:
    print("number is non zero")


a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
if a > b and a > c:
    print("Greater number is :",a)
elif b > a and b > c:
    print("Greater number is :",b)
else:
    print("Greater number is :",c)