from scipy.spatial.distance import euclidean

#returns full cols of movies, movie is a string title, df pickle
def find_similar_movies_by_genre(movie, df, k=10):
    # Convert the movie input to lowercase and match against the dataframe titles (also in lowercase)
    movie_cluster = df.loc[df['title'].str.lower() == movie.lower(), 'genre_cluster'].iloc[0]
    combined_genres_input = df.loc[df['title'].str.lower() == movie.lower(), 'combined_genres'].iloc[0]
    
    clustered_movies = df[df['genre_cluster'] == movie_cluster]
    
    # Calculate distance for each movie
    clustered_movies['distance'] = clustered_movies['combined_genres'].apply(
        lambda x: euclidean(combined_genres_input, x)
    )
    
    # Get the top k similar movies
    similar_movies = clustered_movies.nsmallest(k, 'distance')
    
    print("done")
    return similar_movies[['title', 'distance']]


def find_similar_movies_by_summary(movie, df, k=10):
    # Convert the movie input to lowercase and match against the dataframe titles (also in lowercase)
    movie_cluster = df.loc[df['title'].str.lower() == movie.lower(), 'overview_cluster'].iloc[0]
    combined_summary_input = df.loc[df['title'].str.lower() == movie.lower(), 'embedded_overview'].iloc[0]
    
    cluster_movies = df[df['overview_cluster'] == movie_cluster]
    
    # Calculate distance for each movie
    cluster_movies['distance'] = cluster_movies['embedded_overview'].apply(
        lambda x: euclidean(combined_summary_input, x)
    )
    
    # Get the top k similar movies
    similar_movies = cluster_movies.nsmallest(k, 'distance')
    
    return similar_movies[['title', "distance"]]


def find_similar_movies_by_keywords(movie, df, k=10):
    # Convert the movie input to lowercase and match against the dataframe titles (also in lowercase)
    movie_cluster = df.loc[df['title'].str.lower() == movie.lower(), 'keyword_cluster'].iloc[0]
    combined_keyword_input = df.loc[df['title'].str.lower() == movie.lower(), 'combined_keywords'].iloc[0]
    
    cluster_movies = df[df['keyword_cluster'] == movie_cluster]
    
    # Calculate distance for each movie
    cluster_movies['distance'] = cluster_movies['combined_keywords'].apply(
        lambda x: euclidean(combined_keyword_input, x)
    )
    
    # Get the top k similar movies
    similar_movies = cluster_movies.nsmallest(k, 'distance')
    
    return similar_movies[['title', 'distance']]
