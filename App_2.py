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
# Grid Subplots Dashboard
# -----------------------------
st.subheader("Multi-Chart Dashboard (Subplots Grid)")

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
