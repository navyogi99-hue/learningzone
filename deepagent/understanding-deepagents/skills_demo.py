from deepagents.backends import FilesystemBackend
from utils import get_model
from deepagents import create_deep_agent

model = get_model()
backend =FilesystemBackend(
    root_dir="./agent_workspace",
    virtual_mode=True
)
agent=create_deep_agent(
    model= model,
    backend=backend,
    skills=["./skills/"],
    system_prompt="""
You are a technical article writing agent with skills.
pick a right skill for acheiving the goal
Workflow:
1. Create a short plan with todos and wirte all the todos to /todos.md
2. Use the tool to get article to /article.md
3. Write rough notes /notes.md 
4. Write the fianl article to /article.md
5. Return a short summary and mention the files created.

"""
)

if __name__ == "__main__":
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Write an linkedin article on algebra."
                }
            ]
        }
    )
    result["messages"][-1].pretty_print()