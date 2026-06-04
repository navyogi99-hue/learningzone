from typing import TypedDict
from langgraph.graph import StateGraph
from langgraph.graph import START,END
class Mystate(TypedDict):
    """This class represents the state o fthe graph
   """
    name: str
    friends: list[str]
    family: list[str]
    message: str

def find_friends(state:Mystate)-> Mystate:    # node_1
    """ This function for find friends"""
    state['friends']= ["Ram" ,"shyam"]
    return state

def find_family(state:Mystate) -> Mystate:    # node_2
    """This function find family"""
    state['family'] = ["Sita", "gita"]
    return state

graph=StateGraph(Mystate)

graph.add_node("friends",find_friends)
graph.add_node("family",find_family)

graph.add_edge(START , "friends")
graph.add_edge("friends", "family")
graph.add_edge("family", END)

compiled_graph= graph.compile()


if __name__ == "__main__":
    response = compiled_graph.invoke({
        "name": "ABC",
        "friends": [],
        "family": []
    })
    print(response)

    