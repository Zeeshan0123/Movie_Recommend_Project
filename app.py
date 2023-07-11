import streamlit as st
import pickle
import pandas as pd
import requests
import zipfile
#Using API to fetch posters
def fetch_poster(movie_id):
    respose = requests.get('https://api.themoviedb.org/3/movie/{}'
                 '?api_key=b8d8505bd6929896e6dc50d378b66b86'.format(movie_id))
    data = respose.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']



def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movies_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies,recommended_movies_posters



movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict) # change dictionary to data frame
similarity = pickle.load(open('similarity.pkl','rb')) #read pickle file
# zip_path = './similarity.zip'
#
# # Extract the pickle file from the zip archive
# with zipfile.ZipFile(zip_path, 'r') as zip_file:
#     with zip_file.open('similarity.pkl') as pickle_file:
#         # Load the pickle file
#         similarity = pickle.load(pickle_file)



# GUI design start here

st.set_page_config(page_title="MoviesGem",page_icon=':grapes:',layout='wide')
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title(' :blue[Movie Recommending system] :sunglasses:')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

# st.write('You selected:', selected_movie_name)

if st.button('Recommended'):                      # Button Code
    names,posters = recommend(selected_movie_name)
    # for i in recommendations:
    #     st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

