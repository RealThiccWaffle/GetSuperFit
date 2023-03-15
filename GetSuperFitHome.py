import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from streamlit_extras.stateful_button import button
import random
import pandas as pd

#----------------workoutGenerator Function---------------------
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
            
            If NumOfset3 = 2:
                st.write(num1)
                st.write(num2)
                st.write(num3)
            #st.write(num3)
            #st.write(num4)
def resultsOfButtons(type1, type2, type3, type4):
            type4 = type1 + type2 + type3
            return type4
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
with st.sidebar:
    selected = option_menu(
        menu_title= "Main Menu",
        options= ["Home", "Chest Day", "Back/Shoulder Day", "Leg Day", "Arm Day", "Core Day", "My Data"]
    )
    typeOfEx = "Home"
    resultOfChoices = ""
    if selected == "Home":
        st.title("Welcome to the home page")
        typeOfEx = "Home"
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
        typeOfEx = ""
if typeOfEx == "Home":
    """
    #    WELCOME TO THE GET SUPER FIT APP
    #  Use this app to help you get fit!
    
    # About the App
    This app generates workouts base on what you, the user, inputs. On the sidebar, there are options that correlate to different days which they should be performed on.
    If the user/you clicks on Chest, in the sidebar, it will only generate exercises for chest.
    """
if typeOfEx != "Home":
    def exersizeChoice(HyperChoice, StrenChoice, EndurChoice, TypeOfChoice1):
        ex1, ex2, ex3 = st.columns(3)
        xNum1str = "not"
        xNum2str = "not"
        xNum3str = "not"
        xNum4str = ""
        xNum5str = ""
        xNum6str = ""
        with ex1:
            if button("Hpypertrophy", key = "Hpypertrophy") == False:
                xNum4str = xNum1str + " Hpypertrophy" 
        with ex2:
            if button("Strength", key = "Strength") == False:
                xNum5str = xNum2str + " Strength"
        with ex3:
            if button("Endurance", key = "Endurance") == False:
                xNum6str = xNum3str + " Endurance"


        if xNum4str != "not Hpypertrophy" and xNum5str == "not Strength" and xNum6str == "not Endurance":
            HyperChoice = HyperChoice + " Hypertrophy"
            TypeOfChoice1 = TypeOfChoice1 + "Hpypertrophy"
            st.write("Hypertrophy is if your goal is to gain muscle mass")
        elif xNum5str != "not Strength" and xNum4str == "not Hpypertrophy" and xNum6str == "not Endurance":
            StrenChoice = StrenChoice + "strength"
            TypeOfChoice1 = TypeOfChoice1 + "Strength"
            st.write("Strength is for those you want to get stronger with current muscle mass they have")
        elif xNum6str != "not Endurance" and xNum4str == "not Hpypertrophy" and xNum5str == "not Strength":
            EndurChoice = EndurChoice + "Endurance"
            TypeOfChoice1 = TypeOfChoice1 + "Endurance"
            st.write("Endurance is for those who want to be able to repeat a physical movement in large amount of reps") 
        else:
            st.write("please select only one option")
        return HyperChoice, StrenChoice, EndurChoice, TypeOfChoice1


#---------------2nd Parameter Function----------------
    def exersizeChoice2(BegChoice, InterChoice, AdvChoice, TypeOfChoice2):
        ex1, ex2, ex3 = st.columns(3)
        xNum1str = "not"
        xNum2str = "not"
        xNum3str = "not"
        xNum4str = ""
        xNum5str = ""
        xNum6str = ""
        with ex1:
            if button("Beginnrer", key = "Beginner") == False:
                xNum4str = xNum1str + " Beginner"
        with ex2:
            if button("Intermediate", key = "Intermediate") == False:
                xNum5str = xNum2str + " Intermediate"
        with ex3:
            if button("Advanced", key = "Advanced") == False:
                xNum6str = xNum3str + " Advanced"


        if xNum4str != "not Beginner" and xNum5str == "not Intermediate" and xNum6str == "not Advanced":
            BegChoice = BegChoice + "Beginner"
            TypeOfChoice2 = TypeOfChoice2 + "Beginner"
            st.write("Beginner is a perfect fit if you starting or getting back to fitness!")
        elif xNum5str != "not Intermediate" and xNum4str == "not Beginner" and xNum6str == "not Advanced":
            InterChoice = InterChoice + "Intermediate"
            TypeOfChoice2 = TypeOfChoice2 + "Intermediate"
            st.write("Intermediate is perfect if you need to up it from beginner!")
        elif xNum6str != "not Advanced" and xNum4str == "not Beginner" and xNum5str == "not Intermediate":
            AdvChoice = AdvChoice + "Advanced"
            TypeOfChoice2 = TypeOfChoice2 + "Advanced"
            st.write("Advanced is for those who want a good pump!")
        else:
            st.write("please select only one option")
        return BegChoice, InterChoice, AdvChoice, TypeOfChoice2
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
if typeOfEx != "Home" and numOfSet1 != 0:
    if resultOfChoices == "chest_Hpypertrophy_Beginner":
        st.write("Main lifts")
        workoutGenerator2(chest_Hpypertrophy_Beginner, numOfSet1)
        st.write("Secondary lifts")
        workoutGenerator2(chest_Hpypertrophy_Beginner2, numOfSet2)
    if resultOfChoices == "chest_Hpypertrophy_Intermediate":
        workoutGenerator2(chest_Hpypertrophy_Intermediate, numOfSet1)
        workoutGenerator2(chest_Hpypertrophy_Intermediate2, numOfSet2)
    if resultOfChoices == "chest_Hpypertrophy_Advanced":
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
    if resultOfChoices == "back_shoulder_Hpypertrophy_Beginner":
        workoutGenerator2(back_shoulder_Hpypertrophy_Beginner, numOfSet1)
        workoutGenerator2(back_shoulder_Hpypertrophy_Beginner2, numOfSet2)
    if resultOfChoices == "back_shoulder_Hpypertrophy_Intermediate":
        workoutGenerator2(back_shoulder_Hpypertrophy_Intermediate, numOfSet1)
        workoutGenerator2(back_shoulder_Hpypertrophy_Intermediate2, numOfSet2)
    if resultOfChoices == "back_shoulder_Hpypertrophy_Advanced":
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
    if resultOfChoices == "leg_Hpypertrophy_Beginner":
        workoutGenerator2(leg_Hpypertrophy_Beginner, numOfSet1)
        workoutGenerator2(leg_Hpypertrophy_Beginner2, numOfSet2)
    if resultOfChoices == "leg_Hpypertrophy_Intermediate":
        workoutGenerator2(leg_Hpypertrophy_Intermediate, numOfSet1)
        workoutGenerator2(leg_Hpypertrophy_Intermediate2, numOfSet2)
    if resultOfChoices == "leg_Hpypertrophy_Advanced":
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
    if resultOfChoices == "arm_Hpypertrophy_Beginner":
        workoutGenerator2(arm_Hpypertrophy_Beginner, numOfSet1)
        workoutGenerator2(arm_Hpypertrophy_Beginner2, numOfSet2)
    if resultOfChoices == "arm_Hpypertrophy_Intermediate":
        workoutGenerator2(arm_Hpypertrophy_Intermediate, numOfSet1)
        workoutGenerator2(arm_Hpypertrophy_Intermediate2, numOfSet2)
    if resultOfChoices == "arm_Hpypertrophy_Advanced":
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
    if resultOfChoices == "core_Hpypertrophy_Beginner":
        workoutGenerator2(core_Hpypertrophy_Beginner, numOfSet1)
        workoutGenerator2(core_Hpypertrophy_Beginner2, numOfSet2)
    if resultOfChoices == "core_Hpypertrophy_Intermediate":
        workoutGenerator2(core_Hpypertrophy_Intermediate, numOfSet1)
        workoutGenerator2(core_Hpypertrophy_Intermediate2, numOfSet2)
    if resultOfChoices == "core_Hpypertrophy_Advanced":
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
