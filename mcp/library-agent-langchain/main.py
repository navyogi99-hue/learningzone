from langchain_core.messages import SystemMessage, HumanMessage
from langchain.agents import create_agent
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import asyncio
from langchain_mcp_adapters.client import MultiserverMCPClient
load_dotenv()
project = os.getenv("GOOGLE_CLOUD_PROJECT")

async def main():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        vertexai = True,
        project = project
    )
    client = MultiserverMCPClient({
        "library-mcp":{
            "transport": "http",
            "url": "http://localhost:19000/mcp"
        }
    })
    tools = await client.get_tools()
    agent = create_agent(llm, tools)


    result = await llm.ainvoke("""Get most popular book details on electrical engineering books
    i need title isbn in 13 digit format, published year, author""")
    print(result.content)
    books_to_be_added = result.content

    
    result = await agent.invoke({
    #    "messages": "Add the following book to the library using  library mcp  {'book_id':'B011','title':'The Power of Habit','author':'Charles Duhigg','published_year':2012,'available_copies':6,'total_copies':10,'genre':'Self Help','available':True,'active':True,'tags':['habits','productivity','self-improvement'],'isbn':'9780812981605'}" 
            "messages": [HumanMessage(content=f"Add 3 copies of the each book mentioned in here {books_to_be_added} using library1 mcp")] 
    })
    print(result)
if __name__ == "__main__":
    asyncio.run(main())
