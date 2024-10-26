import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_poster_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_poster_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetching the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header("Movie Recommendations Systems HD")
movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))


selected_movie_name = st.selectbox(
    'Enter Movie Name : ',
    movies['title'].values)

if st.button('Display Recommends'):
    recommends_movie_titles, recommends_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommends_movie_titles[0])
        st.image(recommends_movie_posters[0])
    with col2:
        st.text(recommends_movie_titles[1])
        st.image(recommends_movie_posters[1])
    with col3:
        st.text(recommends_movie_titles[2])
        st.image(recommends_movie_posters[2])
    with col4:
        st.text(recommends_movie_titles[3])
        st.image(recommends_movie_posters[3])
    with col5:
        st.text(recommends_movie_titles[4])
        st.image(recommends_movie_posters[4])

#this is a comment 
