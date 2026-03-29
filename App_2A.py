import streamlit as st
import pandas as pd

st.title("📊 Basic Charts Dashboard")

df = pd.read_csv("student_PRICING_SCHOLARSHIP_Analysis_Project_12.csv")

# -----------------------------
# Streamlit Column Grid Dashboard
# -----------------------------
st.subheader(" Interactive Column-Based Dashboard")

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

# -----------------------------
# Filters
# -----------------------------
st.sidebar.header(" Filters")

# Select Program
program = st.sidebar.selectbox(
    "Select Program",
    options=df["Program_Type"].unique()
)

# Slider for Marks / Price
price_range = st.sidebar.slider(
    "Select Final Price Range",
    int(df["Final_Price"].min()),
    int(df["Final_Price"].max()),
    (int(df["Final_Price"].min()), int(df["Final_Price"].max()))
)

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df[
    (df["Program_Type"] == program) &
    (df["Final_Price"].between(price_range[0], price_range[1]))
]

# -----------------------------
# Output
# -----------------------------
st.subheader(" Filtered Data")
st.dataframe(filtered_df)

st.write("Total Students:", len(filtered_df))
