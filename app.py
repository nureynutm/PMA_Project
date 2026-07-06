import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ai_student_impact_dataset.csv")

st.title("AI Student Impact Dashboard")

# -------------------------
# FILTER (INTERACTIVE 1)
# -------------------------
major = st.selectbox("Select Major", df["Major_Category"].unique())
df_filtered = df[df["Major_Category"] == major]

hours = st.slider("Minimum AI Hours", 0, 20, 5)
df_filtered = df_filtered[df_filtered["Weekly_GenAI_Hours"] >= hours]

st.write(df_filtered)

# -------------------------
# VISUAL 1
# -------------------------
st.subheader("GPA Distribution")
fig, ax = plt.subplots()
ax.hist(df_filtered["Post_Semester_GPA"])
st.pyplot(fig)

# -------------------------
# VISUAL 2
# -------------------------
st.subheader("AI Usage vs GPA")
fig2, ax2 = plt.subplots()
ax2.scatter(df_filtered["Weekly_GenAI_Hours"], df_filtered["Post_Semester_GPA"])
st.pyplot(fig2)

# -------------------------
# VISUAL 3
# -------------------------
st.subheader("Average GPA by Major")
st.bar_chart(df.groupby("Major_Category")["Post_Semester_GPA"].mean())

# -------------------------
# SIMPLE PREDICTION OUTPUT
# -------------------------
st.subheader("Simple Insight")
st.write("Higher AI usage does not always mean higher GPA based on dataset trends.")
