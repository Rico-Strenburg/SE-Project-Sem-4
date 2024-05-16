import streamlit as st
from src.utilities.manager import *
from src.model.Strategy import Strategy

def basic_ratio_rule(ratio:Ratio):
    basic1, basic2, basic3 = st.columns(3)
    with basic1:
        name = st.selectbox('Select the setup',['ratio name...', 'Other'], key=f"name_{ratio.ratio_id}")
    with basic2:
        operator = st.selectbox('Select the setup',['>', '<', '>=', '<=', '='], key=f"operator_{ratio.ratio_id}" )
    with basic3:
        decimals = st.number_input("decimals", key=f"decimal_{ratio.ratio_id}")
    must_watch = st.checkbox("Must watch", key=f"watch_{ratio.ratio_id}")

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

st.write(st.session_state)
st.title("Edit page")

if 'current_id' not in st.session_state:
        st.session_state['current_id'] = '-1'
strategy = get_strategies(id=st.session_state['current_id'])

# with st.popover("Add Rules Pattern"):
#             basic_ratio_button = st.button("Basic Ratio", key="basic-ratio")
#             ratio_vs_ratio_button = st.button("Ratio vs Ratio", key="ratio-vs-ratio")
#             if basic_ratio_button:
#                 basic_ratio_rule() # basic ratio rule
#             if ratio_vs_ratio_button:
#                 ratio_vs_ratio_rule() # ratio vs ratio rule
                
                
if strategy:
    strategy = Strategy(*strategy)
    ratios = get_ratio(strategy.id)
    # with st.form("edit_strategy"):
    #     st.write("Rate my satisfaction")
    #     name = st.text_input('New Name:', strategy.name)
    #     desc = st.text_area('New Description:', strategy.desc)
    #     for ratio in ratios:
    #         basic_ratio_rule()
    #     submit = st.form_submit_button("Submit")
    #     if st.button('Add Ratio'):
    #         insert_ratio(strategy.id)
    name = st.text_input('Name:', strategy.name)
    desc = st.text_area('Description:', strategy.desc)
    st.header("Basic Ratio")
    for ratio in ratios:
        basic_ratio_rule(ratio)
    # submit = st.form_submit_button("Submit")
    if st.button('Add Ratio'):
        insert_ratio(strategy.id)
        st.rerun()
    st.header("Ratio vs Ratio")
    
else:
    st.write("Strategy Is Not Found")

    
    
#     st.session_state[new_name_key] = new_name
#     st.session_state[new_desc_key] = new_desc