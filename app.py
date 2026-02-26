import streamlit as st
import pandas as pd
from db import get_databases, get_tables, get_schema
from executor import execute_with_retry

st.set_page_config(
    page_title="QueryMind: LLM Powered SQL Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# 🎨 PREMIUM UI STYLING RESTORED
# ==============================
st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 20px;
}

/* Card */
.card {
    background: linear-gradient(145deg, #0f172a, #111827);
    padding: 25px;
    border-radius: 16px;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    border: 1px solid rgba(255,255,255,0.05);
}

/* Input */
.stTextInput > div > div > input {
    background-color: #0f172a;
    border-radius: 12px;
    height: 50px;
    font-size: 16px;
    border: 1px solid #1f2937;
}

/* Button */
.stButton>button {
    border-radius: 12px;
    height: 45px;
    font-weight: 600;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0 5px 20px rgba(124, 58, 237, 0.5);
}

.stDataFrame {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# 🔷 ANIMATED PRODUCT TITLE
# ==============================

# ==============================
# 🔷 ULTRA SMOOTH HEADER CARD
# ==============================

st.markdown("""
<style>

/* Remove default top padding */
.block-container {
    padding-top: 2rem;
}

/* Remove extra white gap around app */
.main > div {
    padding-left: 3rem;
    padding-right: 3rem;
}

.top-header {
    width: 100%;
    padding: 36px 42px;
    background: linear-gradient(135deg, #1e293b, #312e81);
    border-radius: 24px;   /* 👈 Proper smooth edges */
    margin-bottom: 40px;
    box-shadow: 0 20px 60px rgba(49,46,129,0.35); /* soft premium glow */
}

.brand-row {
    display: flex;
    align-items: center;
    gap: 16px;
}

.brand-name {
    font-size: 44px;
    font-weight: 800;
    color: #60A5FA;
}

.subtitle {
    font-size: 18px;
    color: #d1d5db;
    margin-left: 60px;
    margin-top: 6px;
}

</style>

<div class="top-header">
    <div class="brand-row">
        <div style="font-size:38px;">🧠</div>
        <div class="brand-name">QueryMind</div>
    </div>
    <div class="subtitle">
        LLM-Powered Natural Language to SQL Engine ⚡📊
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================
# 🔵 SIDEBAR
# ==============================
with st.sidebar:

    st.header("📂 Database Panel")

    databases = get_databases()

    if isinstance(databases, list):

        selected_db = st.selectbox("Select Database", databases)

        if selected_db:

            tables = get_tables(selected_db)
            schema = get_schema(selected_db)

            with st.expander("📑 Tables", expanded=True):
                st.write(tables)

            with st.expander("📜 Schema", expanded=False):
                st.text_area("Schema", schema, height=300)

# ==============================
# 🟢 MAIN PANEL
# ==============================
if isinstance(databases, list) and selected_db:


    st.subheader("💬 Ask Your Question")

    user_question = st.text_input(
        "Enter your query in natural language:"
    )

    generate_btn = st.button("🚀 Generate SQL")

    st.markdown('</div>', unsafe_allow_html=True)

    if generate_btn:

        if user_question.strip() == "":
            st.warning("Please enter a question.")
            st.stop()

        with st.spinner("Generating and Executing SQL..."):

            result_data, final_query, error = execute_with_retry(
                selected_db,
                schema,
                user_question
            )

        # SQL Card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧾 Generated SQL")
        st.code(final_query, language="sql")
        st.markdown('</div>', unsafe_allow_html=True)

        if error:
            st.error(error)
        else:
            columns, result = result_data
            df = pd.DataFrame(result, columns=columns)

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("📊 Query Result")
            st.dataframe(df)

            numeric_columns = df.select_dtypes(
                include=["int64", "float64"]
            ).columns

            if len(numeric_columns) > 0:
                st.subheader("📈 Visualization")
                st.bar_chart(df[numeric_columns])

            st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# Footer
# ==============================
st.markdown(
    """
    <div style="
        text-align:center;
        font-size:14px;
        color:#A0A0A0;
        margin-top:145px;
        padding:15px;
        border-top:1px solid rgba(255,255,255,0.1);
        background:rgba(255,255,255,0.02);
        border-radius:8px;
    ">
        🚀 Built by <b style="color:#FFFFFF;">Pratham Soni</b> | QueryMind: LLM-Powered Natural Language to SQL Engine
    </div>
    """,
    unsafe_allow_html=True
)
