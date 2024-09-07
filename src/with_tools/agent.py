from langchain_openai import ChatOpenAI
from src.with_tools.state import State
from src.with_tools.tools import get_tools

from dotenv import load_dotenv
load_dotenv()

def agent(state: State):

    print(f"State on entering agent: {state}\n")
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    llm_with_tools = llm.bind_tools(tools=get_tools())

    response = llm_with_tools.invoke(state["messages"])

    return {"messages": [response]}