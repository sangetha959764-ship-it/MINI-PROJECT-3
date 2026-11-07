import pandas as pd
import streamlit as st
df = pd.read_csv(r'C:\Users\Niveditha.S\OneDrive\Desktop\HR_predection_project-3\placement_cleaned_data.csv')
#print(df.head())
#print(df.columns.tolist())
#print(df.shape)
#print(df.isnull().sum())

# 1. Total Candidates
total_candidates = len(df)
#print(total_candidates)

# 2. Placement Rate
placed_count = (df["status"] == 1).sum()
placement_rate = (placed_count / total_candidates) * 100
print("Placed Candidates:", placed_count)
print("Placement Rate:", round(placement_rate, 2), "%")

#print(df["status"].unique())
#print(df["status"].value_counts())
#print(df["status"].dtype)
#df["status_label"] = df["status"].map({ 0: "Not Placed",1: "Placed"})

# 3.Job Acceptance Rate (%)
print(df.columns.tolist())

#4.Average Interview Score
df['average_interview_score'] = df[['technical_score', 'aptitude_score', 'communication_score']].mean(axis=1)
avg_interview_score = df['average_interview_score'].mean()
print(avg_interview_score)

#5. Average Skills Match %
avg_skills_match = df['skills_match_percentage'].mean()
print(avg_skills_match)

#6.3. Offer Dropout Rate

#7. High-Risk Candidate Percentage
#print(df['placement_probability_score'].describe())
high_risk = df[df['placement_probability_score'] < 60]

high_risk_percentage = (len(high_risk) / len(df)) * 100
print(high_risk_percentage)


st.title(" HR JOB PLACEMENT PREDICTION")


st.subheader("HR Placement Prediction")


st.header("📊 HR Dashboard KPI")

col1, col2, col3 = st.columns(3)

col1.metric("1. Total Candidates", f"{total_candidates:,}")
col2.metric("2. Placed Candidates", f"{placed_count:,}")
col3.metric("3. Placement Rate", f"{placement_rate:.2f}%")

col4, col5, col6 = st.columns(3)

col4.metric("4. Average Interview Score", f"{avg_interview_score:.2f}")
col5.metric("5. Average Skills Match", f"{avg_skills_match:.2f}%")
col6.metric("6. High-Risk Candidates", f"{high_risk_percentage:.2f}%")
