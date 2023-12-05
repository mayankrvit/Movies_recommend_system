import streamlit as st
import pickle
import requests
import pandas as pd
import numpy as np
import json

movies_df = pickle.load(open('movies_df.pkl','rb'))

similarity_score = pickle.load(open('similarity_score_df','rb'))

movies_name_list = movies_df['title'].values


# get movies poster

import requests

# this will fail when there is no image no image in database while using apis
 
# def fetch_poster(movie_id):
#     url = 'https://api.themoviedb.org/3/movie/{}?language=en-US'.format(movie_id)
#     headers = {
#     'Accept': 'application/json',
#     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMTFhMmVjOTUzNDFlNWFjYjNmNTJhNTkwYmE0MmMyOSIsInN1YiI6IjY1NGIxNjBhNjdiNjEzMDBlNWRjNTI0NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QfeSsm_X8Go05ZVkI1DgLisEPHa4PXMU33z3snuYTV4'
# }
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     a = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#     return a

# Another apporch

import os
default_image_path = r"C:\Python Project\movies_recommendation\movies_recommendation\No_image_available.png"


# Define the default image path as a variable
DEFAULT_IMAGE_PATH = r"C:\Python Project\movies_recommendation\movies_recommendation\No_image_available.png"

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?language=en-US'.format(movie_id)
    headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMTFhMmVjOTUzNDFlNWFjYjNmNTJhNTkwYmE0MmMyOSIsInN1YiI6IjY1NGIxNjBhNjdiNjEzMDBlNWRjNTI0NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QfeSsm_X8Go05ZVkI1DgLisEPHa4PXMU33z3snuYTV4'
}
    response = requests.get(url, headers=headers)
    data = response.json()
    if data['poster_path'] is not None:
        a = "https://image.tmdb.org/t/p/w500/" + data['poster_path']  
    else:
        a = default_image_path
    return a


# def fetch_poster(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US'
#     headers = {
#         'Accept': 'application/json',
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQi...YTV4'
#     }
#     response = requests.get(url, headers=headers)
#     data = response.json()
    
#     if 'poster_path' in data :
#         poster_url = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#     else:
#         # If poster_path is empty or None, use the default image from the project directory
#         poster_url = default_image_path
    
#     return poster_url


def rm(Select_Movie):
    selected_movie_data =  movies_df[movies_df['title'] == Select_Movie]
    
    movie_index = selected_movie_data.index[0]
    
    #movie_id = selected_movie_data['id'][0] this will give single id
    
    c = sorted(list(enumerate(similarity_score[movie_index])), reverse = True, key = lambda x:x[1])[1:7]
    recommand_movies = []
    rm_movies_poster  = []
    for i in c:
        movie_id = movies_df.iloc[i[0]].id
        recommand_movies.append(movies_df.iloc[i[0]].title)        
        rm_movies_poster.append(fetch_poster(movie_id))
    
    return recommand_movies, rm_movies_poster
    



# ----------------------------------------------------------------
# web page apperance and web page settings


st.set_page_config(page_title='Movies',page_icon= '🤠', layout='wide' )
st.title('Get Recommend Movies')

# this use for multi select but we need one selection
#st.multiselect('Select_Movie', movies_name_list)


Select_Movie = st.selectbox('Select a movie for similar recommendations', movies_name_list)

name , photo  = rm(Select_Movie)

#-----------------------------------------------------------------

# Remove the above white space    
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)


#-----------------------------------------------------------------
#please wait     

import time 

status_text = st.empty()
status_text.write("Searching for best titles...")
time.sleep(2)
status_text.write("You are on the way....")
time.sleep(3)
status_text.write("Here you go. Enjoy!")   

st.balloons()



# with st.status("Searching for best titles", expanded = True ) as status:
#     time.sleep(2)
#     st.write("You are on the way....")
#     time.sleep(2)
#     st.write('')
#     time.sleep(1)
#     status.update(label="Here you go. Enjoy!", state="complete", expanded=False)


#---------------------------------------------------------------------


a,b,c,d,e,f   = st.columns(6)

with a: 
    #st.markdown(name[0]) #, divider = 'rainbow')
    st.image(photo[0])
    st.markdown(name[0])
with b:
    #st.text(name[1]) #, divider = 'rainbow') 
    st.image(photo[1])
    st.markdown(name[1])
with c:
    #st.text(name[2]) #, divider = 'rainbow') 
    st.image(photo[2])
    st.markdown(name[2])
with d:
    #st.text(name[3]) #, divider = 'rainbow') 
    st.image(photo[3])
    st.markdown(name[3])
with e:
    #st.text(name[4]) #, divider = 'rainbow') 
    st.image(photo[4])
    st.markdown(name[4])
with f:
    #st.text(name[5]) #, divider = 'rainbow') 
    st.image(photo[5])    
    st.markdown(name[5])
    
    





















    
    
    
    
    
    
    
    