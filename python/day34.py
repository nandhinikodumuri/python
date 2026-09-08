# #Matpoltslib line polt
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)
plt.title("My First Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.plot(x, y, marker="s")
plt.show()

#Bar chart
# import matplotlib.pyplot as plt

x = ["A","B", "C", "D", "E"]
Y = [10,20,30,40,50]
plt.bar(x,Y, color = "pink", linestyle="-", linewidth = 2)
plt.title("Bar chart")
plt.xlabel("x -axis")
plt.ylabel("y -axis")
plt.grid(True)
plt.show()

# 3. HISTOGRAM
import matplotlib.pyplot as plt

marks = [10, 20, 30, 40, 50, 60, 70, 85, 80, 94, 90, 100, 95, 88, 75, 65, 55, 45, 35, 25, 15]

plt.hist(marks, bins = 9, color = "pink", edgecolor = "black")
plt.title("Exam Score Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.grid()
plt.show()

# 4. Scatter Plot
import matplotlib.pyplot as plt
hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
marks = [10,20,30,40,50,60,70,80,90,100,15,25,35,45,55,65,75,85,95,88]
plt.scatter(hours, marks, s=100, marker = "o")
plt.title("study hours vs marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.legend(["Hours vs Marks"])
plt.grid(True)
plt.show()

#5 pie chart
import matplotlib.pyplot as plt
brands = ["Apple","Samsung","OnePlus","Others"]
share = [35,30,20,15]
plt.pie(share,
labels=brands,
autopct="%1.1f%%",
startangle=90,
shadow=True)
plt.title("Mobile Market Share")
plt.show()

#6. box plot
import matplotlib.pyplot as plt
salary = [25000,27000,30000,32000,35000,
36000,38000,40000,42000,70000]

plt.boxplot(salary,
showmeans=True,
patch_artist=True)
plt.title("Salary Distribution")
plt.show()

# 7 area plot
import matplotlib.pyplot as plt
days = [1,2,3,4,5,6,7]
visitors = [200,250,230,280,300,320,350]
plt.fill_between(days, visitors,
color="skyblue",
alpha=0.5)
plt.plot(days, visitors,
color="blue",
linewidth=2)
plt.title("Website Visitors")
plt.xlabel("Days")
plt.ylabel("Visitors")
plt.show()

#8.heatmap
import seaborn as sns
import matplotlib.pyplot as plt
data = [
[80,75,90],
[60,70,85],
[95,88,92]
]
sns.heatmap(data,
annot=True,
cmap="YlOrRd",
linewidths=1)
plt.title("Student Marks")
plt.show()

# 9. Subplots
import matplotlib.pyplot as plt
months = ["Jan","Feb","Mar","Apr"]
sales = [20,25,30,35]
profit = [5,7,8,10]
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(months, sales, marker="o")
plt.title("Sales")
plt.subplot(1,2,2)
plt.bar(months, profit)
plt.title("Profit")
plt.tight_layout()
plt.show()