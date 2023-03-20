import streamlit as st
import random

# Define exercises for each muscle group
exercises = {
    'Chest': ['Bench Press', 'Dumbbell Fly', 'Incline Bench Press'],
    'Back': ['Deadlift', 'Lat Pulldown', 'Barbell Row'],
    'Legs': ['Squat', 'Lunges', 'Leg Press'],
    'Shoulders': ['Military Press', 'Lateral Raise', 'Front Raise'],
    'Arms': ['Bicep Curl', 'Tricep Extension', 'Hammer Curl'],
    'Core': ['Plank', 'Crunches', 'Russian Twist']
}

# Define rep and set schemes for strength and hypertrophy training
strength_schemes = [
    {'reps': 3, 'sets': 5},
    {'reps': 5, 'sets': 5},
    {'reps': 6, 'sets': 4},
    {'reps': 8, 'sets': 3},
    {'reps': 10, 'sets': 3}
]

hypertrophy_schemes = [
    {'reps': 12, 'sets': 4},
    {'reps': 10, 'sets': 4},
    {'reps': 8, 'sets': 4},
    {'reps': 6, 'sets': 4},
    {'reps': 12, 'sets': 3}
]

# Define function to generate workout based on user input
def generate_workout(muscle_group, fitness_level, add_arms, add_bicep, add_core, training_type):
    st.write(f'## Workout Plan for {muscle_group}')
    st.write(f'### Fitness Level: {fitness_level}')
    if add_arms:
        exercises[muscle_group] += exercises['Arms']
    if add_bicep:
        exercises[muscle_group] += ['Bicep Curl']
    if add_core:
        exercises[muscle_group] += exercises['Core']
    st.write('#### Exercises:')
    for exercise in random.sample(exercises[muscle_group], k=3):
        st.write(f'- {exercise}')
        if training_type == 'Strength':
            scheme = random.choice(strength_schemes)
        else:
            scheme = random.choice(hypertrophy_schemes)
        st.write(f'   - Reps: {scheme["reps"]}')
        st.write(f'   - Sets: {scheme["sets"]}')

# Define Streamlit app
def app():
    st.set_page_config(page_title='Hypertrophy Workout Generator', page_icon=':muscle:', layout='wide')
    st.title('Hypertrophy Workout Generator')
    muscle_group = st.selectbox('Select Muscle Group', ['Chest', 'Back', 'Legs', 'Shoulders'])
    fitness_level = st.selectbox('Select Fitness Level', ['Beginner', 'Intermediate', 'Advanced'])
    add_arms = st.checkbox('Add Arms')
    add_bicep = st.checkbox('Add Bicep')
    add_core = st.checkbox('Add Core')
    training_type = st.selectbox('Select Training Type', ['Strength', 'Hypertrophy'])
    generate_workout(muscle_group, fitness_level, add_arms, add_bicep, add_core, training_type)

if __name__ == '__main__':
    app()
