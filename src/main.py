"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}") 

    # Distinct user profiles for quick experiments.
    user_profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.92},
        
        "Case-Mismatch Trap": {"genre": "Pop", "mood": "Happy", "energy": 0.82},
        "Out-of-Range Energy": {"genre": "pop", "mood": "happy", "energy": 9.0},
    }

    # Pick one profile to run.
    profile_name = "High-Energy Pop"
    user_prefs = user_profiles[profile_name]
    print(f"\nProfile: {profile_name}")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for index, rec in enumerate(recommendations, start=1):
        song, score, reasons = rec
        print(f"[{index}] {song['title']}")
        print(f"    Final score: {score:.2f}")
        print("    Reasons:")
        for reason in reasons:
            print(f"      - {reason}")
        print("-" * 50)

if __name__ == "__main__":
    main()
