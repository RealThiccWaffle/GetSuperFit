import streamlit as st
import random
import time

def generate_workout(training_type, target_muscle, fitness_level, add_extras):
    # ... (rest of the workout generator code)

st.title("Hypertrophy Workout Generator")

training_type = st.selectbox("Choose a training type:", ["split", "full_body"])
if training_type == "split":
    target_muscle = st.selectbox("Choose a target muscle:", ["chest", "back", "quads", "hamstrings", "biceps", "triceps", "shoulders", "calves"])
else:
    target_muscle = "all"
fitness_level = st.selectbox("Choose your fitness level:", ["beginner", "intermediate", "advanced"])
add_extras = st.selectbox("Add extra exercises (optional):", ["None", "triceps", "biceps", "core"])

# Add Tone.js library
st.markdown(
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.26/Tone.js" integrity="sha512-OoyvPgCQx/0kNNF8iNtJwvSggSAsKA16mSfY2QlySt+D4ypx/JtI3qy8fdz4pSqss5r5yD3qFoX9DTygr13rDg==" crossorigin="anonymous"></script>',
    unsafe_allow_html=True,
)

# Beep sound script
BEEP_SOUND_SCRIPT = '''
<script>
async function playBeep() {
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("C5", "8n");
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

if st.button("Generate Workout"):
    workout = generate_workout(training_type, target_muscle, fitness_level, add_extras)
    for exercise, sets, reps in workout:
        st.write(f"{exercise}: {sets} sets of {reps} reps")

# Sidebar content
st.sidebar.title("Additional Information")
page = st.sidebar.selectbox("Choose a topic:", ["None", "Hypertrophy Training Tips", "Supplements", "How to Use the App"])

# ... (rest of the sidebar content)


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
