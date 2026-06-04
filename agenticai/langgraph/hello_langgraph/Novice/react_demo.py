from langchain_core.messages import SystemMessage,HumanMessage,BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from typing import TypedDict,Literal
from typing_extensions import Annotated
# Reducer

from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph,START,END
import os
load_dotenv()
project = os.getenv('GOOGLE_CLOUD_PROJECT')

# MODEL
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite",
    vertexai=True,
    project= project
)

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@tool
def add(a:int,b:int) -> int:
    """add two numbers
    """
    return a+b
@tool
def subtract(a: int, b:int) -> int:
    """Subtract two numbers"""
    return a - b

@tool
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    return a / b

@tool
def get_weather(city: str) -> str:
    """Get the weather of the city"""
    return f"{city} is sunny"

# whole set of tools in an array

tools = [multiply, add, subtract, divide, get_weather]

# create a tool node

tool_node = ToolNode(tools=tools)


# create a model with bind tools

llm_with_tools = llm.bind_tools(tools=tools)

# STATE
class AgentState(TypedDict):
    """State"""
    meessages: Annotated[list[BaseMessage],add_messages]
    answer: str

def llm_node(State:AgentState):
    response = llm_with_tools.invoke(State['messages'])
    return{"messages":[response]}
def route_tools(state:AgentState) -> Literal["tools","final"]:
    last_message = state['message'][-1]

    if getattr(last_message,'tools_calls', None):
        return "tools"
    return "final"

def final_result(state:AgentState):
    print(state["messages"][-1].pretty_print())
    state["answer"]= state["messages"][-1].content
    return state

graph = StateGraph(AgentState)
graph.add_edge(START, "llm")
graph.add_conditional_edges(
    "llm",
     route_tools,
    {
        "tools": "tools",
        "final": "final_response"

    }
)
graph.add_edge("tools","llm")
graph.set_finish_point("final_response")

if __name__ == "__main__":
    compiled_graph = graph.compile()
    result = compiled_graph.invoke({
        "messages": [
            HumanMessage(content="10 * 5")
        ]
    })

    for msg in result['messages']:
        print(f"{type(msg).__name__}  : {msg.content}")