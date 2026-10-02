import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Daily Task Prioritization Agent", page_icon="📋")

st.title("📋 Daily Task Prioritization Agent")
st.write("Upload your task list and generate a prioritized daily plan.")

# ---------- Sample data ----------
sample_data = pd.DataFrame({
    "Task": [
        "Prepare monthly procurement report",
        "Follow up with pending vendor invoices",
        "Compare supplier quotations",
        "Review quality complaints",
        "Update supplier rate tracker"
    ],
    "Priority": ["High", "High", "High", "Medium", "Medium"],
    "Due_Date": ["2026-10-02", "2026-10-02", "2026-10-02", "2026-10-03", "2026-10-03"],
    "Estimated_Minutes": [90, 45, 60, 45, 60],
    "Category": ["Finance", "Accounts", "Sourcing", "Quality", "Sourcing"]
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
uploaded_file = st.file_uploader("Choose your CSV file", type=["csv"])


# ---------- Prioritization logic ----------
PRIORITY_POINTS = {"high": 30, "medium": 20, "low": 10}


def urgency_points(days_left):
    if pd.isna(days_left):
        return 0
    if days_left < 0:
        return 50   # overdue
    if days_left == 0:
        return 40   # due today
    if days_left == 1:
        return 30   # due tomorrow
    if days_left <= 3:
        return 20
    if days_left <= 7:
        return 10
    return 0


def build_plan(df, available_minutes, start_time):
    df = df.copy()
    today = pd.Timestamp.today().normalize()

    df["Due_Date"] = pd.to_datetime(df["Due_Date"], errors="coerce")
    df["Days_Left"] = (df["Due_Date"] - today).dt.days
    df["Estimated_Minutes"] = pd.to_numeric(
        df["Estimated_Minutes"], errors="coerce"
    ).fillna(30)

    df["Priority_Points"] = (
        df["Priority"].astype(str).str.strip().str.lower().map(PRIORITY_POINTS).fillna(10)
    )
    df["Urgency_Points"] = df["Days_Left"].apply(urgency_points)
    df["Score"] = df["Priority_Points"] + df["Urgency_Points"]

    # Highest score first; for ties, shorter tasks first
    df = df.sort_values(
        by=["Score", "Estimated_Minutes"], ascending=[False, True]
    ).reset_index(drop=True)
    df.insert(0, "Rank", df.index + 1)

    # Fit tasks into the available time
    used = 0
    current = start_time
    statuses, starts, ends = [], [], []

    for _, row in df.iterrows():
        mins = int(row["Estimated_Minutes"])
        if used + mins <= available_minutes:
            end = current + timedelta(minutes=mins)
            statuses.append("✅ Do Today")
            starts.append(current.strftime("%I:%M %p"))
            ends.append(end.strftime("%I:%M %p"))
            current = end
            used += mins
        else:
            statuses.append("⏭️ Defer")
            starts.append("-")
            ends.append("-")

    df["Status"] = statuses
    df["Start"] = starts
    df["End"] = ends
    df["Due_Date"] = df["Due_Date"].dt.strftime("%Y-%m-%d")
    return df, used


# ---------- App flow ----------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    required = ["Task", "Priority", "Due_Date", "Estimated_Minutes"]
    missing = [c for c in required if c not in df.columns]

    if missing:
        st.error(f"Your file is missing these columns: {', '.join(missing)}")
    else:
        st.success("✅ File uploaded successfully!")

        st.subheader("⚙️ Step 3: Set Your Day")
        col_a, col_b = st.columns(2)
        with col_a:
            hours = st.slider("Available working hours today", 1.0, 12.0, 6.0, 0.5)
        with col_b:
            start = st.time_input("Start time", value=datetime.strptime("09:00", "%H:%M").time())

        start_dt = datetime.combine(datetime.today(), start)
        plan, used = build_plan(df, int(hours * 60), start_dt)

        st.subheader("🎯 Your Prioritized Plan")

        today_tasks = plan[plan["Status"] == "✅ Do Today"]
        deferred = plan[plan["Status"] == "⏭️ Defer"]

        m1, m2, m3 = st.columns(3)
        m1.metric("Tasks Today", len(today_tasks))
        m2.metric("Deferred", len(deferred))
        m3.metric("Time Planned", f"{used} / {int(hours * 60)} min")

        show_cols = ["Rank", "Task", "Priority", "Due_Date", "Estimated_Minutes",
                     "Score", "Status", "Start", "End"]
        if "Category" in plan.columns:
            show_cols.insert(3, "Category")

        st.dataframe(plan[show_cols], use_container_width=True, hide_index=True)

        if len(today_tasks) > 0:
            st.subheader("🗓️ Today's Schedule")
            for _, r in today_tasks.iterrows():
                st.write(f"**{r['Start']} – {r['End']}** → {r['Task']}  ·  _{r['Priority']}_")

        if len(deferred) > 0:
            st.warning("These tasks did not fit in today's time: "
                       + ", ".join(deferred["Task"].tolist()))

        st.download_button(
            "⬇️ Download Prioritized Plan",
            data=plan[show_cols].to_csv(index=False),
            file_name="prioritized_plan.csv",
            mime="text/csv"
        )
else:
    st.info("👆 Download the sample file first, then upload your completed CSV.")
