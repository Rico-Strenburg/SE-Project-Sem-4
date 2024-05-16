import streamlit as st
from src.utilities.manager import *
from src.model.Strategy import Strategy
from typing import List

basic_ratio_options = ['<select>', 'Open Price', 'High Price', 'Low Price', 'Close Price']
operator_options = ['>', '<', '>=', '<=', '=']

def basic_ratio_rule(ratio:Ratio):
    basic1, basic2, basic3, basic4, basic5, basic6 = st.columns([3,3,3,1,1,1])
    with basic1:
        ratio.ratio = st.selectbox('Select the setup',basic_ratio_options,index=basic_ratio_options.index(ratio.ratio), key=f"name_{ratio.ratio_id}")
    with basic2:
        ratio.operator = st.selectbox('Select the setup',operator_options, index=operator_options.index(ratio.operator), key=f"operator_{ratio.ratio_id}" )
    with basic3:
        ratio.value = st.number_input("decimals",value=ratio.value,  key=f"decimal_{ratio.ratio_id}")
    with basic4:
        st.write('<div style="height: 30px;"></div>', unsafe_allow_html=True)
        with st.popover("\u22ee"):
            st.markdown("Additional Settings")
            ratio.must_match = st.checkbox("Must Match",value=ratio.must_match, key=f"watch_{ratio.ratio_id}")
    with basic5:
        st.write('<div style="height: 30px;"></div>', unsafe_allow_html=True)
        delete_button = st.button('\u2717', key=f"delete_{ratio.ratio_id}")
        if delete_button:
            delete_ratio(ratio.ratio_id)
            st.rerun()
    with basic6:
        st.write('<div style="height: 30px;"></div>', unsafe_allow_html=True)
        save_button = st.button('\u2713', key=f"save_{ratio.ratio_id}")
        if save_button:
            update_ratio(ratio)

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

#Check if Id is valid and check if strategy exists
if 'current_id' not in st.session_state:
    st.session_state['current_id'] = '-1'
strategy = get_strategies(id=st.session_state['current_id'])
                
if strategy:
    #Get Strategy and Fundamental Ratios
    strategy = Strategy(*strategy)
    fund_ratios:List[Ratio] = get_ratio(strategy.id)
    
    name = st.text_input('Name:', strategy.name)
    desc = st.text_area('Description:', strategy.desc)
    
    #Display All Fundamental Rule
    st.header("Fundamental Rule")
    for ratio in fund_ratios:
        if (ratio.type == 'basic'):
            basic_ratio_rule(ratio)
        if (ratio.type == 'versus'):
            pass
        
    with st.popover("Add Rules Pattern"):
        basic_ratio_button = st.button("Basic Ratio", key="basic-ratio")
        ratio_vs_ratio_button = st.button("Ratio vs Ratio", key="ratio-vs-ratio")
        if basic_ratio_button:
            insert_ratio(strategy.id, 'basic')
            st.rerun()
        if ratio_vs_ratio_button:
            insert_ratio(strategy.id, 'versus')
            st.rerun()
    st.header("Technical Rule")
else:
    st.write("Strategy Is Not Found")

    
    
#     st.session_state[new_name_key] = new_name
#     st.session_state[new_desc_key] = new_desc