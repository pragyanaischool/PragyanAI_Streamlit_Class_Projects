import streamlit as st
import pandas as pd
import os
from groq import Groq
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
    [" Home", "Dashboard", "Form", "Session State", "All Inputs","Advanced Media"]
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
elif page == "Dashboard":

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
elif page == "Form":

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
elif page == "Session State":

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

# =============================
# 🎛️ ALL INPUTS PAGE
# =============================
elif page == "All Inputs":

    st.subheader(" Streamlit All Input Widgets Playground")

    st.write("👉 This page demonstrates all types of user inputs in Streamlit")

    # -------------------------
    # TEXT INPUT
    # -------------------------
    name = st.text_input("Enter your name")

    # -------------------------
    # NUMBER INPUT
    # -------------------------
    age = st.number_input("Enter your age", min_value=1, max_value=100, value=18)

    # -------------------------
    # SLIDER
    # -------------------------
    price = st.slider("Select Budget", 1000, 100000, 5000)

    # -------------------------
    # SELECTBOX
    # -------------------------
    program = st.selectbox(
        "Choose Program",
        options=df["Program_Type"].unique()
    )

    # -------------------------
    # MULTISELECT
    # -------------------------
    programs = st.multiselect(
        "Select Multiple Programs",
        options=df["Program_Type"].unique()
    )

    # -------------------------
    # RADIO BUTTON
    # -------------------------
    gender = st.radio("Select Gender", ["Male", "Female", "Other"])

    # -------------------------
    # CHECKBOX
    # -------------------------
    agree = st.checkbox("I agree to terms & conditions")

    # -------------------------
    # DATE INPUT
    # -------------------------
    date = st.date_input("Select Date")

    # -------------------------
    # FILE UPLOADER
    # -------------------------
    uploaded_file = st.file_uploader("Upload a CSV File", type=["csv"])

    if uploaded_file:
        uploaded_df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data Preview")
        st.dataframe(uploaded_df.head())

    # -------------------------
    # BUTTON
    # -------------------------
    if st.button("Submit All Inputs"):
        st.success("✅ Inputs Submitted Successfully!")

        st.write("### 📌 Summary of Inputs")
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Budget: ₹{price}")
        st.write(f"Program: {program}")
        st.write(f"Selected Programs: {programs}")
        st.write(f"Gender: {gender}")
        st.write(f"Agreed: {agree}")
        st.write(f"Date: {date}")
# =============================
# 🎬 ADVANCED MEDIA & AI PAGE
# =============================
elif page == "Advanced Media":

    st.subheader("Advanced Media & AI Features")

    # =====================================
    # 🖼️ IMAGE UPLOAD & DISPLAY
    # =====================================
    st.write("## Image Upload")

    image_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

    if image_file:
        st.image(image_file, caption="Uploaded Image", use_container_width=True)

    # =====================================
    # 🎵 AUDIO UPLOAD & PLAY
    # =====================================
    st.write("## Audio Upload & Play")

    audio_file = st.file_uploader("Upload Audio", type=["mp3", "wav","m4a"])

    if audio_file:
        st.audio(audio_file)

    # =====================================
    # 🎥 VIDEO DISPLAY (YouTube)
    # =====================================
    st.write("## YouTube Video")

    video_url = st.text_input("Enter YouTube URL")

    if video_url:
        st.video(video_url)

    st.subheader("💬 AI Chat Assistant (Groq Powered)")

    # -----------------------------
    # Initialize Groq Client
    # -----------------------------
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", None)

    if not GROQ_API_KEY:
        st.error("❌ GROQ API Key not found in secrets")
        st.stop()

    client = Groq(api_key=GROQ_API_KEY)

    # -----------------------------
    # Session State for Chat Memory
    # -----------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # -----------------------------
    # Display Chat History
    # -----------------------------
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # -----------------------------
    # User Input
    # -----------------------------
    user_input = st.chat_input("Ask anything about data, pricing, AI...")

    if user_input:

        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.write(user_input)

        # -----------------------------
        # SYSTEM PROMPT (VERY IMPORTANT)
        # -----------------------------
        system_prompt = """
        You are an AI Data Analytics Assistant for PragyanAI.
        Help users understand data, pricing, conversions, and insights.
        Give clear, concise, and actionable answers.
        """

        # -----------------------------
        # Call Groq LLM
        # -----------------------------
        try:
            response = client.chat.completions.create(
                model="llama3-70b-8192",  # fast + powerful
                messages=[
                    {"role": "system", "content": system_prompt},
                    *st.session_state.messages
                ],
                temperature=0.3
            )

            bot_reply = response.choices[0].message.content

        except Exception as e:
            bot_reply = f"❌ Error: {str(e)}"

        # -----------------------------
        # Store Assistant Response
        # -----------------------------
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_reply
        })

        # -----------------------------
        # Display Response
        # -----------------------------
        with st.chat_message("assistant"):
            st.write(bot_reply)

    # =====================================
    # 🎤 AUDIO RECORD (MIC INPUT - BROWSER BASED)
    # =====================================
    st.write("## Voice Input (Experimental)")

    try:
        audio_value = st.audio_input("Record your voice")

        if audio_value:
            st.audio(audio_value)
            st.success("Voice recorded successfully!")
    except:
        st.info("Audio recording not supported in this environment")

    # =====================================
    # 📥 DOWNLOAD BUTTON
    # =====================================
    st.write("## Download Sample Report")

    sample_text = "PragyanAI Report Generated"

    st.download_button(
        label="Download Report",
        data=sample_text,
        file_name="report.txt",
        mime="text/plain"
    )

    # =====================================
    # 📦 EXPANDER (ADVANCED UI)
    # =====================================
    with st.expander("More Advanced Options"):
        st.write("This section can contain advanced analytics or settings")

    # =====================================
    # 🎨 PROGRESS BAR
    # =====================================
    st.write("## Progress Indicator")

    progress = st.progress(0)

    for i in range(100):
        progress.progress(i + 1)

    st.success("Task Completed!")
