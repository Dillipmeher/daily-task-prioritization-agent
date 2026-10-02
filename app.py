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

import pandas as pd

sample = pd.DataFrame([
    ["Prepare monthly procurement report", "High", "2026-10-02", 90, "Finance"],
    ["Follow up with pending vendor invoices", "High", "2026-10-02", 45, "Accounts"],
    ["Compare supplier quotations for sunflower oil", "High", "2026-10-02", 60, "Sourcing"],
    ["Review chicken quality complaints", "Medium", "2026-10-03", 45, "Quality"],
    ["Update supplier rate tracker", "Medium", "2026-10-03", 60, "Sourcing"],
    ["Check pending PO creation issues", "High", "2026-10-02", 30, "Purchase"],
    ["Prepare weekly team meeting notes", "Low", "2026-10-04", 30, "Admin"],
    ["Follow up on new vendor onboarding", "Medium", "2026-10-04", 45, "Sourcing"],
    ["Review price variance dashboard", "Medium", "2026-10-03", 60, "Analytics"],
    ["Send pending quotation requests", "High", "2026-10-02", 30, "Sourcing"],
], columns=["Task", "Priority", "Due_Date", "Estimated_Minutes", "Category"])

path = "/mnt/data/sample_tasks.csv"
sample.to_csv(path, index=False)

print(path)
print(sample)
