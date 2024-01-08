import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import joblib

# Load the data
@st.cache_data  # Cache the data loading for better performance
def load_data():
    return pd.read_csv('only_embeddings_df.csv')

# Load the trained model
@st.cache_data  # Cache the model for better performance
def load_model():
    return joblib.load('nearest_neighbors_model.pkl')

# Title and description
st.title('Movie Recommender System')
st.write('Enter a movie title to get recommendations.')

# Load data and model
movies_data = load_data()
model = load_model()

# User input for movie title
movie_title = st.text_input('Enter a movie title', 'The Matrix')

# Convert input to lowercase and replace spaces with hyphens
formatted_title = movie_title.lower().replace(' ', '-')

# Finding recommendations
if st.button('Get Recommendations'):
    # Finding the index of the entered movie title
    movie_index = movies_data[movies_data['movie_id'] == formatted_title].index.tolist()[0]
    
    # Remove the 'movie_id' column before querying the NearestNeighbors model
    query_data = movies_data.drop(columns=['movie_id'])
    
    # Using the model to get nearest neighbors
    distances, indices = model.kneighbors([query_data.iloc[movie_index].values])
    
    recommended_indices = indices.flatten()
    
    st.write('Recommended Movies:')
    for i in range(len(recommended_indices)):
        if i < 10:
            movie_id = movies_data.iloc[recommended_indices[i]]['movie_id']
            # Capitalize first letters and replace dashes with spaces
            formatted_movie_id = ' '.join(word.capitalize() for word in movie_id.split('-'))
            st.write(f"{i+1}: {formatted_movie_id}")