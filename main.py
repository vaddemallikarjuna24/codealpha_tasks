import pandas as pd

# Read the dataset
df = pd.read_csv("students.csv")

# Display first 5 rows
print("========== FIRST 5 ROWS ==========")
print(df.head())

# Dataset information
print("\n========== DATASET INFO ==========")
df.info()

# Statistical summary
print("\n========== STATISTICS ==========")
print(df.describe())

# Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Average marks
print("\n========== AVERAGE MARKS ==========")
print("Math Average:", df["Math"].mean())
print("Science Average:", df["Science"].mean())
print("English Average:", df["English"].mean())

# Highest marks
print("\n========== HIGHEST MARKS ==========")
print("Math:", df["Math"].max())
print("Science:", df["Science"].max())
print("English:", df["English"].max())

# Lowest marks
print("\n========== LOWEST MARKS ==========")
print("Math:", df["Math"].min())
print("Science:", df["Science"].min())
print("English:", df["English"].min())

# Top student in Math
print("\n========== TOPPER IN MATH ==========")
topper = df.loc[df["Math"].idxmax()]
print(topper)

# Save cleaned dataset
df.to_csv("output.csv", index=False)

print("\nProject Completed Successfully!")