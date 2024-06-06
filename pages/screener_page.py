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
            
    if st.button('Add Screener'):
        add_default_screener()

def sidebar_selection():
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)


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

if __name__ == '__main__':
    display_screener_page()
    sidebar_selection()
# display_screener_page()
