import streamlit as st
import pickle
import pandas as pd
import requests




def recommend(movies_re):
    index = movies[movies["title"] == movies_re].index[0]
    distances = similarity[index]
    mvie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    
    
    recommend_movie = []
    for i in mvie_list:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie




movies = pickle.load(open('movie_list.pkl','rb'))
movies_lis = movies['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))


st.title("Movie Recommender System")


option = st.selectbox(
    'Select a movie of your choice:',
    movies_lis)

if st.button('Recommend'):
    recomm = recommend(option)
    for i in recomm:
        st.write(i)
    


