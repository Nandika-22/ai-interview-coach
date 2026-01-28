import sqlite3

conn = sqlite3.connect("interview.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interview_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT,
    question TEXT,
    answer TEXT,
    score INTEGER,
    date TEXT
)
""")
conn.commit()

import streamlit as st
import sqlite3

st.title("AI Interview Coach")

conn = sqlite3.connect("interview.db")
cursor = conn.cursor()

st.subheader("Interview Records")

cursor.execute("SELECT * FROM interview_attempts")
rows = cursor.fetchall()

for row in rows:
    st.write(row)

cursor.execute("""
SELECT user_name, COUNT(*), AVG(score)
FROM interview_attempts
GROUP BY user_name
""")
rows = cursor.fetchall()

