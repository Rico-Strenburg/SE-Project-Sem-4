import streamlit as st

def display_home_page():
    st.title('Home Page')
    
    st.subheader('User Information')
    with st.form("edit_strategy"):
        st.write("Rate my satisfaction")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")
        new_name = st.text_input('New Name:', "some")
        new_desc = st.text_area('New Description:', "some")

        submit = st.form_submit_button("Submit")

    if submit:
        print(f"{new_name} and {new_desc}")