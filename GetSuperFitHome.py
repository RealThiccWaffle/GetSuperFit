import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Set up the page
st.set_page_config(page_title="Sushi pH Tracker", layout="wide")
st.title("Sushi pH Tracker")
DATA_FILE = "sushi_ph_data.csv"

# Check if the data file exists; if not, create one
if not os.path.isfile(DATA_FILE):
    data = pd.DataFrame(columns=["Date", "Time", "pH"])
    data.to_csv(DATA_FILE, index=False)

# Load existing data
data = pd.read_csv(DATA_FILE)
# Input fields
date_input = st.date_input("Date", value=datetime.today())
time_input = st.time_input("Time")

# Format time in 12-hour format
time_12hour = time_input.strftime("%I:%M %p")

ph_input = st.number_input("pH Level", min_value=0.0, max_value=14.0, step=0.01)

# Submit button
if st.button("Add pH Data"):
    new_entry = pd.DataFrame({"Date": [date_input], "Time": [time_12hour], "pH": [ph_input]})
    data = data.append(new_entry, ignore_index=True)
    data.to_csv(DATA_FILE, index=False)
    st.success("New pH data added!")
# Display stored data
st.header("Stored pH Data")
st.write(data)
