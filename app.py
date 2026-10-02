import streamlit as st
import pandas as pd

st.set_page_config(page_title="Daily Task Prioritization Agent", page_icon="📋")

st.title("📋 Daily Task Prioritization Agent")
st.write("Upload your task list and generate a prioritized daily plan.")

sample_data = pd.DataFrame({
    "Task": [
        "Prepare monthly procurement report",
        "Follow up with pending vendor invoices",
        "Compare supplier quotations",
        "Review quality complaints",
        "Update supplier rate tracker"
    ],
    "Priority": [
        "High",
        "High",
        "High",
        "Medium",
        "Medium"
    ],
    "Due_Date": [
        "2026-10-02",
        "2026-10-02",
        "2026-10-02",
        "2026-10-03",
        "2026-10-03"
    ],
    "Estimated_Minutes": [
        90,
        45,
        60,
        45,
        60
    ],
    "Category": [
        "Finance",
        "Accounts",
        "Sourcing",
        "Quality",
        "Sourcing"
    ]
})

csv_data = sample_data.to_csv(index=False)

st.subheader("📥 Step 1: Download Sample Format")

st.download_button(
    label="⬇️ Download Sample Tasks CSV",
    data=csv_data,
    file_name="sample_tasks.csv",
    mime="text/csv"
)

st.subheader("📤 Step 2: Upload Your Task File")

uploaded_file = st.file_uploader(
    "Choose your CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")

    st.subheader("📋 Your Tasks")
    st.dataframe(df, use_container_width=True)

    st.subheader("📊 File Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Tasks", len(df))

    with col2:
        st.metric("Total Columns", len(df.columns))

else:
    st.info("👆 Download the sample file first, then upload your completed CSV.")
