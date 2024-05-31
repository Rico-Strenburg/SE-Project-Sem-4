import streamlit as st
from src.utilities.manager import get_screener
from src.utilities.manager import *
# from src.model.Strategy import Strategy
from src.model.Screener import Screener
from typing import List

basic_ratio_options = ['<select>', 'Open Price', 'High Price', 'Low Price', 'Close Price']
operator_options = ['>', '<', '>=', '<=', '=']

def basic_ratio_rule(ratio:Ratio):
    basic1, basic2, basic3, basic4, basic5, basic6 = st.columns([3,3,3,1,1,1])
    with basic1:
        ratio.ratio = st.selectbox('',basic_ratio_options,index=basic_ratio_options.index(ratio.ratio), key=f"name_{ratio.ratio_id}")
    with basic2:
        ratio.operator = st.selectbox('',operator_options, index=operator_options.index(ratio.operator), key=f"operator_{ratio.ratio_id}" )
    with basic3:
        ratio.value = st.number_input("",value=ratio.value,  key=f"decimal_{ratio.ratio_id}")
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

def ratio_vs_ratio_rule(ratio:Ratio):
    basic7, basic8, basic9, basic10, basic11, basic12, basic13, basic14 = st.columns([3,3,3,0.7,3,1.2,1,1])
    with basic7:
        ratio.ratio = st.selectbox('',basic_ratio_options,index=basic_ratio_options.index(ratio.ratio), key=f"name1_{ratio.ratio_id}")
    with basic8:
        ratio.operator = st.selectbox('',operator_options, index=operator_options.index(ratio.operator), key=f"operator_{ratio.ratio_id}" )
    with basic9:
        ratio.value= st.number_input('',value=ratio.value,  key=f"decimal_{ratio.ratio_id}")
    with basic10:
        st.header("x")
    with basic11:
        ratio.ratio2 = st.selectbox('',basic_ratio_options, index= basic_ratio_options.index(ratio.ratio2), key=f"name2_{ratio.ratio_id}" )
    with basic12:
        st.write('<div style="height: 30px;"></div>', unsafe_allow_html=True)
        with st.popover("\u22ee"):
            st.markdown("Additional Settings")
            ratio.must_match = st.checkbox("Must Match",value=ratio.must_match, key=f"watch_{ratio.ratio_id}")
    with basic13:
        st.write('<div style="height: 30px;"></div>', unsafe_allow_html=True)
        delete_button = st.button('\u2717', key=f"delete_{ratio.ratio_id}")
        if delete_button:
            delete_ratio(ratio.ratio_id)
            st.rerun()
    
    with basic14:
        st.write('<div style="height: 30px;"></div>', unsafe_allow_html=True)
        save_button = st.button('\u2713', key=f"save_{ratio.ratio_id}")
        if save_button:
            update_ratio(ratio)

# def screening_page():
    


# st.text("Screener: ")
if 'current_id' not in st.session_state:
    st.session_state['current_id'] = '-1'
screener = get_screener(id=st.session_state['current_id'])
                
if screener:
    #Get Strategy and Fundamental Ratios
    screener = Screener(*screener)
    fund_ratios:List[Ratio] = get_ratio(screener.id)

    st.title('Screening Edit Page')
    screener_name = st.text_input("Screener Name: ", screener.name)
    desc = st.text_area("Description: ", screener.desc)
    # stock_universe = st.selectbox("Stock Universe : ", screener.stock_universe(("IHSG", "..")))
    
    
    #Display All Fundamental Rule
    st.header("Fundamental Rule")
    for ratio in fund_ratios:
        if (ratio.type == 'basic'):
            basic_ratio_rule(ratio)
        if (ratio.type == 'versus'):
            ratio_vs_ratio_rule(ratio)
        
    with st.popover("Add Rules Pattern"):
        basic_ratio_button = st.button("Basic Ratio", key="basic-ratio")
        ratio_vs_ratio_button = st.button("Ratio vs Ratio", key="ratio-vs-ratio")
        if basic_ratio_button:
            insert_ratio(screener.id, 'basic')
            st.rerun()
        if ratio_vs_ratio_button:
            insert_ratio(screener.id, 'versus')
            st.rerun()
    st.header("Technical Rule")
else:
    st.write("Strategy Is Not Found")
    