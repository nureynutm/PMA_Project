import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("ai_student_impact_dataset.csv")

st.title("EDA Dashboard - AI Student Dataset")

# Dataset preview
st.subheader("Dataset Preview")
st.write(df.head())

# -----------------------
# Histogram (Distribution)
# -----------------------
st.subheader("GPA Distribution")

fig, ax = plt.subplots()
sns.histplot(df["Post_Semester_GPA"], bins=20, kde=True, ax=ax)
st.pyplot(fig)

st.write("Most students are between 2.5 and 3.5 GPA.")

# -----------------------
# Scatter (Relationship)
# -----------------------
st.subheader("AI Usage vs GPA")

fig, ax = plt.subplots()
sns.scatterplot(data=df,
                x="Weekly_GenAI_Hours",
                y="Post_Semester_GPA",
                ax=ax)
st.pyplot(fig)

st.write("Weak relationship between AI usage and GPA.")

# -----------------------
# Bar Chart (Categorical)
# -----------------------
st.subheader("Burnout Level")

fig, ax = plt.subplots()
sns.countplot(data=df, x="Burnout_Risk_Level", ax=ax)
st.pyplot(fig)

st.write("Most students have medium burnout level.")