# # 1 Input three numbers and print the greatest among them.
a = 10
b = 200
c = 30
if a > b and a > c:
    print("Greater number is :",a)
elif b > a and b > c:
    print("Greater number is :",b)
else:
    print("Greater number is :",c)

# #2 three digit number
num = 88
if num >= 100 and num <= 999:
    print("Three digit number")
else:
    print("Not a three digit number")

# #3 temperature check
temp = 16
if temp > 30:
    print("it is hot")
elif temp >=15 and temp <= 30:
    print("it is Pleasant")
else:
    print("it is cold")

# #4 +ve,-ve,zero
num = -1
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# #5 marks check
marks = 36
if marks >= 90:
    print("Grade A")
elif marks >= 80 :
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

# #6 polygon check
sides = 0
if sides == 3:
    print("Triangle")
elif sides == 4:
    print("Quadrilateral")
elif sides == 5:
    print("Pentagon")
else:
    print("Unknown shape")

# #7 bus fare
age = 90
if age < 5:
    print("free")
elif age >= 5 and age <= 18:
    print("Half ticket")
else:
    print("Full ticket")

# 8 Student Grade Calculator
averagemarks = 100
if averagemarks  > 90:
    print("Excellent")
elif averagemarks  >= 70 and averagemarks  <= 90:
    print("Good")
else:
    print("Needs Improvement")


 

