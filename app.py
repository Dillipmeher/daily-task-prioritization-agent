import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(
page_title="Daily Task Prioritization Agent",
page_icon="📋",
layout="wide"
)

st.title("📋 Daily Task Prioritization Agent")

st.write("Upload your task list and generate a prioritized daily plan.")

sample_data = pd.DataFrame({
"Task": [
"Prepare monthly procurement report",
"Follow up with pending vendor invoices",
"Compare supplier quotations for sunflower oil",
"Review chicken quality complaints",
"Update supplier rate tracker",
"Check pending PO creation issues",
"Prepare weekly team meeting notes",
"Follow up on new vendor onboarding",
"Review price variance dashboard",
"Send pending quotation requests"
],
"Priority": [
"High",
"High",
"High",
"Medium",
"Medium",
"High",
"Low",
"Medium",
"Medium",
"High"
],
"Due_Date": [
"2026-10-02",
"2026-10-02",
"2026-10-02",
"2026-10-03",
"2026-10-03",
"2026-10-02",
"2026-10-04",
"2026-10-04",
"2026-10-03",
"2026-10-02"
],
"Estimated_Minutes": [
90,
45,
60,
45,
60,
30,
30,
45,
60,
30
],
"Category": [
"Finance",
"Accounts",
"Sourcing",
"Quality",
"Sourcing",
"Purchase",
"Admin",
"Sourcing",
"Analytics",
"Sourcing"
]
})

csv_buffer = StringIO()
sample_data.to_csv(csv_buffer, index=False)

st.subheader("📥 Step 1: Download Sample Format")

st.write(
"Download the sample CSV, open it in Excel, "
"replace the sample tasks with your own tasks, "
"and save it as CSV."
)

st.download_button(
"⬇️ Download Sample Tasks CSV",
csv_buffer.getvalue(),
"sample_tasks.csv",
"text/csv"
)

st.subheader("📤 Step 2: Upload Your Task File")

uploaded_file = st.file_uploader(
"Upload your tasks CSV file",
type=["csv"]
)

if uploaded_file is not None:

```
try:
    df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")

    st.subheader("📋 Your Tasks")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("📊 File Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Tasks", len(df))

    with col2:
        st.metric("Total Columns", len(df.columns))

except Exception as e:

    st.error(
        f"❌ Unable to read the CSV file: {e}"
    )
```

else:

```
st.info(
    "👆 Download the sample file first, "
    "then upload your completed task file."
)
```
