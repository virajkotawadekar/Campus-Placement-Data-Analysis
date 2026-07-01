import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==================================
# 1. Import & print Dataset 
# ==================================

df = pd.read_csv("Job_Placement_Data.csv")
print(df)

# ==================================
# 2. Basic Data
# ==================================

print("Number of Students :", len(df))

print("\nTotal Columns :", len(df.columns))

print("\nColumn Names :")
print(df.columns)

print("\nMissing Values :")
print(df.isnull().sum())

# ==================================
# 3. Academic Analysis
# ==================================

print("\nAverage SSC Percentage :",
      round(df['ssc_percentage'].mean(),2))

print("Average HSC Percentage :",
      round(df['hsc_percentage'].mean(),2))

print("Average Degree Percentage :",
      round(df['degree_percentage'].mean(),2))

print("Average MBA Percentage :",
      round(df['mba_percent'].mean(),2))

print("Maximum Employability Test Score :",
      df['emp_test_percentage'].max())

# ==================================
# 4. Placement Analysis
# ==================================

placed = df[df['status']=="Placed"]
not_placed = df[df['status']=="Not Placed"]

print("\nTotal Placed Students :",
      len(placed))

print("Total Non-Placed Students :",
      len(not_placed))

placement_percentage = (len(placed)/len(df))*100

print("Placement Percentage :",
      round(placement_percentage,2),"%")

# Bar Graph

plt.figure(figsize=(6,4))

sns.countplot(
    x='status',
    data=df
)

plt.title("Placed vs Not Placed Students")
plt.show()

# ==================================
# 5. Specialisation Analysis
# ==================================

print("\nStudents in Each Specialisation")

print(df['specialisation'].value_counts())

print("\nSpecialisation vs Placement")

comparison = pd.crosstab(
    df['specialisation'],
    df['status']
)

print(comparison)

comparison.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Specialisation vs Placement")
plt.xlabel("Specialisation")
plt.ylabel("Student Count")
plt.show()

# ==================================
# 6. Work Experience Analysis
# ==================================

print("\nWork Experience Count")

print(df['work_experience'].value_counts())

print("\nPlacement Based on Work Experience")

print(pd.crosstab(
    df['work_experience'],
    df['status']
))

# ==================================
# 7. Employability Test Analysis
# ==================================

print("\nAverage Employability Test Score :",
      round(df['emp_test_percentage'].mean(),2))

plt.figure(figsize=(6,4))

sns.histplot(
    df['emp_test_percentage'],
    bins=10
)

plt.title("Employability Test Distribution")
plt.show()

# ==================================
# 8. Heatmap
# ==================================

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(8,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()

# ==================================
# 9. Placement Indicators Table
# ==================================

print("\nPLACEMENT INDICATORS")

print("\nSSC Percentage")

print(df.groupby('status')
      ['ssc_percentage']
      .mean())

print("\nHSC Percentage")

print(df.groupby('status')
      ['hsc_percentage']
      .mean())

print("\nDegree Percentage")

print(df.groupby('status')
      ['degree_percentage']
      .mean())

print("\nMBA Percentage")

print(df.groupby('status')
      ['mba_percent']
      .mean())

print("\nEmployability Test Percentage")

print(df.groupby('status')
      ['emp_test_percentage']
      .mean())

# ==================================
# 10. Summary
# ==================================

print("\n========== SUMMARY ==========")

print("Total Students :", len(df))
print("Placed Students :", len(placed))
print("Non-Placed Students :", len(not_placed))
print("Placement Percentage :",
      round(placement_percentage,2),"%")

print("Average SSC Percentage :",
      round(df['ssc_percentage'].mean(),2))

print("Average HSC Percentage :",
      round(df['hsc_percentage'].mean(),2))

print("Average Degree Percentage :",
      round(df['degree_percentage'].mean(),2))

print("Average MBA Percentage :",
      round(df['mba_percent'].mean(),2))

print("\nProject Completed Successfully\n \n")

