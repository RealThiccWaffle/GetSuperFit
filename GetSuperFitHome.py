import streamlit as st
import pandas as pd

def parse_date_time(year, month, day, hour, minute, am_pm):
    hour = int(hour)
    if am_pm == "PM" and hour != 12:
        hour += 12
    elif am_pm == "AM" and hour == 12:
        hour = 0
    return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}"

st.title("Sushi Rice pH Level Tracker")

with st.beta_columns(3):
    year = st.selectbox("Year", list(range(2020, 2031)))
    month = st.selectbox("Month", list(range(1, 13)))
    day = st.selectbox("Day", list(range(1, 32)))

with st.beta_columns(3):
    hour = st.selectbox("Hour", list(range(1, 13)))
    minute = st.selectbox("Minute", list(range(0, 60)))
    am_pm = st.selectbox("AM/PM", ["AM", "PM"])

ph_level = st.number_input("Enter pH level:", min_value=0.0, max_value=14.0, step=0.1)

add_data = st.button("Add Data")

data = {"Date_Time": [], "pH_Level": []}

if add_data:
    if year and month and day and hour and minute and ph_level:
        date_time = parse_date_time(year, month, day, hour, minute, am_pm)
        data["Date_Time"].append(date_time)
        data["pH_Level"].append(ph_level)
        st.success("Data added successfully.")
    else:
        st.error("Please fill in all fields correctly.")

data_df = pd.DataFrame(data)
st.write(data_df)
