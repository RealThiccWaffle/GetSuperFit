import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from streamlit_extras.stateful_button import button
import random
import pandas as pd
import Datalist


#----------------workoutGenerator Function---------------------
user_name = "none"
def workoutGenerator(ex1, ex2, ex3, ex4, workout_Type, numOfset):
    a = numOfset
    if a == 2:
        ex1, ex2 = random.sample(workout_Type, 2)
    if a == 3:
        ex1, ex2, ex3 = random.sample(workout_Type, 3)
    elif a == 4:
        ex1, ex2, ex3, ex4 = random.sample(workout_Type, 4)
    return ex1, ex2, ex3, ex4
def workoutGenerator2(finalResults, NumOfset3):
            num1 = ""
            num2 = ""
            num3 = ""
            num4 = ""
            num1, num2, num3, num4 = workoutGenerator(num1, num2, num3, num4, finalResults, NumOfset3)
            st.write(num1)
            st.write(num2)
            st.write(num3)
            st.write(num4)
            wwwwwwwwwwwww = 1
#--------------------List----------------------------
#$$$$$$$$$$$$$$$$$$$$CHEST$$$$$$$$$$$$$$$$$$$$$$$$$$$$
chest_Hpypertrophy_Beginner = ["a1", "b2", "c3", "d4","a5", "b6", "c7", "d8"]
chest_Hpypertrophy_Beginner2 = ["a", "b", "c", "d","a", "b", "c", "d"]
chest_Hpypertrophy_Intermediate = ["a", "b", "c", "d","a", "b", "c", "d"]
chest_Hpypertrophy_Intermediate2 = ["a", "b", "c", "d","a", "b", "c", "d"]
chest_Hpypertrophy_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Hpypertrophy_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Strength_Beginner = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Strength_Beginner2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Strength_Intermediate = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Strength_Intermediate2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Strength_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Strength_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Endurance_Beginner = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Endurance_Beginner2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Endurance_Intermediate = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Endurance_Intermediate2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Endurance_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
chest_Endurance_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
#$$$$$$$$$$$$$$$$$$$$BACK/SHOULDER$$$$$$$$$$$$$$$$$$$$$$$$$$$$
back_shoulder_Hpypertrophy_Beginner = ["a", "b", "c", "d","a", "b", "c", "d"]
back_shoulder_Hpypertrophy_Beginner2 = ["a", "b", "c", "d","a", "b", "c", "d"]
back_shoulder_Hpypertrophy_Intermediate = ["a", "b", "c", "d","a", "b", "c", "d"]
back_shoulder_Hpypertrophy_Intermediate2 = ["a", "b", "c", "d","a", "b", "c", "d"]
back_shoulder_Hpypertrophy_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Hpypertrophy_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Strength_Beginner = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Strength_Beginner2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Strength_Intermediate = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Strength_Intermediate2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Strength_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Strength_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Endurance_Beginner = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Endurance_Beginner2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Endurance_Intermediate = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Endurance_Intermediate2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Endurance_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
back_shoulder_Endurance_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
#$$$$$$$$$$$$$$$$$$$$Leg$$$$$$$$$$$$$$$$$$$$$$$$$$$$
leg_Hpypertrophy_Beginner = ["a", "b", "c", "d","a", "b", "c", "d"]
leg_Hpypertrophy_Beginner2 = ["a", "b", "c", "d","a", "b", "c", "d"]
leg_Hpypertrophy_Intermediate = ["a", "b", "c", "d","a", "b", "c", "d"]
leg_Hpypertrophy_Intermediate2 = ["a", "b", "c", "d","a", "b", "c", "d"]
leg_Hpypertrophy_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Hpypertrophy_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Strength_Beginner = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Strength_Beginner2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Strength_Intermediate = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Strength_Intermediate2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Strength_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Strength_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Endurance_Beginner = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Endurance_Beginner2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Endurance_Intermediate = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Endurance_Intermediate2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Endurance_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
leg_Endurance_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
#$$$$$$$$$$$$$$$$$$$$Arm$$$$$$$$$$$$$$$$$$$$$$$$$$$$
arm_Hpypertrophy_Beginner = ["a", "b", "c", "d","a", "b", "c", "d"]
arm_Hpypertrophy_Beginner2 = ["a", "b", "c", "d","a", "b", "c", "d"]
arm_Hpypertrophy_Intermediate = ["a", "b", "c", "d","a", "b", "c", "d"]
arm_Hpypertrophy_Intermediate2 = ["a", "b", "c", "d","a", "b", "c", "d"]
arm_Hpypertrophy_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Hpypertrophy_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Strength_Beginner = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Strength_Beginner2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Strength_Intermediate = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Strength_Intermediate2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Strength_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Strength_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Endurance_Beginner = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Endurance_Beginner2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Endurance_Intermediate = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Endurance_Intermediate2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Endurance_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
arm_Endurance_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
#$$$$$$$$$$$$$$$$$$$$Core$$$$$$$$$$$$$$$$$$$$$$$$$$$$
core_Hpypertrophy_Beginner = ["a", "b", "c", "d","a", "b", "c", "d"]
core_Hpypertrophy_Beginner2 = ["a", "b", "c", "d","a", "b", "c", "d"]
core_Hpypertrophy_Intermediate = ["a", "b", "c", "d","a", "b", "c", "d"]
core_Hpypertrophy_Intermediate2 = ["a", "b", "c", "d","a", "b", "c", "d"]
core_Hpypertrophy_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Hpypertrophy_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Strength_Beginner = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Strength_Beginner2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Strength_Intermediate = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Strength_Intermediate2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Strength_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Strength_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Endurance_Beginner = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Endurance_Beginner2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Endurance_Intermediate = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Endurance_Intermediate2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Endurance_Advanced = ["a", "b", "c", "d", "a", "b", "c", "d"]
core_Endurance_Advanced2 = ["a", "b", "c", "d", "a", "b", "c", "d"]
#-----------------SideBar---------------------------------------
user_name = "no"
x = False
y = "no"
z = "no"
typeOfEx = "no"
with st.sidebar.form(key='my_form'):
    user_name = st.text_input("Usrename")
    st.form_submit_button("Login")

if user_name != "Admin":
    x = st.sidebar.selectbox("Navigation Tool", ["Home", "Workouts"])
else:
    x = st.sidebar.selectbox("Navigation Tool", ["Home", "Workouts", "Admin Control"])
if user_name == "Admin":
    if x == "Admin Control":
        with st.sidebar:
            selected = option_menu(
                menu_title= "ADMIN CONTROL",
                options= ["Add Users","Add exercises", "Admin Settings"]
                    )
    if x == "Home":
        with st.sidebar:
            selected = option_menu(
                menu_title= "HOME",
                options= ["Home Page", "My Account", "My Data", "Settings", "About"]
                    )
    if x == "Workouts":
        with st.sidebar:
            selected = option_menu(
                menu_title= "WORKOUTS",
                options= ["Training Guide", "Chest Day", "Back/Shoulder Day", "Leg Day", "Arm Day", "Core Day"]
                )
if user_name != "Admin":
    if x == "Home":
        with st.sidebar:
            selected = option_menu(
                menu_title= "HOME",
                options= ["Home Page", "My Account", "My Data", "Settings", "About"]
                    )
    if x == "Workouts":
        with st.sidebar:
            selected = option_menu(
                menu_title= "WORKOUTS",
                options= ["Training Guide", "Chest Day", "Back/Shoulder Day", "Leg Day", "Arm Day", "Core Day"]
                )
    typeOfEx = "Home"
    resultOfChoices = ""
if selected == "Training Guide":
    typeOfEx = "Training Guide"
    """
    #       WORDS!!!!!
    """
if selected == "Home Page":
    typeOfEx = "Home Page"
    st.title("Welcome to the home page")
if selected == "Chest Day":
    st.title("Lets build a chest workout")
    typeOfEx = "chest"
if selected == "Back/Shoulder Day":
    st.title("Lets build a back/shoulder workout")
    typeOfEx = "back_shoulder"
if selected == "Leg Day":
    st.title("Lets build a leg workout")
    typeOfEx = "leg"
if selected == "Arm Day":
    st.title("Lets build a arm workout")
    typeOfEx = "arm"
if selected == "Core Day":
    st.title("Lets build a core workout")
    typeOfEx = "core"
if selected == "My Data":
    st.title("Your personal Data")
    typeOfEx = "My Data"
####################################################################
if typeOfEx == "Home Page":
    """
    #    WELCOME TO THE GET SUPER FIT APP
    #  Use this app to help you get fit!
    
    # About the App
    This app generates workouts base on what you, the user, inputs. On the sidebar, there are options that correlate to different days which they should be performed on.
    If the user/you clicks on Chest, in the sidebar, it will only generate exercises for chest.
    """
    if user_name != "":
        st.write("Hello "+user_name)
if typeOfEx == "My Data":
    #if user_name != "no":
    st.write("Hello "+user_name) 
if typeOfEx != "My Data":
    if x != "Home":
        if typeOfEx != "Training Guide":
            if x != "Admin Control":
                def exersizeChoice(HyperChoice, StrenChoice, EndurChoice, TypeOfChoice1):
                    tyz = st.selectbox("Please choose what kind of trying you want", ("None", "Hypertrophy", "Strength", "Endurance"))
                    if tyz == "Hypertrophy":
                        HyperChoice = HyperChoice + " Hypertrophy"
                        TypeOfChoice1 = TypeOfChoice1 + "Hypertrophy"
                        st.write("Hypertrophy is if your goal is to gain muscle mass")
                    elif tyz == "Strength":
                        StrenChoice = StrenChoice + "Strength"
                        TypeOfChoice1 = TypeOfChoice1 + "Strength"
                        st.write("Strength is for those you want to get stronger with current muscle mass they have")
                    elif tyz == "Endurance":
                        EndurChoice = EndurChoice + "Endurance"
                        TypeOfChoice1 = TypeOfChoice1 + "Endurance"
                        st.write("Endurance is for those who want to be able to repeat a physical movement in large amount of reps")
                    else:
                        st.write("description")
                    return HyperChoice, StrenChoice, EndurChoice, TypeOfChoice1


    #---------------2nd Parameter Function----------------
                def exersizeChoice2(BegChoice, InterChoice, AdvChoice, TypeOfChoice2):
                    xyt = st.selectbox("Please select your fitness level", ("None", "Beginner", "Intermediate", "Advanced"))
                    if xyt == "Beginner":
                        BegChoice = BegChoice + "Beginner"
                        TypeOfChoice2 = TypeOfChoice2 + "Beginner"
                        st.write("Beginner is a perfect fit if you starting or getting back to fitness!")
                    elif xyt == "Intermediate":
                        InterChoice = InterChoice + "Intermediate"
                        TypeOfChoice2 = TypeOfChoice2 + "Intermediate"
                        st.write("Intermediate is perfect if you need to up it from beginner!")
                    elif xyt == "Advanced":
                        AdvChoice = AdvChoice + "Advanced"
                        TypeOfChoice2 = TypeOfChoice2 + "Advanced"
                        st.write("Advanced is for those who want a good pump!")
                    else:
                        st.write("description")
                    return BegChoice, InterChoice, AdvChoice, TypeOfChoice2
                if typeOfEx != "Training Guide":
                    choice1 = "yes"
                    choice2 = "yes"
                    choice3 = "yes"
                    choice4 = "_"
                    HyperChoice, StrenChoice, EndurChoice, TypeOfChoice1 = exersizeChoice(choice1, choice2, choice3, choice4)
                    BegChoice, interChoice, advChoice, TypeOfChoice2 = exersizeChoice2(choice1, choice2, choice3, choice4)
                    numOfSet1 = 0
                    numOfSet2 = 0
                    if BegChoice == "yesBeginner":
                        numOfSet1 = 2
                        numOfSet2 = 2
                    if interChoice == "yesIntermediate":
                        numOfSet1 = 3
                        numOfSet2 = 3
                    if advChoice == "yesAdvanced":
                        numOfSet1 = 4
                        numOfSet2 = 4
                    resultOfChoices = resultsOfButtons(typeOfEx, TypeOfChoice1, TypeOfChoice2, resultOfChoices)
        
            #-------------------------------------------------chest Hyper
    if x != "Home":
        if typeOfEx != "Training Guide":
            if x != "bobbbbbb":
                if resultOfChoices == "chest_Hypertrophy_Beginner":
                    st.write("Main lifts")
                    workoutGenerator2(chest_Hpypertrophy_Beginner, numOfSet1)
                    st.write("Secondary lifts")
                    workoutGenerator2(chest_Hpypertrophy_Beginner2, numOfSet2)
                if resultOfChoices == "chest_Hypertrophy_Intermediate":
                    workoutGenerator2(chest_Hpypertrophy_Intermediate, numOfSet1)
                    workoutGenerator2(chest_Hpypertrophy_Intermediate2, numOfSet2)
                if resultOfChoices == "chest_Hypertrophy_Advanced":
                    workoutGenerator2(chest_Hpypertrophy_Advanced, numOfSet1)
                    workoutGenerator2(chest_Hpypertrophy_Advanced2, numOfSet2)
                    #-------------------------------------------------chest Strength
                if resultOfChoices == "chest_Strength_Beginner":
                    workoutGenerator2(chest_Strength_Beginner, numOfSet1)
                    workoutGenerator2(chest_Strength_Beginner2, numOfSet2)
                if resultOfChoices == "chest_Strength_Intermediate":
                    workoutGenerator2(chest_Strength_Intermediate, numOfSet1)
                    workoutGenerator2(chest_Strength_Intermediate2, numOfSet2)
                if resultOfChoices == "chest_Strength_Advanced":
                    workoutGenerator2(chest_Strength_Advanced, numOfSet1)
                    workoutGenerator2(chest_Strength_Advanced2, numOfSet2)
                    #-------------------------------------------------chest Ender
                if resultOfChoices == "chest_Endurance_Beginner":
                    workoutGenerator2(chest_Endurance_Beginner, numOfSet1)
                    workoutGenerator2(chest_Endurance_Beginner2, numOfSet2)
                if resultOfChoices == "chest_Endurance_Intermediate":
                    workoutGenerator2(chest_Endurance_Intermediate, numOfSet1)
                    workoutGenerator2(chest_Endurance_Intermediate2, numOfSet2)
                if resultOfChoices == "chest_Endurance_Advanced":
                    workoutGenerator2(chest_Endurance_Advanced, numOfSet1)
                    workoutGenerator2(chest_Endurance_Advanced2, numOfSet2)
                    #####################################################################

                    #####################################################################

                    #####################################################################
                    #-------------------------------------------------back/shoulder Hyper
                if resultOfChoices == "back_shoulder_Hypertrophy_Beginner":
                    workoutGenerator2(back_shoulder_Hpypertrophy_Beginner, numOfSet1)
                    workoutGenerator2(back_shoulder_Hpypertrophy_Beginner2, numOfSet2)
                if resultOfChoices == "back_shoulder_Hypertrophy_Intermediate":
                    workoutGenerator2(back_shoulder_Hpypertrophy_Intermediate, numOfSet1)
                    workoutGenerator2(back_shoulder_Hpypertrophy_Intermediate2, numOfSet2)
                if resultOfChoices == "back_shoulder_Hypertrophy_Advanced":
                    workoutGenerator2(back_shoulder_Hpypertrophy_Advanced, numOfSet1)
                    workoutGenerator2(back_shoulder_Hpypertrophy_Advanced2, numOfSet2)
                    #-------------------------------------------------back/shoulder Strength
                if resultOfChoices == "back_shoulder_Strength_Beginner":
                    workoutGenerator2(back_shoulder_Strength_Beginner, numOfSet1)
                    workoutGenerator2(back_shoulder_Strength_Beginner2, numOfSet2)
                if resultOfChoices == "back_shoulder_Strength_Intermediate":
                    workoutGenerator2(back_shoulder_Strength_Intermediate, numOfSet1)
                    workoutGenerator2(back_shoulder_Strength_Intermediate2, numOfSet2)
                if resultOfChoices == "back_shoulder_Strength_Advanced":
                    workoutGenerator2(back_shoulder_Strength_Advanced, numOfSet1)
                    workoutGenerator2(back_shoulder_Strength_Advanced2, numOfSet2)
                    #-------------------------------------------------back/shoulder Ender 
                if resultOfChoices == "back_shoulder_Endurance_Beginner":
                    workoutGenerator2(back_shoulder_Endurance_Beginner, numOfSet1)
                    workoutGenerator2(back_shoulder_Endurance_Beginner2, numOfSet2)
                if resultOfChoices == "back_shoulder_Endurance_Intermediate":
                    workoutGenerator2(back_shoulder_Endurance_Intermediate, numOfSet1)
                    workoutGenerator2(back_shoulder_Endurance_Intermediate2, numOfSet2)
                if resultOfChoices == "back_shoulder_Endurance_Advanced":
                    workoutGenerator2(back_shoulder_Endurance_Advanced, numOfSet1)
                    workoutGenerator2(back_shoulder_Endurance_Advanced2, numOfSet2)
                    #####################################################################

                    #####################################################################

                    #####################################################################
                    #-------------------------------------------------leg Hyper
                if resultOfChoices == "leg_Hypertrophy_Beginner":
                    workoutGenerator2(leg_Hpypertrophy_Beginner, numOfSet1)
                    workoutGenerator2(leg_Hpypertrophy_Beginner2, numOfSet2)
                if resultOfChoices == "leg_Hypertrophy_Intermediate":
                    workoutGenerator2(leg_Hpypertrophy_Intermediate, numOfSet1)
                    workoutGenerator2(leg_Hpypertrophy_Intermediate2, numOfSet2)
                if resultOfChoices == "leg_Hypertrophy_Advanced":
                    workoutGenerator2(leg_Hpypertrophy_Advanced, numOfSet1)
                    workoutGenerator2(leg_Hpypertrophy_Advanced2, numOfSet2)
                    #-------------------------------------------------leg Strength
                if resultOfChoices == "leg_Strength_Beginner":
                    workoutGenerator2(leg_Strength_Beginner, numOfSet1)
                    workoutGenerator2(leg_Strength_Beginner2, numOfSet2)
                if resultOfChoices == "leg_Strength_Intermediate":
                    workoutGenerator2(leg_Strength_Intermediate, numOfSet1)
                    workoutGenerator2(leg_Strength_Intermediate2, numOfSet2)
                if resultOfChoices == "leg_Strength_Advanced":
                    workoutGenerator2(leg_Strength_Advanced, numOfSet1)
                    workoutGenerator2(leg_Strength_Advanced2, numOfSet2)
                    #-------------------------------------------------leg Ender 
                if resultOfChoices == "leg_Endurance_Beginner":
                    workoutGenerator2(leg_Endurance_Beginner, numOfSet1)
                    workoutGenerator2(leg_Endurance_Beginner2, numOfSet2)
                if resultOfChoices == "leg_Endurance_Intermediate":
                    workoutGenerator2(leg_Endurance_Intermediate, numOfSet1)
                    workoutGenerator2(leg_Endurance_Intermediate2, numOfSet2)
                if resultOfChoices == "leg_Endurance_Advanced":
                    workoutGenerator2(leg_Endurance_Advanced, numOfSet1)
                    workoutGenerator2(leg_Endurance_Advanced2, numOfSet2)
                    #####################################################################

                    #####################################################################

                    #####################################################################
                    #-------------------------------------------------arm Hyper
                if resultOfChoices == "arm_Hypertrophy_Beginner":
                    workoutGenerator2(arm_Hpypertrophy_Beginner, numOfSet1)
                    workoutGenerator2(arm_Hpypertrophy_Beginner2, numOfSet2)
                if resultOfChoices == "arm_Hypertrophy_Intermediate":
                    workoutGenerator2(arm_Hpypertrophy_Intermediate, numOfSet1)
                    workoutGenerator2(arm_Hpypertrophy_Intermediate2, numOfSet2)
                if resultOfChoices == "arm_Hypertrophy_Advanced":
                    workoutGenerator2(arm_Hpypertrophy_Advanced, numOfSet1)
                    workoutGenerator2(arm_Hpypertrophy_Advanced2, numOfSet2)
                    #-------------------------------------------------arm Strength
                if resultOfChoices == "arm_Strength_Beginner":
                    workoutGenerator2(arm_Strength_Beginner, numOfSet1)
                    workoutGenerator2(arm_Strength_Beginner2, numOfSet2)
                if resultOfChoices == "arm_Strength_Intermediate":
                    workoutGenerator2(arm_Strength_Intermediate, numOfSet1)
                    workoutGenerator2(arm_Strength_Intermediate2, numOfSet2)
                if resultOfChoices == "arm_Strength_Advanced":
                    workoutGenerator2(arm_Strength_Advanced, numOfSet1)
                    WorkoutGenerator2(arm_Strength_Advanced2, numOfSet2)
                    #-------------------------------------------------arm Ender 
                if resultOfChoices == "arm_Endurance_Beginner":
                    workoutGenerator2(arm_Endurance_Beginner, numOfSet1)
                    workoutGenerator2(arm_Endurance_Beginner2, numOfSet2)
                if resultOfChoices == "arm_Endurance_Intermediate":
                    workoutGenerator2(arm_Endurance_Intermediate, numOfSet1)
                    workoutGenerator2(arm_Endurance_Intermediate2, numOfSet2)
                if resultOfChoices == "arm_Endurance_Advanced":
                    workoutGenerator2(arm_Endurance_Advanced, numOfSet1)
                    workoutGenerator2(arm_Endurance_Advanced2, numOfSet2)
                    #####################################################################

                    #####################################################################

                    #####################################################################
                    #-------------------------------------------------core Hyper
                if resultOfChoices == "core_Hypertrophy_Beginner":
                    workoutGenerator2(core_Hpypertrophy_Beginner, numOfSet1)
                    workoutGenerator2(core_Hpypertrophy_Beginner2, numOfSet2)
                if resultOfChoices == "core_Hypertrophy_Intermediate":
                    workoutGenerator2(core_Hpypertrophy_Intermediate, numOfSet1)
                    workoutGenerator2(core_Hpypertrophy_Intermediate2, numOfSet2)
                if resultOfChoices == "core_Hypertrophy_Advanced":
                    workoutGenerator2(core_Hpypertrophy_Advanced, numOfSet1)
                    workoutGenerator2(core_Hpypertrophy_Advanced2, numOfSet2)
                    #-------------------------------------------------core Strength
                if resultOfChoices == "core_Strength_Beginner":
                    workoutGenerator2(core_Strength_Beginner, numOfSet1)
                    workoutGenerator2(core_Strength_Beginner2, numOfSet2)
                if resultOfChoices == "core_Strength_Intermediate":
                    workoutGenerator2(core_Strength_Intermediate, numOfSet1)
                    workoutGenerator2(core_Strength_Intermediate2, numOfSet2)
                if resultOfChoices == "core_Strength_Advanced":
                    workoutGenerator2(core_Strength_Advanced, numOfSet1)
                    workoutGenerator2(core_Strength_Advanced2, numOfSet2)
                    #-------------------------------------------------core Ender 
                if resultOfChoices == "core_Endurance_Beginner":
                    workoutGenerator2(core_Endurance_Beginner, numOfSet1)
                    workoutGenerator2(core_Endurance_Beginner2, numOfSet2)
                if resultOfChoices == "core_Endurance_Intermediate":
                    workoutGenerator2(core_Endurance_Intermediate, numOfSet1)
                    workoutGenerator2(core_Endurance_Intermediate2, numOfSet2)
                if resultOfChoices == "core_Endurance_Advanced":
                    workoutGenerator2(core_Endurance_Advanced, numOfSet1)
                    workoutGenerator2(core_Endurance_Advanced2, numOfSet2)
    #_____________________SIGNIN___________________________________

