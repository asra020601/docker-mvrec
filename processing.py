# data_processing.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies = pd.read_csv("https://raw.githubusercontent.com/MahnoorJaved98/Movie-Recommendation-System/main/movie_dataset.csv")

def load_and_preprocess():
    
    features = ["keywords", "cast", "director", "genres"]
    for feature in features:
        # Replace pipes with spaces and fill missing values
        movies[feature] = (
            movies[feature]
            .fillna("")
            .str.replace("|", " ", regex=False)  # Split multi-term values
        )
    
    # Combine features efficiently
    movies["Combined_Features"] = movies[features].apply(
        lambda row: " ".join(row), axis=1
    )
    
    # Case-insensitive vectorization
    cv = CountVectorizer(lowercase=True)
    count_matrix = cv.fit_transform(movies["Combined_Features"])
    cosine_sim = cosine_similarity(count_matrix)
    
    return movies, cv, cosine_sim

# Initialize these when the module is imported
movies, cv, cosine_sim = load_and_preprocess()

def get_movie_index(title: str):
    # Use the title parameter instead of asking for input
    try:
        # Look for the movie title in the 'title' column
        # and return its dataframe index
        return movies.index[movies.title == title].tolist()[0]
    except IndexError:
        print(f"Movie '{title}' not found.")
        return -1
def get_movie_title(index):
    return movies[movies.index == index]["title"].values[0]

