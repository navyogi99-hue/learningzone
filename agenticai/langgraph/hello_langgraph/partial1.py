from langgraph.graph import StateGraph,END,START
from typing import TypedDict

class state(TypedDict):
    fin_dept: bool
    adm_dept: bool
    sport_dept: bool
    std_id: str

def finance_department_check(state: state):
    return{"fin_dept":True}
def administration_department_check(state:state):
    return{"adm_dept":True}
def sport_department_check(state:state):
    return{"sport_dept":True}

graph= StateGraph(state)

graph.add_node("fin",finance_department_check)
graph.add_node("adm",administration_department_check)
graph.add_node("sport",sport_department_check)

graph.add_edge(START,"fin")
graph.add_edge("fin","adm")
graph.add_edge("adm","sport")
graph.add_edge("sport",END)

if __name__ =="__main__":
    compiled_graph = graph.compile()
    result = compiled_graph.invoke(state(std_id=10002))

    print(result)