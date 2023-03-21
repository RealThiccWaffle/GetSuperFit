import streamlit as st
import pandas as pd

def parse_date_time(date_str, time_str):
    return f"{date_str} {time_str}"

st.title("Sushi Rice pH Level Tracker")

date_input = st.text_input("Enter date (YYYY-MM-DD):")
time_input = st.text_input("Enter time (HH:mm):")
ph_level = st.number_input("Enter pH level:", min_value=0.0, max_value=14.0, step=0.1)

add_data = st.button("Add Data")

data = {"Date_Time": [], "pH_Level": []}

if add_data:
    if date_input and time_input and ph_level:
        date_time = parse_date_time(date_input, time_input)
        data["Date_Time"].append(date_time)
        data["pH_Level"].append(ph_level)
        st.success("Data added successfully.")
    else:
        st.error("Please fill in all fields correctly.")

data_df = pd.DataFrame(data)
st.write(data_df)
