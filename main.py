
import streamlit as st
import sqlite3
from src.utilities.manager import init_db
# from views.backtests_page import display_backtest_page
# from pages.edit_page import display_edit_page

def connect_to_database():
    conn = sqlite3.connect("novasieve_dev.db")
    return conn

init_db()
conn = connect_to_database()
st.set_page_config(initial_sidebar_state="collapsed")
# st.markdown(
#     """
# <style>
#     [data-testid="collapsedControl"] {
#         display: none
#     }
# </style>
# """,
#     unsafe_allow_html=True,
# )

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

def main():
    # Sidebar selection box
    page = st.sidebar.selectbox(
        'Select a page',
        ('Screener', 'Strategy','Backtest', 'Screening')
    )

    # Display the selected page
    if page != 'Select a page':
        if page == 'Home':
            # from pages.home_page import display_home_page
            # display_home_page()
            pass
        elif page == 'Strategy':
            from pages.strategy_page import display_strategy_page
            display_strategy_page()
        elif page == 'Screener':
            from pages.screener_page import display_screener_page
            display_screener_page()
        elif page == 'Backtest':
            from pages.backtests_page import display_backtest_page
            display_backtest_page()
        elif page == 'Screening':
            from pages.screening_page import screening_page
            screening_page()
if __name__ == '__main__':
    main()

conn.close()