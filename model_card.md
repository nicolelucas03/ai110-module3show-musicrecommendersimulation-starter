# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name    
VibeLens 1.0

---

## 2. Intended Use  

VibeLens 1.0 is designed to generate top song recommendations by matching a user’s preferred genre, mood, and target energy to songs in a small catalog.
It assumes the user can describe their taste with a few simple preferences and that these features are enough to approximate what they might enjoy.
The system is built for classroom exploration, so its main goal is to demonstrate how recommendation scoring works in a transparent and explainable way.
It is not intended for real-world deployment, because it uses a limited dataset and simplified logic that cannot capture the full complexity of musical taste.
---

## 3. How the Model Works  

VibeLens 1.0 looks at three main song features: genre, mood, and energy level. It compares those features to the user profile, which includes a preferred genre, preferred mood, and a target energy value. 
Each song gets a score by earning points for matching genre and mood, then additional points based on how close its energy is to the user’s target energy. After scoring every song, the system ranks them from highest to lowest and returns the top results as recommendations.  
Compared with the starter structure, my version emphasizes clear, human-readable reasons for each score so it is easy to understand why a song appeared near the top.
---

## 4. Data  

The dataset in songs.csv contains 18 songs total, so it is intentionally small and easy to inspect for classroom testing.  
It includes a fairly broad mix of genres (15 unique labels, including pop, lofi, rock, ambient, jazz, synthwave, metal, folk, and more) and moods (14 unique labels, including happy, chill, intense, relaxed, and melancholic), but some labels appear more often than others.  
I add 8 more songs with different variety to the orginal dataset. Even with variety, the data still misses many parts of real musical taste, such as language preference, lyrical themes, cultural context, era, and personal listening history.  
Because of that limited coverage, recommendations can look reasonable for simple vibe matching but may not generalize well to more complex or niche user tastes.
---

## 5. Strengths  

The recommender seems strongest for users with clear, single-vibe preferences, such as high-energy pop or chill lofi listeners.  
It captures an intuitive pattern. Exact genre and mood matches usually rise to the top, and songs with closer energy values are ranked higher within that group. In my tests, this often matched expectations, like upbeat profiles getting energetic tracks and calm profiles getting softer tracks. Another strength is transparency, because each recommendation includes clear reasons that explain why the song scored well. This makes the system easy to debug, easy to trust in a classroom setting, and useful for learning how recommendation tradeoffs work.
---

## 6. Limitations and Bias 

My recommender can create a filter bubble because it gives large bonuses to exact genre and mood matches, so it keeps surfacing songs that look similar to what the user already liked. It also ignores some user preferences, like acoustic style, which mean users with those tastes are not fully represented in the ranking. The energy-gap formula can unintentionally flatten differences when a user enters extreme energy values, causing many songs to receive similar energy scores. 

If a user input is missing or inconsistent, fallback behavior can bias result toward lower-energy tracks instead of reflecting true intent. Overall, the system is transparent and easy to explain, but it can overfit to a narrow profile and under-serve users with more nuanced or atypical preferences. 

---

## 7. Evaluation  

I evaluated the recommender using several profiles, such as High-Energy Pop, Chill Lofi, Deep Intense Rock, as well as adversarial profiles called Case-Mismatch Trap and Out-of-Range Energy. 

For each profile, I checked whether the top five songs matches the intended vibe in genre, mood, and energy, and whether the explanation reasons made sense with the final scores. I was surprised that small input differences like capitalization chnages could remove genre or mood matches, and that extreme energy values made many songs look similarly scored on energy. 
I also compared outputs across similar profiles to see if the same songs repeatedly dominated, which helped reveal filter-bubble behavior from heavy genre and mood weighting.


- High-Energy Pop vs Chill Lofi: The output shifted from upbeat pop tracks to calmer lofi songs because the profile changed both category targets and the preferred energy range from high to low.
- High-Energy Pop vs Deep Intense Rock: Recommendations moved from bright pop songs to more aggressive tracks, which makes sense because mood and genre priorities changed while both profiles still favored high energy.
- High-Energy Pop vs Case-Mismatch Trap: The Case-Mismatch output was weaker and less intuitive because capitalization differences prevented exact genre and mood matches, so energy contributed more of the score.
- High-Energy Pop vs Out-of-Range Energy: Out-of-Range Energy produced less meaningful separation by vibe because extreme target energy flattened energy scoring, leaving category matches to dominate.
- Chill Lofi vs Deep Intense Rock: The top songs changed sharply because these profiles represent opposite listening intents, with low-energy relaxed preferences versus high-energy intense preferences.
- Chill Lofi vs Case-Mismatch Trap: Chill Lofi gave coherent chill results, while Case-Mismatch looked noisier because strict string matching removed intended categorical boosts.
- Chill Lofi vs Out-of-Range Energy: Chill Lofi kept low-energy songs near the top, but Out-of-Range Energy reduced the importance of true energy closeness and relied more on exact category matches.
- Deep Intense Rock vs Case-Mismatch Trap: Deep Intense Rock prioritized forceful high-energy songs, while Case-Mismatch often failed to lock onto the intended vibe due to formatting-sensitive inputs.
- Case-Mismatch Trap vs Out-of-Range Energy: Both profiles stress robustness, but for different reasons: Case-Mismatch tests text normalization and Out-of-Range tests numeric handling and score flattening under extreme values.
---

## 8. Future Work  

A strong future direction for VibeLens 1.0 is to add more user preference controls, such as acousticness, tempo range, and valence, so recommendations better reflect different listening styles.  
I would also improve robustness by normalizing inputs (for example, handling capitalization and spacing) and validating energy values so minor formatting issues do not break intended matches.  
To reduce filter-bubble effects, I would add a simple diversity step that ensures the top results include a mix of genres or moods instead of only the highest-scoring near-duplicates.  
For explainability, I would expand the recommendation reasons to show both positive and negative factors, so users can understand not just why a song ranked high but also what held others back.  
Lastly, I would evaluate the model on a larger and more representative song dataset and test multi-interest user profiles, because real listeners usually have broader tastes than a single fixed vibe.
---

## 9. Personal Reflection  

Building VibeLens 1.0 taught me that even a simple recommender can feel convincing when the scoring logic is clear and the results are easy to explain. One thing I found surprising was how sensitive the system was to small input differences, like capitalization, and how much those tiny formatting issues could change ranking outcomes.  
I also learned that weighting choices can quietly create filter bubbles, especially when exact genre and mood matches dominate the score.  
This project changed how I think about music apps by showing me that recommendations are not just about prediction quality, but also about fairness, robustness, and how much user intent is actually captured.  Using Copilot as my AI agent helped brainstorm and check different scenarios and edge cases to make sure the system worked on different use cases without getting "tricked". 
This project made me appreciate why real recommendation systems need both strong data coverage and careful design decisions beyond a single scoring formula.