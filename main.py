import spotify_fetch
import gemini_resp
from flask import Flask, render_template, jsonify
import time;

app = Flask(__name__)

@app.route("/")
def setup():
    return render_template("index.html")

@app.route("/response")
def get_roast():
    with open("ai_prompt.txt", "r", encoding="utf-8") as file:
        base_prompt = file.read()
    print("File read!")

    spotify_prompt = spotify_fetch.fetch_data()
    print("Spotify read!")

    data = gemini_resp.generate_response(base_prompt + spotify_prompt)
    print("Data received!")
    '''
    data = {
        "patient_name": "BOOBO",
        "archetype": "The Pretentious Minimalist",
        "diagnosis": "You transition from aggressive Berlin techno to 'undiscovered' 70s folk just to prove you have layers, but it really just proves you lack a consistent personality. This constant need to be 'the person with the interesting taste' is exactly why your dates never text you back after the first car ride.",
        "red_flag_percent": 94,
        "red_flag_comment": "94% indicates that your music taste is less of a hobby and more of a complex defensive mechanism to avoid actual human intimacy.",
        "vibe_age": "Mid-Life Crisis at 21",
        "vibe_age_comment": "You have the jaded cynicism of a retired detective despite the fact that you still haven't figured out how to do your own laundry.",
        "final_burn": "You’re not 'deep,' you’re just difficult to talk to."
    }'''
    print(data)
    return data

if __name__ == "__main__":
    app.run(debug=True, port=5050)