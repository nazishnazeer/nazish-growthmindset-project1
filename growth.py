# streamlit
import streamlit as st

st.set_page_config(page_title='Growth Mind Set Project', page_icon='✨')

st.title('Growth Mindset Challenge : Web App With Streamlit')

st.header('🚀 Welcome To Your Growth Journey')

st.write('Face challenges with confidence, learn from setbacks, and reach your full potential. This AI-powered project helps you develop a growth mindset through self-reflection, exciting challenges, and meaningful achievements..🌟 ')

# quote section
st.header("💡Today's Growth Mindset Quote")
st.write("'It is hard to fail, but it is worse never to have tried to succeed.' Theodore Roosevelt")

st.header("💪What's Your Challenge Today")
user_input = st.text_input('Describe a challenge you are facing :')

# condition
if user_input:
    st.success(f"💪You are facing:{user_input}.Keep looking forward towards your goal🚀")
else:
    st.warning('Tell us about your challenge to get started')

# reflaxing
st.header('reflect on your learning')
reflection = st.text_area('Write your reflections here:')

if reflection:
    st.success(f"✨Great insight! your reflection: {reflection}✨")
else:
    st.info('Growth comes from reflection. Share your difficulties!')

# achievements

st.header('🏆Celebrate your achievements🏆')
achievements= st.text_input('Share you have recently accomplished: ')

if achievements:
    st.success(f"🎉Amazing you achieved: {achievements}")
else:
    st.info('Every achievement matters, big or small! What’s something you’re proud of?😊')

# footer
st.write('- - -')
st.write("Trust yourself growth is a continuous journey, not a final destination. Keep moving forward!")
st.write("""Created by Nazish Nazeer""")