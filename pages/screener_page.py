import streamlit as st
from src.utilities.manager import *
from src.model.Screener import Screener

init_db()
def add_default_screener():
        insert_screener()
        st.rerun()

def display_screener_page():
    screeners = get_screener()
    st.title('Screener Page')
    st.write('Your Screeners :')
    
    for screener in screeners:
        with st.expander(screener.name):
            st.write("Description : " + screener.desc)
            # st.write("Stock Universe : " + strategy)
            col1, col2 = st.columns(2)
            edit_button_id = f"edit_screener_{screener.id}"
            delete_button_id = f"delete_scrneener_{screener.id}"

            # Add buttons to each column
            with col1:
                edit_button = st.button('Edit', key=edit_button_id)
            with col2:
                delete_button = st.button('Delete', key=delete_button_id)
        
        #Redirect to edit page
        if edit_button:
            st.session_state['current_id'] = screener.id
            st.switch_page("pages/screener_edit_page.py")
        
        #Delete selected strategy
        if delete_button:
            delete_screener(screener.id)
            st.rerun()
            
    if st.button('Add Strategy'):
        add_default_screener()

# if __name__ == '__main__':
#     display_screener_page()


display_screener_page()