from langgraph.graph import StateGraph,START,END
from typing import _TypedDict
from typing_extensions import Annotated
import operator

def my_choice(exiting,new):
    return new

class state(_TypedDict):
    message: Annotated[list[str],operator.add]
    student: str

def message_from_friend(state:state):
    return{"messages":["you will win"]}

def message_from_enenmy(state:state):
    return{"messages":["you will die trying but never win"]}

graph= StateGraph(state)

graph.add_node("friend", message_from_friend)
graph.add_node("enemy", message_from_enenmy)

graph.add_edge(START,"friend")
graph.add_edge(START,"enemy")
graph.add_edge("friend",END)
graph.add_edge("enemy",END)

if __name__ == "__main__":
    complied_graph = graph.compile()
    result = complied_graph.invoke(state(message=[],student= 'i1003'))
    print(result)
    