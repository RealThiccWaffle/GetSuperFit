import streamlit as st
import pandas as pd
import time

# Set up the page
st.set_page_config(page_title="Sushi pH Tracker", layout="wide")
st.title("Sushi pH Tracker")

DATA_FILE = "sushi_ph_data.csv"

def load_data():
    try:
        data = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        data = pd.DataFrame(columns=["Date", "Time", "pH"])
        data.to_csv(DATA_FILE, index=False)
    return data

def save_data(data):
    data.to_csv(DATA_FILE, index=False)

def add_ph_data(date, time, ph):
    data = load_data()
    new_entry = pd.DataFrame({"Date": [date], "Time": [time], "pH": [ph]})
    data = data.append(new_entry, ignore_index=True)
    save_data(data)

data = load_data()

# Input form
with st.form("ph_form"):
    st.header("Add pH Data")
    
    # Current date and time
    current_time = time.localtime()
    current_date = time.strftime("%Y-%m-%d", current_time)
    current_time_12hour = time.strftime("%I:%M %p", current_time)

    date_input = st.date_input("Date", value=pd.to_datetime(current_date))
    time_input = st.text_input("Time", value=current_time_12hour)

    ph_input = st.number_input("pH Level", min_value=0.0, max_value=14.0, step=0.01)

    submit_button = st.form_submit_button("Submit")

if submit_button:
    add_ph_data(date_input, time_input, ph_input)
    st.success("New pH data added!")

# Display stored data
st.header("Stored pH Data")
st.write(data)
