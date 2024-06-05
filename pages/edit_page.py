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

def sidebar_selection():
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

     # Display the selected page
    page = st.sidebar.selectbox(
            'Select a page',
            ('NULL','Home', 'Strategy', 'Screener', 'Backtest', 'Screening')
        )

        # Display the selected page
    if page == 'Home':
        st.switch_page("main.py")
    elif page == 'Strategy':
        st.switch_page("pages/strategy_page.py")
    elif page == 'Screener':
        st.switch_page("pages/screener_page.py")
    elif page == 'Backtest':
        st.switch_page("pages/backtests_page.py")
    elif page == 'Screening':
        st.switch_page("pages/screening_page.py")
    
if __name__ == "__main__":
    sidebar_selection()