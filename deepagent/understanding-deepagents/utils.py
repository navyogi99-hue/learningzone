"""
This module will have reusable utilities
"""

from langchain.chat_models import BaseChatModel,init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_model() -> BaseChatModel:
    """
    This model returns the llm

    """
    model=init_chat_model(
        model="gemini-3.5-flash",
        project=os.getenv("GOOGLE_CLOUD_PROJECT")
    )
    return model

