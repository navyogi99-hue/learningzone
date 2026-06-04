from langgraph.graph import StateGraph, START , END 
from typing import TypedDict, Literal
from typing_extensions import Annotated

class State(TypedDict):
    query: str
    response: str
def process_question(State:State) -> Literal["finance", "sports", "admin"]:
    if "fee" in State["query"]:
        return "finance"
    elif "sport" in State["query"]:
        return "sports"
    else:
        return "admin"
def financial_response(state: State):
    return {"response": "pay your fee"}
def sports_dept(state: State):
    return {"response": "Pt trainer on leave"}
def admin_dept(state: State):
    return {"response": "admin office is closed today"}
graph = StateGraph(State)

graph.add_node("fin", financial_response)
graph.add_node("sports", sports_dept)
graph.add_node("adm", admin_dept)
graph.add_conditional_edges(
    START,
      process_question, {
    "finance": "fin",
    "sports": "sports", 
    "admin": "adm"
})
graph.add_edge("fin", END)
graph.add_edge("sports", END)
graph.add_edge("adm", END)
if __name__ == "__main__":
    compiled_graph = graph.compile()
    query = input("Enter your question")
    response = compiled_graph.invoke({
        "query": query,
        "response": ""
})
    print(response)


