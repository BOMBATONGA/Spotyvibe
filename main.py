import spotify_fetch
import gemini_resp
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request, redirect, url_for
import time;
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

load_dotenv(override=True)
app = Flask(__name__)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    storage_uri="memory://"
)
app.secret_key = os.getenv("FLASK_KEY")

@app.route("/login")
def login():
    auth_manager = spotify_fetch.create_auth_manager()
    auth_url = auth_manager.get_authorize_url()
    return redirect(auth_url)

@app.route("/callback")
def callback():
    auth_manager = spotify_fetch.create_auth_manager()
    auth_manager.get_access_token(request.args.get("code"))
    return redirect(url_for("setup"))

@app.route("/")
def setup():
    return render_template("index.html")

@app.route("/response")
@limiter.limit("3 per hour; 5 per day")
def get_roast():
    is_demo = request.args.get('mode') == 'demo'
    
    if is_demo:
        return jsonify({
            "patient_name": "Alex Miller",
            "archetype": "Performative Recluse",
            "diagnosis": "Your playlist is a meticulously curated exhibition of 'obscure' indie-folk designed to signal a depth of soul that your shallow interpersonal history proves you do not possess. This relentless commitment to being 'misunderstood' ensures that any potential partner will eventually realize there is no authentic self beneath your layers of reverb-drenched posturing.",
            "red_flag_percent": 94,
            "red_flag_comment": "Your social circle consists entirely of people you are secretly competing with for the title of 'Most Tortured Creative.'",
            "vibe_age": 14,
            "vibe_age_comment": "You possess the emotional maturity of a teenager who believes staring out of a rainy bus window constitutes a personality trait.",
            "final_burn": "Stop romanticizing your inability to maintain a stable text thread; it’s not a tragedy, it’s a symptom."
        })
    
    

    try:
        spotify_prompt = spotify_fetch.fetch_data()
        print("Spotify read!")

        if spotify_prompt == None:
            auth_manager = spotify_fetch.create_auth_manager()
            return jsonify({"auth_url": auth_manager.get_authorize_url()}), 401
        
        with open("ai_prompt.txt", "r", encoding="utf-8") as file:
            base_prompt = file.read()
        print("File read!")

        data = gemini_resp.generate_response(base_prompt + spotify_prompt)
        print("Data received!")

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"archetype": "ERROR", "diagnosis": "The AI is currently unconscious. Try again later."}), 500
    
    print(data)
    return data

if __name__ == "__main__":
    app.run(debug=True, port=5050)