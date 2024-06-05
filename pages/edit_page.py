import streamlit as st
from src.utilities.manager import *
from src.model.Strategy import Strategy
from typing import List

trading_style_param = ["Trading Style Name 1", "Trading Style Name 2"]
stoploss_param = ["Stopp Loss Name 1", "Stopp Loss Name 2"]

if 'current_id' not in st.session_state:
    st.session_state['current_id'] = '-1'
strategy = get_strategies(id=st.session_state['current_id'])
                
if strategy:
    strategy = Strategy(*strategy)
    dictionary = get_screener_dictionary()

    # basic_1 = st.columns([1,1])
    st.title("Strategy Edit Page")
    # st.text("Welcome Strategy Edit Page")
    # st.text(f"Strategy  Name: {strategy.name}")
    # st.text(f"Descripstion: {strategy.desc}")
    strategy_name = st.text_input("Screener Name: ", strategy.name)
    desc = st.text_area("Description: ", strategy.desc)

    # column = st.selectbox("Describe Column", list(dataset.columns), format_func=cols.get)

    screener = st.selectbox("Screener: ", dictionary.keys(),format_func=dictionary.get)

    trading_style = st.selectbox("Trading Style: ", trading_style_param, index = trading_style_param.index(strategy.trading), key=f"trading_{strategy.id}")
    stopLoss = st.selectbox("Stopp Loss: ", stoploss_param, index = stoploss_param.index(strategy.stopLoss), key=f"trading_{strategy.id}")

    
    save = st.button("Save")
    if save :
        update_strategy(strategy_name, desc, screener, trading_style, stopLoss)
    reset = st.button("Reset")

    # if save:
    #     update_strategy(strategy.name, strategy.desc, strategy.id, screener, trading_style, stopLoss)

    

