import streamlit as st
import sqlite3
from views.home_page import display_home_page
from views.strategy_page import display_strategy_page
from views.screener_page import display_screener_page
from views.backtests_page import display_backtest_page

def connect_to_database():
    conn = sqlite3.connect("novasieve_dev.db")
    return conn

conn = connect_to_database()

def main():
    # Create a sidebar for navigation
    page = st.sidebar.selectbox(
        'Select a page',
        ('Home', 'Strategy', 'Screener', 'Backtest')
    )

    # Display the selected page
    if page == 'Home':
        display_home_page(conn)
    elif page == 'Strategy':
        display_strategy_page(conn)
    elif page == 'Screener':
        display_screener_page(conn)
    elif page == 'Backtest':
        display_backtest_page(conn)
    
if __name__ == '__main__':
    main()

conn.close()