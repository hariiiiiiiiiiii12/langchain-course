import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = """
    Lionel Andrés, widely regarded as one of the greatest players in history, he has set numerous records for individual accolades won throughout his professional footballing career, including eight Ballons d'Or, six European Golden Shoes, and being named the world's best player by FIFA eight times.    
    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them    
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response.content[0]["text"])

if __name__ == "__main__":
    main()
