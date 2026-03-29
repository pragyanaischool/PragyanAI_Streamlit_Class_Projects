import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import os

st.set_page_config(layout="wide")

st.title(" PragyanAI Student Data Advanced Visualization App")

# -----------------------------
# SAFE DATA LOADING
# -----------------------------
uploaded_file = st.file_uploader("Upload CSV (Recommended)", type=["csv"])

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    default_path = "student_PRICING_SCHOLARSHIP_Analysis_Project_12.csv"
    
    if os.path.exists(default_path):
        df = load_data(default_path)
    else:
        st.error("❌ Dataset not found. Please upload CSV.")
        st.stop()

st.success("✅ Data Loaded Successfully")

# -----------------------------
# SAFE COLUMN CHECK
# -----------------------------
required_cols = ["Final_Price", "Converted", "Program_Type", "Revenue", "Discount_%"]

missing = [col for col in required_cols if col not in df.columns]

if missing:
    st.error(f"❌ Missing columns: {missing}")
    st.stop()

# -----------------------------
# LIMIT DATA (avoid crash)
# -----------------------------
df = df.head(5000)

# -----------------------------
# BASIC GRID (SMALL + SAFE)
# -----------------------------
st.subheader(" Multi-Chart Dashboard")

fig1, axes1 = plt.subplots(2, 2, figsize=(12, 8))

axes1[0, 0].hist(df["Final_Price"], bins=20)
axes1[0, 0].set_title("Final Price")

sns.countplot(x="Converted", data=df, ax=axes1[0, 1])
axes1[0, 1].set_title("Conversion")

sns.boxplot(x="Program_Type", y="Final_Price", data=df, ax=axes1[1, 0])
axes1[1, 0].set_title("Price by Program")

axes1[1, 1].plot(df["Revenue"])
axes1[1, 1].set_title("Revenue Trend")

plt.tight_layout()
st.pyplot(fig1)
