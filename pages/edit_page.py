import streamlit as st
from src.utilities.manager import *
from src.model.Strategy import Strategy
from typing import List

if 'current_id' not in st.session_state:
    st.session_state['current_id'] = '-1'
strategy = get_strategies(id=st.session_state['current_id'])
                
if strategy:
    strategy = Strategy(*strategy)
    dictionary = get_screener_dictionary()

    # basic_1 = st.columns([1,1])
    st.title("Strategy Edit Page")
    # st.text("Welcome Strategy Edit Page")
    st.text(f"Strategy  Name: {strategy.name}")
    st.text(f"Descripstion: {strategy.desc}")

    # column = st.selectbox("Describe Column", list(dataset.columns), format_func=cols.get)

    st.selectbox("Screener: ", dictionary.keys(),format_func=dictionary.get)

    st.selectbox("Trading Style: ", ["Trading Style Name 1", "Trading Style Name 2"])
    st.selectbox("Stopp Loss: ", ["Stopp Loss Name 1", "Stopp Loss Name 2"])

    
    save = st.button("Save")
    reset = st.button("Reset")

