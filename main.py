import streamlit as st
import sqlite3
from src.utilities.manager import init_db
from pages.home_page import display_home_page
from pages.strategy_page import display_strategy_page
# from views.screener_page import display_screener_page
# from views.backtests_page import display_backtest_page
# from pages.edit_page import display_edit_page

def connect_to_database():
    conn = sqlite3.connect("novasieve_dev.db")
    return conn

init_db()
conn = connect_to_database()

def main():
    page = st.sidebar.selectbox(
        'Select a page',
        ('Home', 'Strategy', 'Screener', 'Backtest')
    )

    
    # Display the selected page
    if page == 'Home':
        display_home_page()
    elif page == 'Strategy':
        display_strategy_page()
    
if __name__ == '__main__':
    main()

conn.close()