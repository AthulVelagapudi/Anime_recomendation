import pickle
import streamlit as st
import pandas as pd

anime_dict =  pickle.load(open('anime.pkl','rb'))
similarity =  pickle.load(open('similarity.pkl','rb'))
anime_list = pd.DataFrame(anime_dict)
anime_values = anime_list['Name'].values

def recommend(anime):
    x = anime_list[anime_list['Name'] == anime].index[0]
    distances = similarity[x]
    animelist = sorted(list(enumerate(distances)), reverse = True,key =lambda x :x[1])[1:6]
    recommended_anime = []
    recommended_anime_poster = []

    for i in animelist:
        recommended_anime.append(anime_list.iloc[i[0]].Name)
        recommended_anime_poster.append(anime_list.iloc[i[0]].image_url)
        #st.text(anime_list.iloc[i[0]].image_url)

    return recommended_anime,recommended_anime_poster

st.title('Anime Recommender System')
selected_anime = st.selectbox(
     'Type or select a anime from the dropdown',
     anime_values)
if st.button('Show Recommendation'):
    recommended_anime_names,recommended_anime_posters = recommend(selected_anime)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_anime_names[0])
        st.image(recommended_anime_posters[0])
    with col2:
        st.text(recommended_anime_names[1])
        st.image(recommended_anime_posters[1])
    with col3:
        st.text(recommended_anime_names[2])
        st.image(recommended_anime_posters[2])
    with col4:
        st.text(recommended_anime_names[3])
        st.image(recommended_anime_posters[3])
    with col5:
        st.text(recommended_anime_names[4])
        st.image(recommended_anime_posters[4])
