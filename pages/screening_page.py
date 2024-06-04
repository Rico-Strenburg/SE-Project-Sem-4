import streamlit as st

def screening_page():

    st.header("Screening Page")

    st.selectbox("Screener: ", ["Screening_1", "Screening_2"])

    st.button("Screener")
    st.button("Edit")

    st.text("Result : 1-25 of 250 equities")

    df_screening = {
        'Symbol': ['BBCA', 'BBRI'],
        'Close': [1063, 30],
        'PBV': [5.11, 3.07]
    }

    data_screening = st.dataframe(df_screening,width = None, height=None, use_container_width=True)

screening_page()