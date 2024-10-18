import pickle as pk
import streamlit as st


# Load the data
with open("dt.pkl", 'rb') as f:
    data = pk.load(f)

with open("music.pkl", 'rb') as f:
    pattern = pk.load(f)


def recommender(song_name):
    idx = data[data['song'] == song_name].index[0]  # This line finds the index of the input song in the DataFrame df.
    distance = sorted(list(enumerate(pattern[idx])), reverse=True, key=lambda x: x[1]) # passing the similarity array into the list
    song = []
    for s in distance[1:5]:
        song.append(data.iloc[s[0]].song)
    return song

st.header("Music Recommender System")

select = st.selectbox("select song from the dropdown", data.song.values)

if st.button("Display recommended Songs"):
    recommendations = recommender(select)
    for song in recommendations:
        st.text(song)

