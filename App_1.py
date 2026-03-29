import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns
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
st.write("Basic Info about Data")
buffer = io.StringIO()
df.info(buf=buffer)

st.text(buffer.getvalue())
# -----------------------------
# KPIs
# -----------------------------
st.subheader(" Key Metrics")

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
st.write(f" Highest Revenue Student ID: {top_student['Student_ID']} → ₹{top_student['Revenue']:,.0f}")

# Conversion by Program
conversion_by_program = df.groupby("Program_Type")["Converted"].mean() * 100
st.write(" Conversion Rate by Program:")
st.write(conversion_by_program)

# Avg Discount
avg_discount = df["Discount_%"].mean()
st.write(f" Average Discount Given: {avg_discount:.2f}%")

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

# -----------------------------
# Advanced Charts (Matplotlib + Seaborn)
# -----------------------------
st.subheader(" Advanced Visualizations (Matplotlib & Seaborn)")

# =============================
# 🔹 MATPLOTLIB CHARTS
# =============================
st.write("### Matplotlib Charts")

# 1. Histogram - Final Price Distribution
fig1, ax1 = plt.subplots()
ax1.hist(df["Final_Price"], bins=20)
ax1.set_title("Distribution of Final Price")
ax1.set_xlabel("Final Price")
ax1.set_ylabel("Frequency")
st.pyplot(fig1)

# 2. Line Chart - Revenue Trend (if index acts like time/order)
fig2, ax2 = plt.subplots()
ax2.plot(df["Revenue"])
ax2.set_title("Revenue Trend")
ax2.set_xlabel("Index")
ax2.set_ylabel("Revenue")
plt.tight_layout()
st.pyplot(fig2)

# =============================
# 🔹 SEABORN CHARTS
# =============================
st.write("### Seaborn Charts")

# 3. Count Plot - Conversion
fig3, ax3 = plt.subplots()
sns.countplot(x="Converted", data=df, ax=ax3)
ax3.set_title("Conversion Count")
st.pyplot(fig3)

# 4. Box Plot - Final Price by Program
fig4, ax4 = plt.subplots()
sns.boxplot(x="Program_Type", y="Final_Price", data=df, ax=ax4)
ax4.set_title("Final Price Distribution by Program")
st.pyplot(fig4)

# 5. Heatmap - Correlation
fig5, ax5 = plt.subplots()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax5)
ax5.set_title("Correlation Heatmap")
plt.tight_layout()
st.pyplot(fig5)

# -----------------------------
# Grid Subplots Dashboard
# -----------------------------
st.subheader("Multi-Chart Dashboard (Subplots Grid)")

import matplotlib.pyplot as plt
import seaborn as sns

# Create figure with 2 rows × 2 columns
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# =============================
# 🔹 Plot 1: Histogram
# =============================
axes[0, 0].hist(df["Final_Price"], bins=20)
axes[0, 0].set_title("Final Price Distribution")

# =============================
# 🔹 Plot 2: Count Plot
# =============================
sns.countplot(x="Converted", data=df, ax=axes[0, 1])
axes[0, 1].set_title("Conversion Count")

# =============================
# 🔹 Plot 3: Box Plot
# =============================
sns.boxplot(x="Program_Type", y="Final_Price", data=df, ax=axes[1, 0])
axes[1, 0].set_title("Price by Program")

# =============================
# 🔹 Plot 4: Revenue Trend
# =============================
axes[1, 1].plot(df["Revenue"])
axes[1, 1].set_title("Revenue Trend")

# Adjust layout
plt.tight_layout()

# Display in Streamlit
st.pyplot(fig)

# -----------------------------
# Advanced Dynamic Subplots Grid
# -----------------------------
st.subheader("📊 Advanced Multi-Chart Dynamic Dashboard")

import matplotlib.pyplot as plt
import seaborn as sns
import math

# =============================
# 🔹 Define number of plots dynamically
# =============================
plots = [
    "hist_price",
    "revenue_trend",
    "conversion_count",
    "box_plot",
    "discount_distribution",
    "correlation_heatmap"
]

num_plots = len(plots)
cols = 2  # number of columns you want
rows = math.ceil(num_plots / cols)

# =============================
# 🔹 Create subplot grid
# =============================
fig, axes = plt.subplots(rows, cols, figsize=(16, 5 * rows))
axes = axes.flatten()  # flatten for easy indexing

# =============================
# 🔹 Loop through plots
# =============================
for i, plot in enumerate(plots):

    if plot == "hist_price":
        axes[i].hist(df["Final_Price"], bins=20)
        axes[i].set_title("Final Price Distribution")

    elif plot == "revenue_trend":
        axes[i].plot(df["Revenue"])
        axes[i].set_title("Revenue Trend")

    elif plot == "conversion_count":
        sns.countplot(x="Converted", data=df, ax=axes[i])
        axes[i].set_title("Conversion Count")

    elif plot == "box_plot":
        sns.boxplot(x="Program_Type", y="Final_Price", data=df, ax=axes[i])
        axes[i].set_title("Price by Program")

    elif plot == "discount_distribution":
        axes[i].hist(df["Discount_%"], bins=20)
        axes[i].set_title("Discount Distribution")

    elif plot == "correlation_heatmap":
        corr = df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=axes[i])
        axes[i].set_title("Correlation Heatmap")

# =============================
# 🔹 Hide empty subplots
# =============================
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

# =============================
# 🔹 Final Layout Fix
# =============================
plt.tight_layout()

# =============================
# 🔹 Show in Streamlit
# =============================
st.pyplot(fig)

# -----------------------------
# Streamlit Column Grid Dashboard
# -----------------------------
st.subheader("📊 Interactive Column-Based Dashboard")

# =============================
# 🔹 ROW 1 (2 columns)
# =============================
col1, col2 = st.columns(2)

with col1:
    st.write("### Revenue Distribution")
    st.bar_chart(df["Revenue"])

with col2:
    st.write("### Final Price Trend")
    st.line_chart(df["Final_Price"])

# =============================
# 🔹 ROW 2 (2 columns)
# =============================
col3, col4 = st.columns(2)

with col3:
    st.write("### Conversion Count")
    st.bar_chart(df["Converted"].value_counts())

with col4:
    st.write("### Discount Distribution")
    st.line_chart(df["Discount_%"])

# =============================
# 🔹 ROW 3 (3 columns)
# =============================
col5, col6, col7 = st.columns(3)

with col5:
    st.write("### Revenue by Program")
    st.bar_chart(df.groupby("Program_Type")["Revenue"].sum())

with col6:
    st.write("### Avg Final Price by Program")
    st.bar_chart(df.groupby("Program_Type")["Final_Price"].mean())

with col7:
    st.write("### Conversion Rate by Program")
    conv = df.groupby("Program_Type")["Converted"].mean() * 100
    st.bar_chart(conv)

# =============================
# 🔹 ROW 4 (FULL WIDTH)
# =============================
st.write("### Full Dataset Trend View")
st.line_chart(df[["Final_Price", "Revenue"]])
