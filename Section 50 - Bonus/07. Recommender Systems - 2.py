# https://chat.openai.com/share/f079061e-13c9-4ae6-bb33-fd766e0baaff

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

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

# Create user and movie tensors
user_tensor = torch.LongTensor(user_ids)
movie_tensor = torch.LongTensor(movie_ids)

# Create user and movie embedding layers
user_embedding = nn.Embedding(num_users, embedding_dim)
movie_embedding = nn.Embedding(num_movies, embedding_dim)

# Define the matrix factorization model
class MatrixFactorization(nn.Module):
    def __init__(self, num_users, num_movies, embedding_dim):
        super(MatrixFactorization, self).__init__()
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        self.movie_embedding = nn.Embedding(num_movies, embedding_dim)

    def forward(self, user_ids, movie_ids):
        user_embeds = self.user_embedding(user_ids)
        movie_embeds = self.movie_embedding(movie_ids)
        dot_product = torch.sum(user_embeds * movie_embeds, dim=1)
        return dot_product

# Create the model
model = MatrixFactorization(num_users, num_movies, embedding_dim)

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Print model summary
print(model)

# Train the model with your user-movie interaction data
# user_movie_ratings = pd.read_csv('user_movie_ratings.csv')
# user_ids = user_movie_ratings['user_id'].values
# movie_ids = user_movie_ratings['movie_id'].values
# ratings = user_movie_ratings['rating'].values

# Convert user_ids and movie_ids to PyTorch tensors
# user_ids_tensor = torch.LongTensor(user_ids)
# movie_ids_tensor = torch.LongTensor(movie_ids)

# Train the model
# for epoch in range(10):  # Replace with desired number of epochs
#     predicted_ratings = model(user_ids_tensor, movie_ids_tensor)
#     loss = criterion(predicted_ratings, torch.FloatTensor(ratings))
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

# Make recommendations for a specific user
user_id_to_recommend_to = 10  # Replace with the user you want to recommend movies to

# Generate a list of all movie IDs
all_movie_ids = np.arange(num_movies)

# Remove the movies the user has already rated
movies_rated_by_user = []  # Replace with actual data
movies_to_recommend = np.setdiff1d(all_movie_ids, movies_rated_by_user)

# Create input data for recommendations
user_input_data = torch.LongTensor([user_id_to_recommend_to] * len(movies_to_recommend))

# Predict ratings for the user's recommendations
predicted_ratings = model(user_input_data, torch.LongTensor(movies_to_recommend))

# Sort movies by predicted ratings in descending order
movie_ranking = pd.DataFrame({'movie_id': movies_to_recommend, 'predicted_rating': predicted_ratings.detach().numpy()})
movie_ranking = movie_ranking.sort_values(by='predicted_rating', ascending=False)

# Get the top N recommended movies
N = 10  # Number of recommendations to generate
top_n_recommendations = movie_ranking.head(N)

# Print the top N movie recommendations
print(top_n_recommendations)