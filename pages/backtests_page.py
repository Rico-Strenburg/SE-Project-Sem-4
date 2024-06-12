import streamlit as st
from src.utilities.manager import *
from src.model.Strategy import Strategy
from datetime import datetime

dictionary = get_strategy_dictionary()
default_date = datetime.today()

stock_names = ["BBCA.JK", "BMRI.JK", "BTPS.JK", "BREN.JK", "TPIA.JK", "kaushduiahdui"]


def display_backtest_page():
    def validate():
        if (strategy == None):
            st.write("Strategy cannot be empty")
            return False
        if (start_time == None or end_time == None):
            st.write("Time Period cannot be empty")
            return False
        if (end_time < start_time):
            st.write("End Time cannot before start time")
            return False
        if (len(selected_stocks) <= 0):
            st.write("Please select a stock")
            return False
        return True
        
    # tunggu ada function get_strategy_result
    # strategy = get_strategies()
    # display_names = [f"{strategies.name}" for strategies in strategy]

    # selected_name = st.selectbox("Select a screener:", display_names)
    # selected_screener:Strategy = [x for x in strategy if x.name == selected_name][0]
    # selected_index = None

    st.title('Backtest Page')
    st.write('Welcome to the backtest page!')

    strategy = st.selectbox("Select Strategy: ", dictionary.keys(),format_func=dictionary.get)
    selected_stocks = st.multiselect("Select stocks (up to 5):", stock_names)

    # Check if the number of selected stocks exceeds 5
    if len(selected_stocks) > 5:
        st.warning("You can only select up to 5 stocks.")
        # Slice the selected_stocks list to contain only the first 5 items
        selected_stocks = selected_stocks[:5]
    start_time = st.date_input("Start Time period: ", value=default_date)
    end_time = st.date_input("End time period", value=None)

    # if end_time and end_time < start_time:
    #     st.warning("End Time cannot be before Start Time. Please select a valid End Time.")

    # if end_time:
    #     st.write(f"Selected End Time: {end_time}")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        backtest = st.button("Backtest")
    with col2:
        edit_button = st.button("Edit Strategy")

    if edit_button:
        st.switch_page("pages/strategy_page.py")

    if backtest:
        if (validate()):
            st.write("Succesful")
        # st.dataframe()

    # st.text("Result : 1-25 of 250 equities")

    # df_backtest = {
    #     'Symbol': ['BBCA', 'BBRI'],
    #     'Close': [1063, 30],
    #     'PBV': [5.11, 3.07]
    # }

    # data_backtest = st.dataframe(df_backtest,width = None, height=None, use_container_width=True)

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

if __name__ == "__main__":
    display_backtest_page()
    sidebar_selection()