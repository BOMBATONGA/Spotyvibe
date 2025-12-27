from google import genai
from dotenv import load_dotenv
import os


def get_auth():
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    return client

def generate_response(main_prompt):
    load_dotenv(override=True)
    client = get_auth()
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=main_prompt
    )
    print(response.text)