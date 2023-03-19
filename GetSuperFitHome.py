import streamlit as st
import random
import time
def generate_workout(training_type, target_muscle, fitness_level, add_extras):
    workouts = {
        "split": {
            "chest": {
                "beginner": [("Bench Press", 3, 8), ("Push-ups", 3, 12)],
                "intermediate": [("Bench Press", 4, 10), ("Incline Bench Press", 3, 8), ("Push-ups", 3, 15)],
                "advanced": [("Bench Press", 5, 10), ("Incline Bench Press", 4, 8), ("Decline Bench Press", 4, 8), ("Dips", 3, 12)],
            },
            "back": {
                "beginner": [("Pull-ups", 3, 5), ("Bent-over Rows", 3, 8)],
                "intermediate": [("Pull-ups", 4, 8), ("Bent-over Rows", 3, 10), ("Seated Rows", 3, 10)],
                "advanced": [("Pull-ups", 5, 10), ("Bent-over Rows", 4, 10), ("Seated Rows", 4, 10), ("T-bar Rows", 4, 10)],
            },
            "quads": {
                "beginner": [("Squats", 3, 8), ("Lunges", 3, 8)],
                "intermediate": [("Squats", 4, 10), ("Lunges", 3, 10), ("Leg Press", 3, 10)],
                "advanced": [("Squats", 5, 10), ("Lunges", 4, 10), ("Leg Press", 4, 10), ("Hack Squat", 4, 10)],
            },
            "hamstrings": {
                "beginner": [("Romanian Deadlift", 3, 8), ("Lying Leg Curls", 3, 8)],
                "intermediate": [("Romanian Deadlift", 4, 10), ("Lying Leg Curls", 3, 10), ("Seated Leg Curls", 3, 10)],
                "advanced": [("Romanian Deadlift", 5, 10), ("Lying Leg Curls", 4, 10), ("Seated Leg Curls", 4, 10), ("Stiff Leg Deadlift", 4, 10)],
            },
            "biceps": {
                "beginner": [("Bicep Curls", 3, 8), ("Hammer Curls", 3, 8)],
                "intermediate": [("Bicep Curls", 4, 10), ("Hammer Curls", 3, 10), ("Concentration Curls", 3, 10)],
                "advanced": [("Bicep Curls", 5, 10), ("Hammer Curls", 4, 10), ("Concentration Curls", 4, 10), ("Preacher Curls", 4, 10)],
            },
            "triceps": {
                "beginner": [("Tricep Dips", 3, 8), ("Tricep Pushdowns", 3, 8)],
                "intermediate": [("Tricep Dips", 4, 10), ("Tricep Pushdowns", 3, 10), ("Skull Crushers", 3, 10)],
                "advanced": [("Tricep Dips", 5, 10), ("Tricep Pushdowns", 4, 10), ("Skull Crushers", 4, 10), ("Close-grip Bench Press", 4, 10)],
            },
            "shoulders": {
                "beginner": [("Shoulder Press", 3, 8), ("Lateral Raises", 3, 8)],
                "intermediate": [("Shoulder Press", 4, 10), ("Lateral Raises", 3, 10), ("Front Raises", 3, 10)],
                "advanced": [("Shoulder Press", 5, 10), ("Lateral Raises", 4, 10), ("Front Raises", 4, 10), ("Bent-over Reverse Fly", 4, 10)],
            },
            "calves": {
                "beginner": [("Standing Calf Raises", 3, 12), ("Seated Calf Raises", 3, 12)],
                "intermediate": [("Standing Calf Raises", 4, 15), ("Seated Calf Raises", 3, 15), ("Leg Press Calf Raises", 3, 15)],
                "advanced": [("Standing Calf Raises", 5, 15), ("Seated Calf Raises", 4, 15), ("Leg Press Calf Raises", 4, 15), ("Donkey Calf Raises", 4, 15)],
            },
        },
        "full_body": {
            "all": {
                "beginner": [("Squats", 3, 8), ("Bench Press", 3, 8), ("Bent-over Rows", 3, 8), ("Shoulder Press", 3, 8), ("Bicep Curls", 3, 8), ("Tricep Dips", 3, 8), ("Standing Calf Raises", 3, 12)],
                "intermediate": [("Squats", 4, 10), ("Bench Press", 4, 10), ("Bent-over Rows", 4, 10), ("Shoulder Press", 4, 10), ("Bicep Curls", 4, 10), ("Tricep Dips", 4, 10), ("Standing Calf Raises", 4, 15)],
                "advanced": [("Squats", 5, 10), ("Bench Press", 5, 10), ("Bent-over Rows", 5, 10), ("Shoulder Press", 5, 10), ("Bicep Curls", 5, 10), ("Tricep Dips", 5, 10), ("Standing Calf Raises", 5, 15)],
            }
        }
    }

    extra_workouts = {
        "triceps": [("Tricep Dips", 3, 10), ("Tricep Pushdowns", 3, 10), ("Skull Crushers", 3, 10)],
        "biceps": [("Bicep Curls", 3, 10), ("Hammer Curls", 3, 10), ("Concentration Curls", 3, 10)],
        "core": [("Planks", 3, 30), ("Russian Twists", 3, 20), ("Leg Raises", 3, 15)]
    }

    if training_type == "full_body":
        workout = workouts[training_type]["all"][fitness_level]
    else:
        workout = workouts[training_type][target_muscle][fitness_level]
    
    random.shuffle(workout)

    if add_extras != "None":
        workout.extend(random.sample(extra_workouts[add_extras], 2))

    return workout

st.title("Hypertrophy Workout Generator")

training_type = st.selectbox("Choose a training type:", ["split", "full_body"])
if training_type == "split":
    target_muscle = st.selectbox("Choose a target muscle:", ["chest", "back", "quads", "hamstrings", "biceps", "triceps", "shoulders", "calves"])
else:
    target_muscle = "all"
fitness_level = st.selectbox("Choose your fitness level:", ["beginner", "intermediate", "advanced"])
add_extras = st.selectbox("Add extra exercises (optional):", ["None", "triceps", "biceps", "core"])

# ... (rest of the code remains the same)

if st.button("Generate Workout", key="generate_workout"):
    workout = generate_workout(training_type, target_muscle, fitness_level, add_extras)
    st.write(f"Your {training_type} workout for {target_muscle} (Fitness Level: {fitness_level.capitalize()}):")
    for exercise, sets, reps in workout:
        st.write(f"{exercise}: {sets} sets x {reps} reps")

# ... (rest of the code remains the same)

# Main workout generator code
# ... (rest of the workout generator code)

import streamlit as st
import random
import time

# ... (rest of the code remains the same)

# Main workout generator code
# ... (rest of the workout generator code)

BEEP_SOUND_SCRIPT = '''
<script>
async function playBeep() {
    const context = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = context.createOscillator();
    const gainNode = context.createGain();

    oscillator.connect(gainNode);
    gainNode.connect(context.destination);

    oscillator.type = 'sine';
    oscillator.frequency.value = 440;
    gainNode.gain.setValueAtTime(1, context.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.001, context.currentTime + 0.5);

    oscillator.start(context.currentTime);
    oscillator.stop(context.currentTime + 0.5);
}

function updateTimer() {
    window.timerId = setInterval(function() {
        let timeRemaining = parseInt(document.getElementById('timeRemaining').innerText);
        if (timeRemaining > 0) {
            document.getElementById('timeRemaining').innerText = timeRemaining - 1;
        } else {
            clearInterval(window.timerId);
            playBeep();
        }
    }, 1000);
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


# ... (rest of the code remains the same)



st.sidebar.title("Additional Information")
page = st.sidebar.selectbox("Choose a topic:", ["None", "Hypertrophy Training Tips", "Supplements", "How to Use the App"])

if page == "Hypertrophy Training Tips":
    st.sidebar.header("Hypertrophy Training Tips")
    st.sidebar.subheader("Reps and Intensity")
    st.sidebar.write("""
    - Use a weight that is around 65-85% of your 1RM for each exercise.
    - Perform reps at a controlled pace, e.g., 2 seconds for lifting, 1 second pause, 2 seconds for lowering.
    - Train close to failure, but not necessarily to absolute failure on each set.
    """)

    st.sidebar.subheader("Diet")
    st.sidebar.write("""
    - Consume a calorie surplus to support muscle growth.
    - Aim for 1.6-2.2 grams of protein per kilogram of body weight daily.
    - Maintain a balanced intake of carbohydrates, fats, and micronutrients.
    """)

    st.sidebar.subheader("Split Training")
    st.sidebar.write("""
    - Split training allows you to focus on specific muscle groups in each session.
    - Common split routines include upper/lower, push/pull/legs, and body part-specific splits.
    - Ensure adequate rest and recovery between sessions targeting the same muscle group.
    """)
elif page == "Supplements":
    st.sidebar.header("Supplements for Hypertrophy")
    st.sidebar.write("""
    Here are some supplements that may help support muscle growth and hypertrophy:

    1. **Protein powder**: Helps to meet daily protein requirements and provides the building blocks for muscle growth.
    2. **Creatine**: Increases strength and power output, allowing for more intense workouts and faster muscle growth.
    3. **Beta-Alanine**: Improves endurance and may help increase muscle mass in combination with resistance training.
    4. **Branched-Chain Amino Acids (BCAAs)**: May help reduce muscle breakdown and promote recovery.
    5. **Fish oil**: Rich in omega-3 fatty acids, which can support muscle growth and overall health.
    """)
elif page == "How to Use the App":
    st.sidebar.header("How to Use the App")
    st.sidebar.write("""
    Follow these steps to generate a workout for hypertrophy:

    1. Choose a training type: 'split' or 'full_body'.
    2. If 'split' is selected, choose the target muscle group.
    3. Choose your fitness level: 'beginner', 'intermediate', or 'advanced'.
    4. Optionally, add extra triceps, biceps, or core exercises using the select box.
    5. Click 'Generate Workout' to create a customized workout.
    6. Adjust the rest time between sets using the slider.
    7. Click 'Start Workout Timer' to begin the timer for your workout.
    8. Perform the exercises as displayed, following the sets and reps suggested.
    9. Prioritize proper form and technique for each exercise.
    """)
