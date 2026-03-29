import streamlit as st
import pandas as pd
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="PragyanAI Advanced Dashboard", layout="wide")

st.title(" PragyanAI Advanced Streamlit UI Dashboard")

# -----------------------------
# LOAD DATA (SAFE)
# -----------------------------
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

file_path = "student_PRICING_SCHOLARSHIP_Analysis_Project_12.csv"

if os.path.exists(file_path):
    df = load_data(file_path)
else:
    st.error("❌ Dataset not found")
    st.stop()

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
st.sidebar.title(" Navigation")

page = st.sidebar.radio(
    "Go to",
    [" Home", " Dashboard", " Form", " Session State"]
)

# =============================
# 🏠 HOME
# =============================
if page == " Home":
    st.subheader("Welcome to PragyanAI Dashboard")
    st.write("This app demonstrates all major Streamlit UI features")

# =============================
# 📊 DASHBOARD (TABS)
# =============================
elif page == " Dashboard":

    st.subheader(" Data Analytics Dashboard")

    tab1, tab2, tab3 = st.tabs([" Data", " Charts", " KPIs"])

    # -------------------------
    # TAB 1: DATA
    # -------------------------
    with tab1:
        st.write("### Dataset Preview")
        st.dataframe(df.head())

    # -------------------------
    # TAB 2: CHARTS
    # -------------------------
    with tab2:
        st.write("### Revenue Trend")
        st.line_chart(df["Revenue"])

        st.write("### Revenue by Program")
        st.bar_chart(df.groupby("Program_Type")["Revenue"].sum())

    # -------------------------
    # TAB 3: KPIs
    # -------------------------
    with tab3:
        col1, col2, col3 = st.columns(3)

        total_students = len(df)
        avg_price = df["Final_Price"].mean()
        conversion_rate = df["Converted"].mean() * 100

        col1.metric("Total Students", total_students)
        col2.metric("Avg Price", f"₹{avg_price:,.0f}")
        col3.metric("Conversion Rate", f"{conversion_rate:.2f}%")

# =============================
# 📝 FORM PAGE
# =============================
elif page == "📝 Form":

    st.subheader("📝 Student Input Form")

    with st.form("student_form"):
        name = st.text_input("Enter Name")
        marks = st.number_input("Enter Marks", 0, 100)
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"✅ Student {name} scored {marks}")

# =============================
# 🧠 SESSION STATE PAGE
# =============================
elif page == " Session State":

    st.subheader(" Session State Counter")

    if "count" not in st.session_state:
        st.session_state.count = 0

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Increase"):
            st.session_state.count += 1

    with col2:
        if st.button("Reset"):
            st.session_state.count = 0

    st.write("### Current Count:", st.session_state.count)
