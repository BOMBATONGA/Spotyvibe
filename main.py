import spotify_fetch
import gemini_resp

with open("ai_prompt.txt", "r", encoding="utf-8") as file:
    base_prompt = file.read()
print("File read")

spotify_prompt = spotify_fetch.fetch_data()
print("Spotify read")

gemini_resp.generate_response(base_prompt + spotify_prompt)