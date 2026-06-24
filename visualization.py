import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("students.csv")

# -------------------------------
# Bar Chart - Math Marks
# -------------------------------
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Math"])
plt.title("Math Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Math Marks")
plt.show()

# -------------------------------
# Line Chart - Science Marks
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(df["Name"], df["Science"], marker="o")
plt.title("Science Marks")
plt.xlabel("Student Name")
plt.ylabel("Science Marks")
plt.show()

# -------------------------------
# Pie Chart - Department Distribution
# -------------------------------
department = df["Department"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(department, labels=department.index, autopct="%1.1f%%")
plt.title("Department Distribution")
plt.show()

# -------------------------------
# Histogram - Attendance
# -------------------------------
plt.figure(figsize=(8,5))
plt.hist(df["Attendance"], bins=5)
plt.title("Attendance Distribution")
plt.xlabel("Attendance")
plt.ylabel("Number of Students")
plt.show()

print("Visualization Project Completed Successfully!")