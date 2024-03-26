import streamlit as st
from src.utilities.manager import delete_strategy, insert_new_strategy, get_strategies, update_strategy
from src.model.Strategy import Strategy

def add_default_strategy():
    insert_new_strategy()
    st.rerun()

def display_strategy_page():
    strategies = get_strategies()
    st.title('Strategy Page')
    st.write('Your Strategies : ')

    for strategy in strategies:
        with st.expander(strategy.name):
            st.write("Description : " + strategy.desc)
            col1, col2 = st.columns(2)
            edit_button_id = f"edit_strategy_{strategy.id}"
            delete_button_id = f"delete_strategy_{strategy.id}"

            # Add buttons to each column
            with col1:
                edit_button = st.button('Edit', key=edit_button_id)
            with col2:
                delete_button = st.button('Delete', key=delete_button_id)
        
        #Redirect to edit page
        if edit_button:
            st.session_state['current_id'] = strategy.id
            st.switch_page("pages/edit_page.py")
        
        #Delete selected strategy
        if delete_button:
            delete_strategy(strategy.id)
            st.rerun()
            
    if st.button('Add Strategy'):
        add_default_strategy()

