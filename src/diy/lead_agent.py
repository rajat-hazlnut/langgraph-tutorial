from langchain_openai import ChatOpenAI
from src.basic.state import State

from dotenv import load_dotenv
load_dotenv()

def lead_agent(state: State):

    print(state)
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    return {"messages": [llm.invoke(state["messages"])]}

# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_openai import ChatOpenAI
# from pydantic import BaseModel
# from typing import Literal

# members = ["Math", "Science"]
# system_prompt = (
#     "You are a supervisor tasked with managing a conversation between the"
#     " following workers:  {members}. Given the following user request,"
#     " respond with the worker to act next. Each worker will perform a"
#     " task and respond with their results and status. When finished,"
#     " respond with FINISH."
# )
# # Our team supervisor is an LLM node. It just picks the next agent to process
# # and decides when the work is completed
# options = ["FINISH"] + members

# class routeResponse(BaseModel):
#     next: Literal["Math","Science","Finish"]

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt),
#         MessagesPlaceholder(variable_name="messages"),
#         (
#             "system",
#             "Given the conversation above, who should act next?"
#             " Or should we FINISH? Select one of: {options}",
#         ),
#     ]
# ).partial(options=str(options), members=", ".join(members))


# llm = ChatOpenAI(model="gpt-4o-mini")

# def supervisor_agent(state):
#     supervisor_chain = (
#         prompt
#         | llm.with_structured_output(routeResponse)
#     )
#     return supervisor_chain.invoke(state)