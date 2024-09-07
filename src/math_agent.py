from langchain_openai import ChatOpenAI
from src.basic.state import State
from src.add_tool import AddTool
from src.multiply_tool import MultiplyTool
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

def math_agent(state: State):

    print(state)
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    llm_with_tools = llm.bind_tools(tools=[AddTool,MultiplyTool],tool_choice="any")

    prompt = PromptTemplate.from_template("""
        You are an agent to solve math questions.
    """)

    chain = prompt | llm_with_tools

    return {"messages": [chain.invoke(state["messages"])]}