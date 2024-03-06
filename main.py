import streamlit as st
from home_page import display_home_page
from strategy_page import display_strategy_page
from screener_page import display_screener_page
from backtests_page import display_backtest_page

# Create a sidebar for navigation
page = st.sidebar.selectbox(
    'Select a page',
    ('Home', 'Strategy', 'Screener', 'Backtest')
)

# Display the selected page
if page == 'Home':
    display_home_page()
elif page == 'Strategy':
    display_strategy_page()
elif page == 'Screener':
    display_screener_page()
elif page == 'Backtest':
    display_backtest_page()