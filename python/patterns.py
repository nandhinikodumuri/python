#Square pattern
row = 5
for i in range (1, 6):
    for j in range(1,6):
        print("*", end=" ")
    print()

#right traingle pattern
row = 5
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

#triangle pattern
row = 5
for i in range(1,6):
    for K in range(row-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

#left triangle pattern
row = 4
for i in range(1,row+1):
    for K in range(row-i):
          print(" ", end="")     #// if we  keep space it becomes  left triangle
    for j in range(i):
          print("*", end=" ")
    print()

#reverse triangle pattern // reverse left triangle pattern
row = 5
for i in range(row,0,-1):
    for K in range(row-i):
          print(" ", end="")
    for j in range(i):
          print("*", end=" ")
    print()

#diamond pattern
row =5 
for i in range(1,row+1):
    for k in range(row-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

# for i in range(row,0,-1):
    for k in range(row-i):
        print(" ", end = "")
    for j in range(i):
        print("*", end = " ")
    print()

#reverse diamond pattern
row = 5
for i in range(row,0,-1):
    for k in range(row-i):
        print(" ",end="")
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(1,row+1):
    for k in range(row-i):
        print(" ",end="")
    for j in range(i):
        print("*", end=" ")
    print()

#number pattern of right triangle
row = 5
for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()

row = 5
for i in range(1,6):
    for j in range(i):
        print(j+1, end=" ")
    print()

row = 5
c = 1
for i in range(1,6):
    for k in range(row-i):
        print(" ", end="")
    for j in range(i):
        print(c, end=" ")
        c = c + 1
    print()
number = 20
print a + b 
print a - b