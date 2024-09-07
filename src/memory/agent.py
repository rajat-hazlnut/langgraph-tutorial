from langchain_openai import ChatOpenAI
from src.memory.state import State

from dotenv import load_dotenv
load_dotenv()

def agent(state: State):

    print(f"State on entering agent: {state}\n")
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    response = llm.invoke(state["messages"])

    return {"messages": [response]}