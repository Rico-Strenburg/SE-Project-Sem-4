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
    
if __name__ == '__main__':
    display_backtest_page()