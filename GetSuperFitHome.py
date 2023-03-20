import streamlit as st
import random

# List of available exercises for each muscle group
chest_exercises = ["Bench Press", "Incline Dumbbell Press", "Cable Flyes", "Dips"]
back_exercises = ["Lat Pulldowns", "Deadlifts", "Seated Rows", "Pull-Ups"]
leg_exercises = ["Squats", "Leg Press", "Lunges", "Deadlifts"]
shoulder_exercises = ["Military Press", "Arnold Press", "Lateral Raises", "Front Raises"]
bicep_exercises = ["Bicep Curls", "Hammer Curls", "Preacher Curls", "Incline Curls"]
tricep_exercises = ["Tricep Extensions", "Dips", "Skull Crushers", "Close Grip Bench Press"]
core_exercises = ["Plank", "Russian Twists", "Sit-Ups", "Hanging Leg Raises"]

# Define the workout plan generation function
def generate_workout(muscle_group, fitness_level, arms, bicep, core):
    st.write(f"Here's your hypertrophy workout for {muscle_group}:")
    st.write("")

    # Choose the number of sets and reps based on fitness level
    if fitness_level == "Beginner":
        sets = 3
        reps = 12
    elif fitness_level == "Intermediate":
        sets = 4
        reps = 10
    else:
        sets = 5
        reps = 8

    # Choose the main exercise for the muscle group
    if muscle_group == "Chest":
        main_exercise = random.choice(chest_exercises)
    elif muscle_group == "Back":
        main_exercise = random.choice(back_exercises)
    elif muscle_group == "Legs":
        main_exercise = random.choice(leg_exercises)
    else:
        main_exercise = random.choice(shoulder_exercises)

    st.write(f"Main Exercise: {main_exercise}")
    st.write("")

    # Choose additional exercises for the muscle group
    other_exercises = []
    for i in range(sets - 1):
        exercise = random.choice(eval(muscle_group.lower() + "_exercises"))
        while exercise == main_exercise or exercise in other_exercises:
            exercise = random.choice(eval(muscle_group.lower() + "_exercises"))
        other_exercises.append(exercise)

    for i, exercise in enumerate(other_exercises):
        st.write(f"Set {i+1}: {exercise} - {sets} sets x {reps} reps")
        st.write("")

    # Add arm exercises if requested
    if arms:
        if bicep:
            bicep_exercise = random.choice(bicep_exercises)
            st.write(f"Bicep Exercise: {bicep_exercise} - {sets} sets x {reps} reps")
            st.write("")
        tricep_exercise = random.choice(tricep_exercises)
        st.write(f"Tricep Exercise: {tricep_exercise} - {sets} sets x {reps} reps")
        st.write("")

    # Add core exercises if requested
    if core:
        core_exercise = random.choice(core_exercises)
        st.write(f"Core Exercise: {core_exercise} - {sets} sets x {reps} reps")
        st.write("")

# Define the Streamlit app
# Define the Streamlit app
def app():
    st.title("Hypertrophy Workout Generator")

    # Get user inputs
    muscle_group = st.selectbox("Select a muscle group:", ["Chest", "Back", "Legs", "Shoulders"])
    fitness_level = st.selectbox("Select your fitness level:", ["Beginner", "Intermediate", "Advanced"])
    arms = st.checkbox("Add arm exercises")
    if arms:
        bicep = st.checkbox("Add bicep exercises")
    else:
        bicep = False
    core = st.checkbox("Add core exercises")

    # Generate the workout plan
    generate_workout(muscle_group, fitness_level, arms, bicep, core)

# Run the Streamlit app
if __name__ == '__main__':
    app()
