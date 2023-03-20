import streamlit as st
import random
import time

def generate_workout(target_muscle, fitness_level, add_extras):
    workouts = {
        "chest": {
            "beginner": [("Bench Press", 4, 8), ("Push-ups", 3, 15), ("Incline Dumbbell Press", 3, 8)],
            "intermediate": [("Bench Press", 5, 8), ("Chest Fly", 4, 10), ("Incline Dumbbell Press", 4, 8), ("Decline Push-ups", 3, 15)],
            "advanced": [("Bench Press", 5, 8), ("Chest Fly", 4, 10), ("Incline Dumbbell Press", 4, 8), ("Cable Crossover", 3, 10), ("Decline Push-ups", 3, 15)],
        },
        "legs": {
            "beginner": [("Squat", 4, 10), ("Lunges", 3, 12), ("Leg Press", 3, 10)],
            "intermediate": [("Squat", 5, 10), ("Lunges", 4, 12), ("Leg Press", 4, 10), ("Leg Curl", 3, 12)],
            "advanced": [("Squat", 5, 10), ("Lunges", 4, 12), ("Leg Press", 4, 10), ("Leg Curl", 3, 12), ("Calf Raises", 3, 15)],
        },
        "back_shoulders": {
            "beginner": [("Deadlift", 4, 8), ("Pull-ups", 3, 10), ("Seated Rows", 3, 10)],
            "intermediate": [("Deadlift", 5, 8), ("Pull-ups", 4, 10), ("Seated Rows", 4, 10), ("Face Pull", 3, 12)],
            "advanced": [("Deadlift", 5, 8), ("Pull-ups", 4, 10), ("Seated Rows", 4, 10), ("Face Pull", 3, 12), ("Lateral Raises", 3, 15)],
        },
        "arms": {
            "beginner": [("Bicep Curls", 3, 12), ("Tricep Dips", 3, 12), ("Hammer Curls", 3, 12)],
            "intermediate": [("Bicep Curls", 4, 12), ("Tricep Dips", 4, 12), ("Hammer Curls", 4, 12), ("Skull Crushers", 3, 12)],
            "advanced": [("Bicep Curls", 4, 12), ("Tricep Dips", 4, 12), ("Hammer Curls", 4, 12), ("Skull Crushers", 3, 12), ("Close-grip Bench Press", 3, 8)],
        },
    }

    extra_workouts = {
        "triceps": [("Tricep Pushdown", 2, 12), ("Close-grip Bench Press", 2, 8)],
        "biceps": [("Preacher Curl", 2, 12), ("Concentration Curl", 2, 10)],
        "core": [("Plank", 2, "60s"), ("Russian Twists", 2, 20), ("Leg Raises", 2, 12), ("Mountain Climbers", 2, 30)],
    }

    workout = workouts[target_muscle][fitness_level]
    random.shuffle(workout)

    if add_extras != "None":
        workout.extend(random.sample(extra_workouts[add_extras], 2))

    return workout

st.title("Hypertrophy Workout Generator")

target_muscle = st.selectbox("Choose a target muscle:", ["chest", "legs", "back_shoulders", "arms"])
fitness_level = st.selectbox("Choose your fitness level:", ["beginner", "intermediate", "advanced"])
add_extras = st.selectbox("Add extra exercises (optional):", ["None", "triceps", "biceps", "core"])

# Add Tone.js library
st.markdown(
    '<script src="https://cdn.jsdelivr.net/npm/tone@14.8.30/build/Tone.min.js"></script>',
    unsafe_allow_html=True,
)

# Beep sound script
BEEP_SOUND_SCRIPT = '''
<script>
    function playBeep() {
        const synth = new Tone.Synth().toDestination();
        synth.triggerAttackRelease("C4", "8n");
    }
</script>
'''

st.markdown(BEEP_SOUND_SCRIPT, unsafe_allow_html=True)

progress_bar = st.empty()
time_remaining = st.empty()

if st.button("Start 60s Timer"):
    st.markdown('<span id="timeRemaining" style="display:none;">60</span>', unsafe_allow_html=True)
    st.markdown("<script>updateTimer();</script>", unsafe_allow_html=True)
    for i in range(60, 0, -1):
        progress_bar.progress((60 - i) / 60)
        time_remaining.text(f"Time remaining: {i}s")
        time.sleep(1)
    time_remaining.text("Time's up!")
    st.markdown("<script>playBeep();</script>", unsafe_allow_html=True)

if st.button("Generate Workout"):
    st.header("Generated Workout")
    workout = generate_workout(target_muscle, fitness_level, add_extras)
    workout_container = st.empty()

    for index, (exercise, sets, reps) in enumerate(workout):
        workout_container.subheader(f"{index + 1}. {exercise}")
        workout_container.write(f"Sets: {sets} - Reps: {reps}")

    if st.button("Clear Workout"):
        workout_container.empty()

# ... (Add additional content and scripts as required)
st.sidebar.title("Additional Information")
page = st.sidebar.selectbox("Choose a topic:", ["None", "Hypertrophy Training Tips", "Supplements", "How to Use the App"])

if page == "Hypertrophy Training Tips":
    st.sidebar.header("Hypertrophy Training Tips")
    st.sidebar.subheader("Reps and Intensity")
    st.sidebar.write("""
    When training for hypertrophy, aim for 6-12 reps per set at an intensity of 60-85% of your one-rep max (1RM). This rep range and intensity have been found to be optimal for muscle growth.
    """)

    st.sidebar.subheader("Diet")
    st.sidebar.write("""
    To support muscle growth, consume a calorie surplus and ensure you're getting enough protein. Aim for a daily protein intake of 0.7-1.0 grams per pound of body weight.
    """)

    st.sidebar.subheader("Split Training")
    st.sidebar.write("""
    Split training allows you to focus on specific muscle groups in each workout, which can be useful for targeting weak areas and ensuring adequate recovery between workouts.
    """)

elif page == "Supplements":
    st.sidebar.header("Supplements")
    st.sidebar.subheader("Protein Powder")
    st.sidebar.write("""
    Protein powder can be a convenient way to increase your daily protein intake. Look for a high-quality protein source like whey, casein, or a plant-based alternative.
    """)

    st.sidebar.subheader("Creatine")
    st.sidebar.write("""
    Creatine is a popular supplement that has been shown to increase muscle strength, power, and size. Aim for a daily intake of 3-5 grams.
    """)

    st.sidebar.subheader("BCAAs")
    st.sidebar.write("""
    Branched-chain amino acids (BCAAs) can help support muscle recovery and growth. They can be found in protein-rich foods or taken as a supplement.
    """)

elif page == "How to Use the App":
    st.sidebar.header("How to Use the App")
    st.sidebar.write("""
    1. Select the target muscle group you'd like to focus on.
    2. Choose your fitness level (beginner, intermediate, or advanced).
    3. Optionally, add extra exercises to your workout.
    4. Click the 'Generate Workout' button to create your custom workout.
    5. The generated workout will appear on the main screen with the exercises, sets, and reps.
    6. Use the 60-second timer to time your rest periods between sets.
    7. Click the 'Clear Workout' button to remove the current workout and generate a new one.
    """)

