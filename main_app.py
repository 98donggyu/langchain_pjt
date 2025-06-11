import streamlit as st
from stock_info import Stock

st.title("AI 투자 보고서 생성 서비스")

search_query = st.text_input("회사명", "Apple Inc")
company_list = ["AAPL: Apple Inc",
                "APLE: Apple Hospitality REIT Inc"]
company_selected = st.selectbox("회사 선택", company_list, index=0)

tabs = ["주식 정보", "투자 보고서"]
tab1, tab2 = st.tabs(tabs)

with tab1:
    st.header(f"{company_selected}의 6개월 주식 거래량")
    stock = Stock(company_selected.split(":")[0])
    volume = stock.get_stock_volume()
    st.line_chart(volume)
    

with tab2:
    st.header(f"{company_selected} AI 투자 보고서")