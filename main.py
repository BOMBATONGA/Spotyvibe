import spotify_fetch
import gemini_resp
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
import time;
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()
app = Flask(__name__)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    storage_uri="memory://"
)

@app.route("/")
def setup():
    return render_template("index.html")

@app.route("/response")
@limiter.limit("3 per hour; 5 per day")
def get_roast():
    with open("ai_prompt.txt", "r", encoding="utf-8") as file:
        base_prompt = file.read()
    print("File read!")

    try:
        spotify_prompt = spotify_fetch.fetch_data()
        print("Spotify read!")

        data = gemini_resp.generate_response(base_prompt + spotify_prompt)
        print("Data received!")
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"archetype": "ERROR", "diagnosis": "The AI is currently unconscious. Try again later."}), 500
    print(data)
    return data

if __name__ == "__main__":
    app.run(debug=True, port=5050)