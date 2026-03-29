import streamlit as st
import pandas as pd

st.title("📂 File Upload Data Analyzer")

# Upload File
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader(" Data Preview")
    st.dataframe(df.head())

    st.subheader(" Data Info")
    st.write("Shape:", df.shape)
    st.write("Columns:", df.columns.tolist())

    st.subheader("📈 Statistics")
    st.write(df.describe())

else:
    st.info("Please upload a CSV file")

st.subheader(" Basic Charts Dashboard")

df = pd.read_csv("student_PRICING_SCHOLARSHIP_Analysis_Project_12.csv")

# -----------------------------
# Charts
# -----------------------------
st.subheader(" Revenue Trend")
st.line_chart(df["Revenue"])

st.subheader(" Revenue by Program")
st.bar_chart(df.groupby("Program_Type")["Revenue"].sum())

st.subheader(" Discount Trend")
st.line_chart(df["Discount_%"])
