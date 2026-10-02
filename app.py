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
    "Upload your tasks CSV file",
    type=["csv"]
)
if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.success("✅ File uploaded successfully!")

        st.subheader("Your Tasks")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.write("### File Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Total Tasks",
                len(df)
            )

        with col2:
            st.metric(
                "Total Columns",
                len(df.columns)
            )

    except Exception as e:
        st.error(f"❌ Unable to read the CSV file: {e}")

else:
    st.info("👆 Please upload your tasks CSV file to begin.")
:::

**Important:** In GitHub, paste the code **without** the `:::writing...` lines and without any ` ``` ` lines. Your first line must be exactly:

```text
import streamlit as st
