# https://chat.openai.com/share/f079061e-13c9-4ae6-bb33-fd766e0baaff

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import Embedding, Input, Dot, Flatten
from tensorflow.keras.models import Model

# Load your movie and user data
# movie_data = pd.read_csv('movie_data.csv')
# user_data = pd.read_csv('user_data.csv')

# Example data (replace with your dataset)
num_users = 1000
num_movies = 500
embedding_dim = 30

# Create user and movie ID mappings
user_ids = np.arange(num_users)
movie_ids = np.arange(num_movies)

# Create user and movie input layers
user_input = Input(shape=(1,), name='user_input')
movie_input = Input(shape=(1,), name='movie_input')

# Create user and movie embedding layers
user_embedding = Embedding(input_dim=num_users, output_dim=embedding_dim, name='user_embedding')(user_input)
movie_embedding = Embedding(input_dim=num_movies, output_dim=embedding_dim, name='movie_embedding')(movie_input)

# Compute dot product of user and movie embeddings
dot_product = Dot(axes=1, name='dot_product')([user_embedding, movie_embedding])

# Flatten the result
flat_output = Flatten()(dot_product)

# Create the model
model = Model(inputs=[user_input, movie_input], outputs=flat_output)

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Print model summary
model.summary()

# Train the model with your user-movie interaction data
# user_movie_ratings = pd.read_csv('user_movie_ratings.csv')
# user_ids = user_movie_ratings['user_id'].values
# movie_ids = user_movie_ratings['movie_id'].values
# ratings = user_movie_ratings['rating'].values

# model.fit([user_ids, movie_ids], ratings, epochs=10, batch_size=64, validation_split=0.2)

# Make recommendations for a specific user
user_id_to_recommend_to = 10  # Replace with the user you want to recommend movies to

# Generate a list of all movie IDs
all_movie_ids = np.arange(num_movies)

# Remove the movies the user has already rated
movies_rated_by_user = []  # Replace with actual data
movies_to_recommend = np.setdiff1d(all_movie_ids, movies_rated_by_user)

# Create input data for recommendations
user_input_data = np.full(len(movies_to_recommend), user_id_to_recommend_to)

# Predict ratings for the user's recommendations
predicted_ratings = model.predict([user_input_data, movies_to_recommend])

# Sort movies by predicted ratings in descending order
movie_ranking = pd.DataFrame({'movie_id': movies_to_recommend, 'predicted_rating': predicted_ratings})
movie_ranking = movie_ranking.sort_values(by='predicted_rating', ascending=False)

# Get the top N recommended movies
top_n_recommendations = movie_ranking.head(N)

# Print the top N movie recommendations
print(top_n_recommendations)