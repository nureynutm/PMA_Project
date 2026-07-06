import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("ai_student_impact_dataset.csv")

st.title("Data Quality Checks - AI Student Dataset")

# -------------------------
# 1. Missing Values Check
# -------------------------
st.subheader("Missing Values Check")

missing_values = df.isnull().sum()
st.write("Missing values in each column:")
st.write(missing_values)

# -------------------------
# 2. Duplicate Records Check
# -------------------------
st.subheader("Duplicate Records Check")

duplicate_rows = df[df.duplicated()]
st.write("Number of duplicate rows:", duplicate_rows.shape[0])
st.write("Duplicate rows (if any):")
st.write(duplicate_rows)

# -------------------------
# Summary Table
# -------------------------
st.subheader("Summary of Data Quality Issues")

summary = pd.DataFrame({
    "Issue Type": ["Missing Values", "Duplicate Records"],
    "Identified By": ["df.isnull().sum()", "df.duplicated()"],
    "Observed Outcome": [missing_values.to_dict(), f"{duplicate_rows.shape[0]} rows duplicated"],
    "Potential Impact": [
        "Missing values could bias models and dashboards",
        "Duplicates can skew statistics and predictions"
    ]
})

st.table(summary)