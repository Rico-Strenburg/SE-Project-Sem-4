import streamlit as st

def display_backtest_page():
    st.title('Backtest Page')
    st.write('Welcome to the backtest page!')

    st.selectbox("Screener: ", ["Screening_1", "Screening_2"])

    st.button("Backtest")
    st.button("Edit")

    st.text("Result : 1-25 of 250 equities")

    df_backtest = {
        'Symbol': ['BBCA', 'BBRI'],
        'Close': [1063, 30],
        'PBV': [5.11, 3.07]
    }

    data_backtest = st.dataframe(df_backtest,width = None, height=None, use_container_width=True)

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