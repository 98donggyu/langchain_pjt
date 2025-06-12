from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from stock_info import Stock

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=api_key, temperature=0)

def investment_report(company, symbol):
    
    system_prompt = """
    Want assistance provided by qualified individuals enabled with experience on understanding charts using technical analysis tools while interpreting macroeconomic environment prevailing across world consequently assisting customers acquire long term advantages requires clear verdicts therefore seeking same through informed predictions written down precisely! First statement contains following content- “Can you tell us what future stock market looks like based upon current conditions ?".
    """

    user_prompt = """
        {company}에 주식을 투자해도 될까요? 마크다운 형식의 투자보고서를 한글로 작성해 주세요.
        야래의 기본 정보, 재무제표를 참고해 마크다운 형식의 투자 보고서를 한글로 작성해 주세요.

        기본정보:
        {basic_info}

        재무제표:
        {finacial_statement}
    """

    prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", user_prompt)
    ])

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    # company = "Apple Inc"
    # symbol = "AAPL"

    stock = Stock(symbol)
    
    req_value = {
        "company":company,
        "basic_info": stock.get_basic_info(),
        "finacial_statement" : stock.get_financial_statement()
    }

    response = chain.invoke(req_value)

    return response

if __name__ == "__main__":
    company = "Apple Inc"
    symbol = "AAPL"

    report = investment_report(company, symbol)