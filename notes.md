**Collaborative Filtering**

- Core Idea: "Users like you also loved this" 

- Finds patterns in behavior across users 

How it Works: 
- Build a giant matrix: rows = users, columns = songs, values = play counts / ratings 
- Find users with similar listening histories (user-user) or find songs that tend to be listened to together (item-item)
- Recomend what similar users liked that you haven't heard 

Pros: 
- Discovers surpirsing, cross-genre gems 
- No need to analyze audio content 
- Improves as data grows 

Cons: 
- Cold start problem - new users or new songs have no history 
- popularity bias - niche artists get buried 
- privacy-sensitive (requires user behavior data)

**Content-Based Filtering** 
- Core Idea: "You liked songs that sound like this, so here's more like this" 
- Analyzes the attributes of the content itself 

How it Works: 
- Extract features from songs: tempo, key, energy, danceability, vocal style, genre tags, lyrics 
- Build a profile of what the user likes based on features of songs they've played 
- Recommend songs with similar feature vectors

Pros: 
- Works for new users (only needs their own history)
- Works for new songs (no listening data needed)
- Explainable: "Recommended because it's similar to X" 

Cons: 
- Filter bubble - tends to recommend more of the same, less serendipity 
- Requires a rich metadata or audio analysis 
- Can't capture cultural/social dimensions of music taste

**Spotify and YouTube** 
- Both use hybrid models that combines multiple appoaches: 
  - Collaborative filtering 
  - Content-based filtering 
  - Deep learning on audio 
  - NLP on lyrics/playlist 
  - Session context 
  - Social graph 

Spotify's Discover Weekly uses a blend of: 
- Matrix factorization 
- NLP on playlist co-occurrence 
- Audio CNNs

**Main data types involved in Spotify/YouTube** 

Song/Item Data
- Identifiers (song ID, artist ID)
- Categorical (genre, mood, language)
- Continuous floats (energy, tempo, valence)
- Continuous floats (energy, tempo, valence)
- Boolean flags (explicit, acoustic)
- Embeddings (audio features from neural nets)

User Data 
- Preference (favorite genre, mood)
- Behavioral signals (play count, skip rate, saves)
- Implicit feedback (listen duration, replays)
- User embedding (compressed taste vector)

**Feature Recommendations based on songs.csv**
Most effective features 
- mood + genre (categorical)
- energy + acousticness
- temp_bpm 

Less effective features 
- valence 
- danceability 
- title/artist 

For a simple cosine similarity recommender, I'd use: 
[genre (one-hot), mood (one-hot), energy, acousticness, tempo_bpm (normalized)]

**Scoring Rule Design for Content-Based Learning** 
- Key Insight: Measure similarity/distance rather than ranking by absolute values. 

1. Gaussian/Normal Distribution Scoring 

**Scoring Rule vs Ranking Rule** 
Scoring Rule: "How well does this song match the user's preference?" 
- Evaluates one song at a time 
- Output: Single numerical score per song 
- Example: Song A = 0.85, Song B: 0.92

Ranking Rule: "In what order should we show these songs to the user?" 
- Operates on multple scored songs 
- Ordered list with selection logic 
- Example: "Show top 10, but ensure 80% match high scores and 20% are discovery picks" 


**Creating a User Profile** 
- recommender will use this as the taste anchor for comparisons

Core profile:
{
  favorite_genre: jazz,
  favorite_mood: happy,
  target_energy: 0.75,
  likes_acoustic: True,
}

Optional expansion for a richer recommender:
{
  secondary_genres: ["lofi", "indie pop"],
  energy_tolerance: 0.15,
  openness_to_discovery: 0.30,
}

**Algorithm Recipe** 
score=2.0⋅1(genre match)+1.0⋅1(mood match)+2.0⋅energy_sim 

where: 
energy_sim=1−min(∣song_energy−target_energy∣, 1)


**Visualize the Design**
Input: User Prefs
- favorite_genre 
- favorite_mood 
- target_energy 
- likes_acoustic 

Process: The Loop
- For each song in the CSV: 
    - Compare song.genre to favorite_genre
    - Compare song.mood to favorite_mood 
    - Measure how close song.energy is to target_energy 
    - Can include other features like tempo, valence, danceability, acousticness 
    - Compute one total score for that song 
- Repeat for every song in the dataset 
- Store each song with its score

Output: The Ranking 
- Sort all songs from highest score to lowest score 
- Return the top K songs 
- Optionally include a short explanation for why each song ranked well 


flowchart LR
    A[Input: User Prefs]
    A1[favorite_genre]
    A2[favorite_mood]
    A3[target_energy]
    A4[likes_acoustic]

    B[Process: The Loop]
    C[For each song in songs.csv]
    D[Compare genre to favorite_genre]
    E[Compare mood to favorite_mood]
    F[Measure energy closeness]
    G[Optional: tempo, valence, danceability, acousticness]
    H[Compute total score]
    I[Store song + score]

    J[Output: The Ranking]
    K[Sort all songs by score]
    L[Return Top K recommendations]
    M[Optional: short explanation]

    A --> A1
    A --> A2
    A --> A3
    A --> A4

    A1 --> B
    A2 --> B
    A3 --> B
    A4 --> B

    B --> C --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M