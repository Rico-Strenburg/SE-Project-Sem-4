import streamlit as st

def display_screener_page(conn):

    # st.form()
    st.title('Screener Page')
    st.write('Welcome to the screener page!')
    name = st.text_input('Screener Name: ')
    desc = st.text_input('Description: ')
    stock_universe = st.text_input('Stock Universe: ')

    def basic_ratio_rule():

        st.header("Basic Ratio")

        basic1, basic2, basic3 = st.columns(3)

        with basic1:
            ratio = st.selectbox('Select the setup',['ratio name...', 'Other'])

        with basic2:
            must_be = st.selectbox('Select the setup',['>', '<', '>=', '<=', '='])

        with basic3:
            decimals = st.number_input("decimals")


        must_watch = st.checkbox("Must watch")


    def ratio_vs_ratio_rule():

        st.header("Ratio Vs Ratio")

        basic4, basic5, basic6, basic7 = st.columns(4)

        with basic4:
            ratiooo = st.selectbox('Select the setup',['Ratio name...', 'Other'])

        with basic5:
            mustbee = st.selectbox('select the setup', ['>', '<', '>=', '<=', '='], key="mustbee")

        with basic6:
            decimalss = st.number_input('Decimals')
        
        with basic7:
            rationamee = st.selectbox('select the setup',['Ratio name...','Other'])
        
        must_watchs = st.checkbox('must watch')


    st.subheader("Technical: ")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        setup1 = st.selectbox('Ratio name:',['Ratio','other', 'Other'])

    with col2:
        setup2 = st.selectbox('Comparison',['>', '<', '>=', '<=', '='], key="setup2")

    with col3:
        setup3 = st.number_input('Number: ')

    # must_watch_1 = st.checkbox("Must Watch")
        
    with st.popover("Add Rules Pattern"):
        basic_ratio_button = st.button("Basic Ratio", key="basic-ratio")
        ratio_vs_ratio_button = st.button("Ratio vs Ratio", key="ratio-vs-ratio")
        if basic_ratio_button:
            basic_ratio_rule() # basic ratio rule
        if ratio_vs_ratio_button:
            ratio_vs_ratio_rule() # ratio vs ratio rule
    
    

    st.subheader("Fundamental: ")

    colom1, colom2, colom3, colom4 = st.columns(4)
    with colom1:
        fundamental1 = st.selectbox('Ratio name: ', ['Ratio','other'])
    
    with colom2:
        fundamental2 = st.selectbox('Comparison', ['>', '<', '>=', '<=', '='], key="fundamental2")

    with colom3 :
        fundamental3 = st.number_input('Input PBVR: ')

    with colom4:
        fundamental4 = st.number_input('Input PER: ')

    with st.popover("Add Rules Pattern"):
        basic_ratio_button = st.button("Basic Ratio", key="basic-ratio1")
        ratio_vs_ratio_button = st.button("Ratio vs Ratio", key="ratio-vs-ratio1")
        if basic_ratio_button:
            basic_ratio_rule() # basic ratio rule
        if ratio_vs_ratio_button:
            ratio_vs_ratio_rule() # ratio vs ratio rule

        

    

    st.header('Pattern: ')

        
    # kolom1, kolom2 = st.columns(2)

    # with kolom1:
    #     rules_1 = st.selectbox('Select the setup', ['--','Other'], key="rules1")
        
    # with kolom2:
    #     rules = st.selectbox('Select the setup',['--', 'Other'], key="rules2")

    with st.popover("Add Rules Pattern"):
        basic_ratio_button = st.button("Basic Ratio", key="basic-ratio2")
        ratio_vs_ratio_button = st.button("Ratio vs Ratio", key="ratio-vs-ratio2")
        if basic_ratio_button:
            basic_ratio_rule() # basic ratio rule
        if ratio_vs_ratio_button:
            ratio_vs_ratio_rule() # ratio vs ratio rule
    