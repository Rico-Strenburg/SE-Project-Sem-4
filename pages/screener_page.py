import streamlit as st
from src.utilities.manager import delete_screener, insert_new_screener, get_screener, update_screener
from src.model.Strategy import Strategy


def add_default_strategy():
        insert_new_screener()
        st.rerun()

def display_screener_page():

    screeners = get_screener()
    st.title('Screener Page')
    st.write('Your Screeners :')
    
    
    for strategy in screeners:
        with st.expander(strategy.name):
            st.write("Description : " + strategy.desc)
            # st.write("Stock Universe : " + strategy)
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
            st.switch_page("pages/screening_page.py")
        
        #Delete selected strategy
        if delete_button:
            delete_screener(strategy.id)
            st.rerun()
            
    if st.button('Add Strategy'):
        add_default_strategy()

# if __name__ == '__main__':
#     display_strategy_page()


display_screener_page()