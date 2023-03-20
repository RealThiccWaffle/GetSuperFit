import streamlit as st
import random
import time

def generate_workout(training_type, target_muscle, fitness_level, add_extras):
    workouts = {
        "split": {
            "chest": {
                "beginner": [
                    ("Bench Press", 3, 10),
                    ("Incline Dumbbell Press", 3, 10),
                    ("Chest Fly", 3, 10),
                ],
                "intermediate": [
                    ("Bench Press", 4, 8),
                    ("Incline Dumbbell Press", 4, 8),
                    ("Chest Fly", 4, 8),
                ],
                "advanced": [
                    ("Bench Press", 5, 6),
                    ("Incline Dumbbell Press", 5, 6),
                    ("Chest Fly", 5, 6),
                ],
            },
            "back": {
                "beginner": [
                    ("Deadlift", 3, 10),
                    ("Bent Over Row", 3, 10),
                    ("Lat Pulldown", 3, 10),
                ],
                "intermediate": [
                    ("Deadlift", 4, 8),
                    ("Bent Over Row", 4, 8),
                    ("Lat Pulldown", 4, 8),
                ],
                "advanced": [
                    ("Deadlift", 5, 6),
                    ("Bent Over Row", 5, 6),
                    ("Lat Pulldown", 5, 6),
                ],
            },
            # Add other muscle groups here in a similar format
        },
        "full_body": {
            "all": {
                "beginner": [
                    ("Bench Press", 3, 10),
                    ("Deadlift", 3, 10),
                    ("Squat", 3, 10),
                ],
                "intermediate": [
                    ("Bench Press", 4, 8),
                    ("Deadlift", 4, 8),
                    ("Squat", 4, 8),
                ],
                "advanced": [
                    ("Bench Press", 5, 6),
                    ("Deadlift", 5, 6),
                    ("Squat", 5, 6),
                ],
            }
        }
    }

    extra_workouts = {
        "triceps": [
            ("Triceps Dips", 3, 10),
            ("Skull Crushers", 3, 10),
        ],
        "biceps": [
            ("Bicep Curls", 3, 10),
            ("Hammer Curls", 3, 10),
        ],
        "core": [
            ("Plank", 3, "60s"),
            ("Crunches", 3, 15),
        ],
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
    target_muscle = st.selectbox("Choose a target muscle:", ["chest", "back"])
else:
    target_muscle = "all"
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
    const synth = new Tone.Synth().toDestination();

    function playBeep() {
        synth.triggerAttackRelease("C4", "8n");
    }

    function updateTimer() {
        const timeRemainingElement = document.getElementById("timeRemaining");
        const timeRemaining = parseInt(timeRemainingElement.innerText, 10);
        if (timeRemaining > 0) {
            timeRemainingElement.innerText = (timeRemaining - 1).toString();
            setTimeout(updateTimer, 1000);
            if (timeRemaining === 1) {
                playBeep();
            }
        }
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
    st.header("Generated Workout")
    workout = generate_workout(training_type, target_muscle, fitness_level, add_extras)

    for index, (exercise, sets, reps) in enumerate(workout):
        st.subheader(f"{index + 1}. {exercise}")
        st.write(f"Sets: {sets}")
        st.write(f"Reps: {reps}")

st.sidebar.title("Additional Information")
page = st.sidebar.selectbox("Choose a topic:", ["None", "Hypertrophy Training Tips", "Supplements", "How to Use the App"])

if page == "Hypertrophy Training Tips":
    st.sidebar.header("Hypertrophy Training Tips")
    st.sidebar.subheader("Reps and Intensity")
    st.sidebar.write("""
    To promote hypertrophy, aim for a rep range of 8-12 repetitions per set. This range has been shown to be effective for muscle growth. Adjust the weight used so that you can complete the given number of reps with good form while still challenging your muscles.
    """)

    st.sidebar.subheader("Diet")
    st.sidebar.write("""
    To support muscle growth, ensure that you're consuming enough protein and overall calories. A general guideline is to consume about 1g of protein per pound of body weight daily. Additionally, eat a mix of carbohydrates and healthy fats to fuel your workouts and recovery.
    """)

    st.sidebar.subheader("Split Training")
    st.sidebar.write("""
    Split training involves dividing your workouts to focus on specific muscle groups during each session. This allows you to train each muscle group with greater intensity and volume, which can help stimulate muscle growth. Common split routines include upper/lower, push/pull, and body part splits.
    """)

elif page == "Supplements":
    st.sidebar.header("Supplements")
    st.sidebar.subheader("Protein Powder")
    st.sidebar.write("""
    Protein powder can be a convenient way to increase your daily protein intake, especially if you struggle to get enough protein from whole foods. Common types of protein powder include whey, casein, and plant-based options like soy, pea, and rice protein.
    """)

    st.sidebar.subheader("Creatine")
    st.sidebar.write("""
    Creatine is a popular supplement that can help improve strength, power, and muscle mass. It works by increasing your muscles' stores of creatine phosphate, which is used to produce energy for high-intensity exercise. To supplement with creatine, start with a loading phase of 20g per day for 5-7 days, followed by a maintenance phase of 3-5g per day.
    """)

    st.sidebar.subheader("BCAAs")
    st.sidebar.write("""
    Branched-chain amino acids (BCAAs) are a group of three essential amino acids: leucine, isoleucine, and valine. They can help promote muscle protein synthesis and reduce muscle breakdown during exercise. BCAAs can be taken before, during, or after your workout to support muscle recovery and growth.
    """)

elif page == "How to Use the App":
    st.sidebar.header("How to Use the App")
    st.sidebar.write("""
    1. Select the training type (split or full body) from the dropdown menu.
    2. If you choose 'split', select the target muscle group you'd like to focus on.
    3. Choose your fitness level (beginner, intermediate, or advanced).
    4. Optionally, add extra exercises to your workout.
    5. Click the 'Generate Workout' button to create your custom workout.
    6. The generated workout will appear on the main screen with the exercises, sets, and reps.
    7. Use the 60-second timer to time your rest periods between sets.
    8. Explore the sidebar for additional information on hypertrophy training tips, supplements, and how to use the app.
    """)
