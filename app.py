# streamlit 
import streamlit as st 

st.set_page_config(page_title= "Growth-mindset-project", project_icon=" ⭐")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to your Growth journey!")
st.write("🌱 Do not be afraid to grow. Its the only way to find out how strong you really are. Every day is a new beginning. Take a deep breath, smile, and start again.")

# quote section 
st.header("💡Today's Growth Mindset Quote")
st.write("Success is the result of preparation, hard work, and learning from failure. – Colin Powell 🌟")

st.header(" 🌸 What's Your Challenge Today ?")
user_input = st.text_input("Describe a challenge you're facing:")


# condition 

if user_input:
    st.success(f"you're facing: {user_input}.Keep pushing forward towards your goal!🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# reflexing 

st.header("Reflect on Your Learning")
reflection = st.text_area("write your reflection here:")

if reflection:
    st.success(f" ✨ Great insight ! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

# achievements 

st.header("🏆 Celebrate Your Wins!")
achievements = st.text_input("Share something you've recently accomplished:")

if achievements:
    st.success(f"🎉 Amazing! You achieved: {achievements}")
else:
    st.info("Big or Small, every acheivment counts! Share one now 😍")

# footer 

st.write("- - -")
st.write("🌸 Keep believing in yourself. Growth is a journey, not a destination! ✨")
st.write("**⛔ Created by Alishba Ansari**")

