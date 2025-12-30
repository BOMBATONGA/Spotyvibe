from google import genai
from dotenv import load_dotenv
import os
import json


def get_auth():
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    return client

def generate_response(main_prompt):
    #Actual generation code (disabled to not waste tokens)
    load_dotenv(override=True)
    client = get_auth()
    
    print("Generating response...")
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=main_prompt
    )

    print("Unpackaging json...")
    clean_json = response.text.replace("```json", "").replace("```", "").strip()
    return json.loads(clean_json)
    return data