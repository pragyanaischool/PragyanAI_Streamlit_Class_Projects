import streamlit as st
import pandas as pd
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="PragyanAI Dashboard", layout="wide")

st.title("🚀 PragyanAI Pricing Analytics Dashboard")

# -----------------------------
# SAFE DATA LOADING
# -----------------------------
uploaded_file = st.file_uploader("Upload CSV (Optional)", type=["csv"])

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    file_path = "student_PRICING_SCHOLARSHIP_Analysis_Project_12.csv"
    
    if os.path.exists(file_path):
        df = load_data(file_path)
    else:
        st.error("❌ Dataset not found. Please upload CSV.")
        st.stop()

st.success("✅ Data Loaded Successfully")

# -----------------------------
# COLUMN VALIDATION
# -----------------------------
required_cols = ["Program_Type", "Final_Price", "Converted", "Revenue", "Student_ID"]

missing = [col for col in required_cols if col not in df.columns]

if missing:
    st.error(f"❌ Missing columns: {missing}")
    st.stop()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")

program = st.sidebar.selectbox(
    "Select Program",
    options=df["Program_Type"].dropna().unique()
)

price_range = st.sidebar.slider(
    "Select Final Price Range",
    int(df["Final_Price"].min()),
    int(df["Final_Price"].max()),
    (
        int(df["Final_Price"].min()),
        int(df["Final_Price"].max())
    )
)

# -----------------------------
# APPLY FILTERS
# -----------------------------
filtered_df = df[
    (df["Program_Type"] == program) &
    (df["Final_Price"].between(price_range[0], price_range[1]))
]

# -----------------------------
# KPI METRICS (BASED ON FILTERED DATA)
# -----------------------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

total_students = len(filtered_df)
avg_price = filtered_df["Final_Price"].mean() if len(filtered_df) > 0 else 0
conversion_rate = filtered_df["Converted"].mean() * 100 if len(filtered_df) > 0 else 0

col1.metric("Total Students", total_students)
col2.metric("Avg Price", f"₹{avg_price:,.0f}")
col3.metric("Conversion Rate", f"{conversion_rate:.2f}%")

# -----------------------------
# FILTERED DATA TABLE
# -----------------------------
st.subheader("📊 Filtered Data")
st.dataframe(filtered_df)

# -----------------------------
# TOP PERFORMER (SAFE)
# -----------------------------
st.subheader("🏆 Top Performer")

if len(filtered_df) > 0:
    top_student = filtered_df.loc[filtered_df["Revenue"].idxmax()]
    st.write(f"Student ID: {top_student['Student_ID']}")
    st.write(f"Revenue: ₹{top_student['Revenue']:,.0f}")
else:
    st.warning("No data available for selected filters")

# -----------------------------
# DEBUG (OPTIONAL)
# -----------------------------
with st.expander("🔍 Debug Info"):
    st.write("Dataset Shape:", df.shape)
    st.write("Columns:", df.columns.tolist())

