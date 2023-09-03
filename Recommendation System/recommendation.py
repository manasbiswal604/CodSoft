import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies_data = pd.read_csv('D:\Courses and Internships\CodSoft\Recommendation System\movies.csv')

selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

combined_features = movies_data[selected_features].apply(lambda x: ' '.join(x), axis=1)

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

similarity = cosine_similarity(feature_vectors)

movie_name = input('ENTER YOUR FAVORITE MOVIE NAME: ')

find_close_match = difflib.get_close_matches(movie_name, movies_data['title'].tolist())
close_match = find_close_match[0]

index_of_the_movie = movies_data[movies_data['title'] == close_match].index[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

print('MOVIES SUGGESTED FOR YOU:')
for i, movie in enumerate(sorted_similar_movies):
    index = movie[0]
    title_from_index = movies_data.loc[index, 'title']
    if i < 30:
        print(i + 1, '.', title_from_index)
    else:
        break
