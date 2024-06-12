import streamlit as st
from typing import List, Literal
from src.utilities.manager import get_screener
from src.utilities.manager import *
# from src.model.Strategy import Strategy
from src.model.Screener import Screener
from src.model.Pattern import Pattern

from backend_api import analysis_options

base_ratio_options = ['<select>']
pattern_rule_option = ["Basic Pattern Rule", "Medium Pattern", "Hard Pattern"]
# basic_ratio_options = ['<select>', 'Open Price', 'High Price', 'Low Price', 'Close Price']
operator_options = ['=', '>', '≥', '<', '≤', 'cross-above', 'cross-below']

def basic_ratio_rule(ratio:Ratio, analysis_type: Literal['technical', 'fundamental']):
    basic_ratio_options = analysis_options[analysis_type]
    list_basic_ratio_options = base_ratio_options + list(basic_ratio_options.values())
    
    basic1, basic2, basic3, basic4, basic5, basic6 = st.columns([3,3,3,1,1,1])
    with basic1:
        ratio.ratio = st.selectbox('',list_basic_ratio_options,index=list_basic_ratio_options.index(ratio.ratio), key=f"name_{ratio.ratio_id}")
    with basic2:
        ratio.operator = st.selectbox('',operator_options, index=operator_options.index(ratio.operator), key=f"operator_{ratio.ratio_id}" )
    with basic3:
        if ratio.value is None:
            ratio.value = 0.0
        ratio.value = st.number_input('',value=float(ratio.value),format="%.2f" ,key=f"decimal_{ratio.ratio_id}")
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

def ratio_vs_ratio_rule(ratio:Ratio, analysis_type: Literal['technical', 'fundamental']):
    basic_ratio_options = analysis_options[analysis_type]
    list_basic_ratio_options = base_ratio_options + list(basic_ratio_options.values())

    basic7, basic8, basic9, basic10, basic11, basic12, basic13, basic14 = st.columns([3,3,3,0.7,3,1.2,1,1])
    with basic7:
        ratio.ratio = st.selectbox('',list_basic_ratio_options,index=list_basic_ratio_options.index(ratio.ratio), key=f"name1_{ratio.ratio_id}")
    with basic8:
        ratio.operator = st.selectbox('',operator_options, index=operator_options.index(ratio.operator), key=f"operator_{ratio.ratio_id}" )
    with basic9:
        if ratio.value is None:
            ratio.value = 0.0
        ratio.value= st.number_input('',value=float(ratio.value),format="%.2f" , key=f"decimal_{ratio.ratio_id}")
    with basic10:
        st.header("x")
    with basic11:
        ratio.ratio2 = st.selectbox('',list(list_basic_ratio_options),index=list(list_basic_ratio_options).index(ratio.ratio2), key=f"name2_{ratio.ratio_id}")
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

def show_pattern_rule(pattern:Pattern):
    row1, row2, row3, row4 = st.columns([3,3,1,1])
    with row1:
        pattern.name = st.selectbox('',pattern_rule_option,index=pattern_rule_option.index(pattern.name), key=f"pattern_name_{pattern.patternId}")
    with row2:
        st.write('<div style="height: 30px;"></div>', unsafe_allow_html=True)
        with st.popover("\u22ee"):
            st.markdown("Additional Settings")
            pattern.must_match = st.checkbox("Must Match", key=f"pattern_match_{pattern.patternId}")
    with row3:
        st.write('<div style="height: 30px;"></div>', unsafe_allow_html=True)
        delete_button = st.button('\u2717', key=f"delete_pattern_){pattern.patternId}")
        if delete_button:
            delete_pattern(pattern.patternId)
            st.rerun()
    with row4:
        st.write('<div style="height: 30px;"></div>', unsafe_allow_html=True)
        save_button = st.button('\u2713', key=f"save_pattern_{pattern.patternId}")
        if save_button:
            update_pattern(pattern.patternId, pattern.name, pattern.must_match)

# def screening_page():
    


# st.text("Screener: ")
if 'current_id' not in st.session_state:
    st.session_state['current_id'] = '-1'
screener = get_screener(id=st.session_state['current_id'])
                
if screener:
    #Get Strategy and Fundamental Ratios
    screener = Screener(*screener)
    fund_ratios:List[Ratio] = get_fundamental(screener.id)
    tech_ratios:List[Ratio] = get_technical(screener.id)
    pattern_rule:List[Pattern] = get_pattern(screener.id)

    st.title('Screening Edit Page')
    screener_name = st.text_input("Screener Name: ", screener.name)
    desc = st.text_area("Description: ", screener.desc)
    # stock_universe = st.selectbox("Stock Universe : ", screener.stock_universe(("IHSG", "..")))
    
    save_button = st.button("Save")
    if save_button:
        update_screener(screener_name, desc, screener.id)
        st.text("Succesfull")
    
    
    #Display All Fundamental Rule
    st.header("Fundamental Rule")
    for ratio in fund_ratios:
        if (ratio.type == 'basic'):
            basic_ratio_rule(ratio, 'fundamental')
        if (ratio.type == 'versus'):
            ratio_vs_ratio_rule(ratio, 'fundamental')
        
    with st.popover("Add Rules Pattern"):
        basic_ratio_button = st.button("Basic Ratio", key="basic-ratio-f")
        ratio_vs_ratio_button = st.button("Ratio vs Ratio", key="ratio-vs-ratio-f")
        if basic_ratio_button:
            insert_ratio(screener.id, 'basic', 'fundamental')
            st.rerun()
        if ratio_vs_ratio_button:
            insert_ratio(screener.id, 'versus', 'fundamental')
            st.rerun()
            
    st.header("Technical Rule")
    for ratio in tech_ratios:
        if (ratio.type == 'basic'):
            basic_ratio_rule(ratio, 'technical')
        if (ratio.type == 'versus'):
            ratio_vs_ratio_rule(ratio, 'technical')
        
    with st.popover("Add Rules Pattern"):
        basic_ratio_button = st.button("Basic Ratio", key="basic-ratio-t")
        ratio_vs_ratio_button = st.button("Ratio vs Ratio", key="ratio-vs-ratio-t")
        if basic_ratio_button:
            insert_ratio(screener.id, 'basic', 'technical')
            st.rerun()
        if ratio_vs_ratio_button:
            insert_ratio(screener.id, 'versus', 'technical')
            st.rerun()
        
    st.header("Pattern Rule")
    for pattern in pattern_rule:
        # st.write(pattern.patternId)
        show_pattern_rule(pattern)
        
    pattern_button = st.button("Add Pattern")
    if pattern_button:
        insert_pattern(screener.id, 0)
        st.rerun()
    
    back_button = st.button("Back")
    
    if back_button:
        st.session_state['current_id'] = None
        st.switch_page("pages/screener_page.py")
else:
    st.write("Strategy Is Not Found")

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
    
sidebar_selection()