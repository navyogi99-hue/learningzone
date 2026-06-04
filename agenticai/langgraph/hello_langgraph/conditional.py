from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from typing_extensions import Annotated

class State(TypedDict):
    query: str
    response: str
def process_question(state:State) -> Literal["apply", "process", "approval"]:
    if 'apply' in state['query']:
        return "apply"
    elif 'process' in state['query']:
        return "process"
    else:
        return "approval"
def apply(state: State):
    return {"response": "Applying..."}
def process(state: State):
    return {"response": "Processing..."}
def approval(state: State):
    return {"response": "Approving..."}
graph = StateGraph(State)
graph.add_node("apply", apply)
graph.add_node("process", process)
graph.add_node("approval", approval)
graph.add_conditional_edges(START,
     process_question, {
    "apply": "apply",
    "process": "process",
    "approval": "approval"})
graph.add_edge("apply", END)
graph.add_edge("process", END)
graph.add_edge("approval", END)
if __name__ == "__main__":
    compiled_graph = graph.compile()
    result = compiled_graph.invoke(State(query='I want to apply for a loan', response=''))
    print(result)       