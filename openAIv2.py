from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

talk = input("Enter your question:")

api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key= api_key)

result = chat_model.predict("hi!")

print(result)