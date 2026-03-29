import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

st.title(" PragyanAI Student Data Advance Visualization & Filtering App")

# Load Data
#df = pd.read_csv("student_PRICING_SCHOLARSHIP_Analysis_Project_12.csv")
# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("student_PRICING_SCHOLARSHIP_Analysis_Project_12.csv")
    return df

df = load_data()

# -----------------------------
# Charts
# -----------------------------
st.subheader(" Revenue Trend")
st.line_chart(df["Revenue"])

st.subheader(" Revenue by Program")
st.bar_chart(df.groupby("Program_Type")["Revenue"].sum())

st.subheader(" Discount Trend")
st.line_chart(df["Discount_%"])

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
st.subheader("Advanced Multi-Chart Dynamic Dashboard")

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
