import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0,
    vertexai=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT")
)

response = llm.invoke([
    HumanMessage(content="What is the capital of France?")
])

print(response.content)