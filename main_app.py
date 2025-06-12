from report_info import investment_report
import streamlit as st
from stock_info import Stock
from search_index import SearchResult, search_company

st.title("AI 투자 보고서 생성 서비스")

search_query = st.text_input("회사명", "Apple Inc")
# company_list = ["AAPL: Apple Inc",
#                 "APLE: Apple Hospitality REIT Inc"]


hits = search_company(search_query)['hits']
search_results = [SearchResult(hit) for hit in hits]

if search_results:
    company_selected = st.selectbox("회사 선택", search_results)

    tabs = ["주식 정보", "투자 보고서"]
    tab1, tab2 = st.tabs(tabs)

    with tab1:
        st.header(f"{search_query}의 6개월 주식 거래량")
        stock = Stock(company_selected.symbol)
        volume = stock.get_stock_volume()
        st.line_chart(volume, use_container_width=True)

    with tab2:
        st.header(f"{search_query} 투자보고서 생성")

        if st.button("투자 보고서 생성"):
            with st.spinner(text="투자 보고서 생성 중..."):
                report = investment_report(company_selected.name, company_selected.symbol)
                st.success("투자 보고서 생성 완료!")            
            st.write(report)
else:
    st.warning(f"'{search_query}'에 해당하는 회사를 찾을 수 없습니다.")