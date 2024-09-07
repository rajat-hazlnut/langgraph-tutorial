from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
load_dotenv()

def get_tools():

    tavily_tool = TavilySearchResults(max_results=2)
    tavily_tool.invoke("What's a 'node' in LangGraph?")

    tools = [tavily_tool]
    return tools