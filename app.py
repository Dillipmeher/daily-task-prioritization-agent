import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Daily Task Prioritization Agent",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Daily Task Prioritization Agent")

st.write(
    "Upload your task list and generate a prioritized daily plan."
)

uploaded_file = st.file_uploader(
    "Upload tasks.csv",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Your Tasks")

    st.dataframe(
        df,
        use_container_width=True
    )
