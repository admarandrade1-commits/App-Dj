from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import openpyxl
import os
import random

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

def load_songs():
    wb = openpyxl.load_workbook("songs.xlsx")
    ws = wb.active
    songs = []
    for i, row in enumerate(ws.iter_rows(min_row=2, values_only=True)):
        songs.append({
            "id": row[0],
            "title": row[1],
            "artist": row[2],
            "bpm": row[3],
            "energy": row[4],
            "votes": 0
        })
    return songs

songs = load_songs()
current_song = {"title": "Music Is Math", "artist": "Boards of Canada", "bpm": 125, "energy": 0.65}

@app.route("/")
def index():
    return render_template("index.html", current_song=current_song, songs=songs)

@app.route("/songs")
def get_songs():
    return jsonify(songs)

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
