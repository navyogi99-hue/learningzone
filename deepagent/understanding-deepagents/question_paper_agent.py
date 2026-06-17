from utils import get_model
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()
model=get_model()
backend=FilesystemBackend(
    root_dir="./question_paper_workspace",
    virtual_mode=True,
)
web_search=TavilySearch(
    max_results=10,
    Topic="general"
)
reasoning_subagent = {
    "name": "reasoning_subagent",
    "description": "Creates multiple choice questions on logical reasoning, series, analogy, coding-decoding, blood relations, directions and puzzles.",
    "instruction": """
Generate 10 multiple choice questions.
Each question must have:
- Question number
- Four options (A, B, C, D)
- Correct answer
""",
  "tools": [web_search]
}

numerical_subagent = {
    "name": "numerical-agent",
    "description": "Creates multiple choice questions on numerical aptitude.",
    "instruction": """
Generate 10 MCQs covering:
- Percentages
- Profit and Loss
- Ratio and Proportion
- Average
- Time and Work
- Speed, Time and Distance

Each question must contain:
- Four options
- Correct answer
""",
  "tools": [web_search]
}

english_subagent = {
    "name": "english_subagent",
    "description": "Creates English language MCQs.",
    "instruction": """
Generate 10 MCQs covering:
- Grammar
- Synonyms
- Antonyms
- Vocabulary
- Error Detection
- Sentence Completion

Each question must include:
- Four options
- Correct answer
""",
  "tools": [web_search]
}

gk_subagent = {
    "name": "gk_subagent",
    "description": "Creates General Knowledge questions related to India.",
    "instruction": """
      Generate 10 MCQs covering:
  - Indian History
  - Geography
  - Constitution
  - Important Personalities
  - National Symbols
  - Current static GK of India

  Each question must include:
  - Four options
  - Correct answer
""",
  "tools": [web_search]
}

science_subagent = {
        "name": "science_subagent",
        "description": "Creates Basic Science MCQs.",
        "instruction": """
Generate 10 MCQs covering:
 - Physics
 - Chemistry
 - Biology
 - Environment
 - Human Body

Each question must include:
 - Four options
 - Correct answer
""",
  "tools": [web_search]
}

agent= create_deep_agent(
    model=model,
    backend=backend,
    system_prompt="""
You are responsible for creating 50 multiple choice questions on
reasoning
numeriacal-Ability
English
GeneralKnowledge of India
basic Science

You have access to subagents, where you can delegate the work
Ensure you create todos first and store in /todos.md
Capture the response from every subagent and save in /<subagent-name>.md

Store the final question paper in /questions.md

Ensure the final output is in standard markdown format.
"""
)

if __name__ == "__main__":
    result = agent.invoke(
        input={
            "messages": [
                {
                    "role": "user",
                    "content": "I need 50 questions with 10 each on reasoning, numerical-ability, english, gk and science for a competitive exam level-1."
                }
            ]
        }
    )

    print(result["messages"][-1].content)