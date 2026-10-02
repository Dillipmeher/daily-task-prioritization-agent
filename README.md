# daily-task-prioritization-agent
# 📋 Daily Task Prioritization Agent

A Python and Streamlit application that helps prioritize daily tasks based on **deadline, effort, impact, and blocked status**.

## 🎯 Project Objective

The application reads a list of tasks from a CSV file, calculates a priority score for each task, and generates a daily action plan.

The plan categorizes tasks into:

* **TOP 3** – Tasks to complete first
* **NEXT 5** – Tasks to complete after the top priorities
* **UNBLOCK** – Tasks that are currently blocked
* **DEFER** – Lower-priority tasks that can be postponed

## 📊 Input Data

The application uses a CSV file with the following columns:

| Column      | Description                                  |
| ----------- | -------------------------------------------- |
| title       | Task name                                    |
| description | Task details                                 |
| deadline    | Task deadline                                |
| effort      | Estimated effort such as 10m, 25m, S, M or L |
| impact      | Low, Medium or High                          |
| blocked     | Yes or No                                    |
| tags        | Task category                                |

## 🧮 Priority Scoring

Tasks are prioritized using:

**Priority Score = Urgency + Importance + Quick Win Bonus − Blocked Penalty**

The scoring considers:

* Deadline urgency
* Task impact
* Quick-win opportunities
* Whether the task is blocked

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* GitHub
* CSV

## 🚀 How to Use

1. Open the Streamlit application.
2. Upload the `tasks.csv` file.
3. Review the uploaded tasks.
4. Generate the daily priority plan.
5. Review the TOP 3, NEXT 5, UNBLOCK and DEFER sections.

## 📁 Project Structure

```text
daily-task-prioritization-agent/
│
├── app.py
├── tasks.csv
└── README.md
```

## 🔮 Future Improvements

* Add available-time planning
* Add priority score explanations
* Add downloadable JSON and TXT plans
* Add charts and dashboard
* Allow users to add/edit tasks directly in the application
* Improve the prioritization logic

