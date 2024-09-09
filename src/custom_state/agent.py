from langchain_openai import ChatOpenAI
from src.custom_state.state import State
from src.custom_state.tools import get_tools
from src.custom_state.request_assistance import RequestAssistance
from langchain_core.messages import AIMessage, ToolMessage

from dotenv import load_dotenv
load_dotenv()

def agent(state: State):

    print(f"State on entering agent: {state}\n")

    ask_human = False
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    llm_with_tools = llm.bind_tools(tools=get_tools())

    response = llm_with_tools.invoke(state["messages"])

    if (
        response.tool_calls
        and response.tool_calls[0]["name"] == RequestAssistance.__name__
    ):
        ask_human = True
    return {"messages": [response], "ask_human": ask_human}


def create_response(response: str, ai_message: AIMessage):
    return ToolMessage(
        content=response,
        tool_call_id=ai_message.tool_calls[0]["id"],
    )


def human_node(state: State):
    new_messages = []
    if not isinstance(state["messages"][-1], ToolMessage):
        # Typically, the user will have updated the state during the interrupt.
        # If they choose not to, we will include a placeholder ToolMessage to
        # let the LLM continue.
        new_messages.append(
            create_response("No response from human.", state["messages"][-1])
        )
    return {
        # Append the new messages
        "messages": new_messages,
        # Unset the flag
        "ask_human": False,
    }