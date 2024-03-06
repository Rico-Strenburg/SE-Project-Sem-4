import streamlit as st
from model.Strategy import Strategy

strategies = []
index = 1

# def init_session_state():
#     if 'current_strategy' not in st.session_state:
#         st.session_state.current_strategy = None
#         st.session_state.edit_mode = False

def add_default_strategy():
    global index
    name = "Strategy_name_" + str(index)
    desc = "New Strategy you created"
    new_strat = Strategy(index, name, desc)
    index+=1
    strategies.append(new_strat)
    st.rerun()

def delete_strategy(strategy_id):
    global strategies
    st.write(strategy_id)
    strategies = [strat for strat in strategies if strat.id != strategy_id]




def display_edit_page(strategy):
    new_name = st.text_input('New Name:', strategy.name)
    new_desc = st.text_area('New Description:', strategy.desc)
    strategy.name = new_name
    strategy.desc = new_desc

def display_strategy_page():
    st.title('Strategy Page')
    st.write('Your Strategies : ')

    for strategy in strategies:
        with st.expander(strategy.name):
            st.write("Description : " + strategy.desc)
            st.write("Last Modified : " + strategy.modified)
            col1, col2 = st.columns(2)
            edit_button_id = f"edit_strategy_{strategy.id}"
            delete_button_id = f"delete_strategy_{strategy.id}"

            # Add buttons to each column
            with col1:
                edit_button = st.button('Edit', key=edit_button_id)
            with col2:
                delete_button = st.button('Delete', key=delete_button_id)
            
            if edit_button:
                pass
                
            if delete_button:
                delete_strategy(strategy.id)
                st.rerun()


    if st.button('Add Strategy'):
        add_default_strategy()

