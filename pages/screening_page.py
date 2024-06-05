import streamlit as st
from src.utilities.manager import *
from src.model.Screener import Screener

def screening_page():
    screeners = get_screener()
    display_names = [f"{screener.name}" for screener in screeners]
    
    st.header("Screening Page")

    selected_name = st.selectbox("Select a screener:", display_names)
    selected_screener:Screener = [x for x in screeners if x.name == selected_name][0]
    selected_index = None

    # for i, screener in enumerate(screeners):
    #     if screener.name == selected_name.split()[0] and screener.id == int(selected_name.split()[1][1:-1]):  # Assuming unique_id is an integer
    #         selected_object = screener
    #         selected_index = i
    #         break
    # selected_screener = screeners[int(selected_index)]

    apply_button = st.button("Screener")
    st.button("Edit")
    
    if (apply_button):
        get_screening_result(selected_screener.id)
        # table_result = selected_screener.id)
        

    st.text("Result : 1-25 of 250 equities")

    df_screening = {
        'Symbol': ['BBCA', 'BBRI'],
        'Close': [1063, 30],
        'PBV': [5.11, 3.07]
    }

    data_screening = st.dataframe(df_screening,width = None, height=None, use_container_width=True)


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
    screening_page()
    sidebar_selection()