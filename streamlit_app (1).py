
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
