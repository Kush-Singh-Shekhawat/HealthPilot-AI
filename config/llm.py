from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import GOOGLE_API_KEY, LLM_MODEL

llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2,
    max_retries=3,
)