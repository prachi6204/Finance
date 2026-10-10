# STUDENT PERFORMANCE DATA ANALYSIS
# Mini Project

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 2. Create Dataset
data = {
    "Name": ["Aman", "Riya", "Karan", "Simran", "Arjun",
             "Neha", "Rahul", "Priya", "Vivek", "Anjali"],

    "Gender": ["Male", "Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female"],

    "Attendance": [85, 92, 78, 95, 88, 70, 82, 90, 75, 96],

    "Maths": [78, 90, 65, 92, 80, 60, 72, 88, 68, 95],

    "Python": [82, 94, 70, 89, 85, 62, 75, 91, 72, 96],

    "DBMS": [75, 88, 68, 94, 82, 65, 70, 90, 74, 93]
}

df = pd.DataFrame(data)


# 3. Display Dataset
print("STUDENT DATA")
print(df)


# 4. Basic Information
print("\nFIRST FIVE RECORDS")
print(df.head())

print("\nDATA INFORMATION")
print(df.info())

print("\nSTATISTICAL SUMMARY")
print(df.describe())


# 5. Data Cleaning
print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDATA TYPES")
print(df.dtypes)


# 6. Calculate Average Marks
df["Average"] = df[["Maths", "Python", "DBMS"]].mean(axis=1)

print("\nAVERAGE MARKS")
print(df[["Name", "Average"]])


# 7. NumPy Analysis
print("\nNUMPY ANALYSIS")

print("Mean:", np.mean(df["Average"]))
print("Median:", np.median(df["Average"]))
print("Standard Deviation:", np.std(df["Average"]))


# 8. Subject-wise Average
subjects = ["Maths", "Python", "DBMS"]

print("\nSUBJECT-WISE AVERAGE")
print(df[subjects].mean())


# 9. Highest Performing Student
highest = df.loc[df["Average"].idxmax()]

print("\nHIGHEST PERFORMING STUDENT")
print(highest)


# 10. Attendance and Marks Correlation
print("\nATTENDANCE VS AVERAGE CORRELATION")
print(df[["Attendance", "Average"]].corr())


# 11. Sort Students by Average Marks
print("\nSTUDENTS SORTED BY PERFORMANCE")
print(df.sort_values("Average", ascending=False))


# 12. Gender-wise Performance
print("\nGENDER-WISE PERFORMANCE")
print(df.groupby("Gender")["Average"].mean())


# ----------------------------------------
# VISUALIZATIONS
# ----------------------------------------

# 13. Bar Chart
plt.figure(figsize=(7, 5))

plt.bar(subjects, df[subjects].mean())

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()


# 14. Histogram
plt.figure(figsize=(7, 5))

plt.hist(df["Average"], bins=5)

plt.title("Distribution of Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")

plt.show()


# 15. Scatter Plot
plt.figure(figsize=(7, 5))

plt.scatter(df["Attendance"], df["Average"])

plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")

plt.show()


# 16. Gender-wise Bar Plot
plt.figure(figsize=(7, 5))

sns.barplot(x="Gender", y="Average", data=df)

plt.title("Gender-wise Average Performance")
plt.xlabel("Gender")
plt.ylabel("Average Marks")

plt.show()


# 17. Box Plot
plt.figure(figsize=(7, 5))

sns.boxplot(data=df[subjects])

plt.title("Subject-wise Marks Distribution")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()


# 18. Correlation Heatmap
plt.figure(figsize=(7, 5))

sns.heatmap(
    df[["Attendance", "Maths", "Python", "DBMS", "Average"]].corr(),
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()


# 19. Final Findings
print("\n========== FINDINGS ==========")

print("1. Students with higher attendance generally have better marks.")
print("2. Python has a strong overall performance.")
print("3. Some students perform consistently well in all subjects.")
print("4. Attendance and average marks show a positive relationship.")
print("5. Student performance varies across different subjects.")
print("6. The average marks help identify high and low performing students.")
print("7. Gender-wise average performance can also be compared.")
print("8. Correlation helps identify relationships between attendance and marks.")


# 20. Conclusion
print("\n========== CONCLUSION ==========")

print("""
The Student Performance Data Analysis project helps understand
students' academic performance using marks and attendance data.
Pandas and NumPy were used for data cleaning and analysis,
while Matplotlib and Seaborn were used for visualization.
The analysis shows that attendance can be associated with
academic performance and that students have different
performance levels across subjects.
""")
