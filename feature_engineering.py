import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("ai_student_impact_dataset.csv")

st.title("Feature Engineering - AI Student Dataset")

# ------------------------
# 1. Encoding Major_Category
# ------------------------
df_encoded = pd.get_dummies(df, columns=["Major_Category"], prefix="Major")
st.subheader("Encoded Major_Category")
st.write(df_encoded.head())

# ------------------------
# 2. Feature Creation - AI Usage Intensity
# ------------------------
df_encoded["AI_Usage_Intensity"] = df_encoded["Weekly_GenAI_Hours"] / (df_encoded["Traditional_Study_Hours"] + 1)
st.subheader("AI Usage Intensity Feature")
st.write(df_encoded[["Weekly_GenAI_Hours", "Traditional_Study_Hours", "AI_Usage_Intensity"]].head())