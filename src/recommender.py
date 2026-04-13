import csv 
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initializes the recommender with a catalog of songs."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top-k recommended songs for a user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a human-readable explanation for a recommendation."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file into a list of typed dictionaries."""
    # TODO: Implement CSV loading logic
    songs = []

    with open(csv_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": int(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores one song against user preferences and returns reasons."""
    target_genre = user_prefs.get("genre", "")
    target_mood = user_prefs.get("mood", "")
    target_energy = float(user_prefs.get("energy", 0.0))

    score = 0.0
    reasons: List[str] = []

    if song.get("genre") == target_genre:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song.get("mood") == target_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    song_energy = float(song.get("energy", 0.0))
    energy_similarity = 1.0 - min(abs(song_energy - target_energy), 1.0)
    energy_points = 2.0 * energy_similarity
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, List[str]]]:
    """Ranks songs by score and returns the top-k recommendations."""
    scored_songs = [(song, *score_song(user_prefs, song)) for song in songs]
    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
