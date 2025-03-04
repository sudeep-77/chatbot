import openai
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def get_ai_response(question: str):
    response = await openai.ChatCompletion.acreate( 
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": question}
        ]
    )
    return response["choices"][0]["message"]["content"]
