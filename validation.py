import pandas as pd

# Load dataset
df = pd.read_csv("ai_student_impact_dataset.csv")

print("=== AUTOMATED DATA VALIDATION REPORT ===")

# 1. Missing Values Check
print("\nMissing Values Check:")
print(df.isnull().sum())

# 2. Duplicate Rows Check
print("\nDuplicate Rows Check:")
print("Total duplicates:", df.duplicated().sum())

# 3. Data Type Check
print("\nData Types Check:")
print(df.dtypes)

# 4. Value Range Check (GPA example)
print("\nValue Range Check (GPA 0–4):")
invalid_gpa = df[(df["Post_Semester_GPA"] < 0) | (df["Post_Semester_GPA"] > 4)]
print(invalid_gpa)