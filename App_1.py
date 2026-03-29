import streamlit as st
import pandas as pd
import io
# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="PragyanAI Student Program Pricing Analytics Dashboard", layout="wide")

# -----------------------------
# Title
# -----------------------------
st.title("PragyanAI Student Program Pricing & Scholarship Analytics Dashboard")

st.write("Analyze pricing, discounts, and student conversion behavior.")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("student_PRICING_SCHOLARSHIP_Analysis_Project_12.csv")
    return df

df = load_data()

# -----------------------------
# Show Data
# -----------------------------
st.subheader("Dataset Preview")
st.dataframe(df.head())
# st.write(df.info()) df.info - Not Return Anything

buffer = io.StringIO()
df.info(buf=buffer)

st.text(buffer.getvalue())
# -----------------------------
# KPIs
# -----------------------------
st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

total_students = len(df)
conversion_rate = df["Converted"].mean() * 100
avg_price = df["Final_Price"].mean()
total_revenue = df["Revenue"].sum()

col1.metric("Total Students", total_students)
col2.metric("Conversion Rate (%)", f"{conversion_rate:.2f}")
col3.metric("Avg Final Price", f"₹{avg_price:,.0f}")
col4.metric("Total Revenue", f"₹{total_revenue:,.0f}")

# -----------------------------
# Basic Analysis
# -----------------------------
st.subheader(" Descriptive Statistics")
st.write(df.describe())

# -----------------------------
# Business Insights
# -----------------------------
st.subheader("💡 Key Insights")

# Top revenue student
top_student = df.loc[df["Revenue"].idxmax()]
st.write(f"🏆 Highest Revenue Student ID: {top_student['Student_ID']} → ₹{top_student['Revenue']:,.0f}")

# Conversion by Program
conversion_by_program = df.groupby("Program_Type")["Converted"].mean() * 100
st.write("📊 Conversion Rate by Program:")
st.write(conversion_by_program)

# Avg Discount
avg_discount = df["Discount_%"].mean()
st.write(f"🎁 Average Discount Given: {avg_discount:.2f}%")

# -----------------------------
# Simple Charts
# -----------------------------
st.subheader("📊 Visualizations")

# Conversion count
st.write("### Conversion Distribution")
st.bar_chart(df["Converted"].value_counts())

# Revenue by Program
st.write("### Revenue by Program")
revenue_by_program = df.groupby("Program_Type")["Revenue"].sum()
st.bar_chart(revenue_by_program)

# -----------------------------
# Raw Data Toggle
# -----------------------------
if st.checkbox("Show Full Data"):
    st.write(df)
