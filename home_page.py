import streamlit as st

def display_home_page():
    st.title('Home Page')
    
    st.subheader('User Information')
    name = st.text_input('Enter your name', '')
    age = st.slider('Select your age', 0, 100, 25)
    gender = st.selectbox('Select your gender', ['Male', 'Female', 'Other'])

    # Display the submitted information
    st.subheader('Submitted Information')
    st.write(f'Name: {name}')
    st.write(f'Age: {age}')
    st.write(f'Gender: {gender}')