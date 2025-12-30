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
    """load_dotenv(override=True)
    client = get_auth()
    
    print("Generating response...")
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=main_prompt
    )

    print("Unpackaging json...")
    clean_json = response.text.replace("```json", "").replace("```", "").strip()
    return json.loads(clean_json)"""
    
    #Dummy data to save tokens
    data = {
        'stereotype_score': [4, 5, 6], 
        'diagnosis': "This playlist screams 'I spend more time on my computer than in direct sunlight'...", 
        'red_flag_percent': 85, 
        'red_flag_comment': "That 85% isn't just a number; it's the exact percentage of your social interactions that end with someone politely excusing themselves.",
        'vibe_block': 'Coworker', 
        'vibe_block_comment': "You'd rather gnaw off your own limb than be caught listening to 'Today's Top Hits'.", 
        'vibe_age': 17, 
        'vibe_age_comment': "Seventeen is generous; your playlist reads like a freshman trying way too hard.", 
        'final_burn': 'Congratulations, your Spotify Wrapped is a public service announcement for mandatory screen time limits.'
    }
    return data