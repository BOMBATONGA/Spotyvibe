import spotify_fetch
import gemini_resp
from flask import Flask, render_template, jsonify

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

    print(data)
    return data

if __name__ == "__main__":
    app.run(debug=True, port=5050)