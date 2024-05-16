import streamlit as st
from src.utilities.manager import get_strategies
def screening_page():
    st.header('Screening page')
    # st.text("Screener: ")
    screener = st.selectbox('Screener: ',["ya", "Tidak"])

    st.button
        