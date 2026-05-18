from flask import Flask, render_template, request, jsonify, session, redirect
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import random

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope="user-read-currently-playing"
)

# Lista de músicas (vamos expandir depois)
songs = [
    {"id": 1, "title": "Strobe", "artist": "deadmau5", "bpm": 128, "energy": 0.6, "votes": 0},
    {"id": 2, "title": "Around The World", "artist": "Daft Punk", "bpm": 121, "energy": 0.8, "votes": 0},
    {"id": 3, "title": "One More Time", "artist": "Daft Punk", "bpm": 123, "energy": 0.9, "votes": 0},
    {"id": 4, "title": "Levels", "artist": "Avicii", "bpm": 126, "energy": 0.7, "votes": 0},
    {"id": 5, "title": "Blue (Da Ba Dee)", "artist": "Eiffel 65", "bpm": 136, "energy": 0.85, "votes": 0},
]

current_song = {"title": "Music Is Math", "artist": "Boards of Canada", "bpm": 125, "energy": 0.65}

@app.route("/")
def index():
    return render_template("index.html", current_song=current_song, songs=songs)

@app.route("/vote/<int:song_id>", methods=["POST"])
def vote(song_id):
    for song in songs:
        if song["id"] == song_id:
            song["votes"] += 1
    return jsonify({"success": True, "votes": next(s["votes"] for s in songs if s["id"] == song_id)})

@app.route("/recommend")
def recommend():
    compatible = [
        s for s in songs
        if abs(s["bpm"] - current_song["bpm"]) <= 20
        and abs(s["energy"] - current_song["energy"]) <= 0.20
    ]
    recommended = random.sample(compatible, min(3, len(compatible)))
    return jsonify(recommended)

if __name__ == "__main__":
    app.run(debug=True)
