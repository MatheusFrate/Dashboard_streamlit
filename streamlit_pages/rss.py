import feedparser
import pandas as pd
import streamlit as st
import requests

nome = st.session_state['nome']
rss_url = f"https://myanimelist.net/rss.php?type=rw&u={nome}"

feed = feedparser.parse(rss_url)
st.title(feed.feed.title)

rss_items = []
names = []
for entry in feed.entries:
    rss_items.append({
        "title": entry.title,
        "link": entry.link,
        "description": entry.description,
        "published": entry.published
    })
    names.append(entry.title.split(' - ')[0])
num_cols = 5

params = {
    "names": names
}
response = requests.get(f'http://mal-datadashboard.onrender.com/api/get_anime_data/', params=params).json()

for i in range(0, len(rss_items), num_cols):
    cols = st.columns(num_cols)  
    for idx, (col, item) in enumerate(zip(cols, rss_items[i:i+num_cols])):
        with col:
            st.markdown(
                f"""
                <a href="{item['link']}" target="_blank" style="text-decoration: none;">
                    <div style="
                        border: 1px solid #ddd; 
                        border-radius: 10px; 
                        padding: 0; 
                        background: linear-gradient(to top, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.1)), 
                                    url('{response[i + idx]}') center/cover no-repeat; 
                        height: 300px; 
                        display: flex; 
                        flex-direction: column; 
                        justify-content: flex-end; 
                        color: white; 
                        text-shadow: 1px 1px 5px rgba(0,0,0,0.7);
                    ">
                        <div style="padding: 20px;">
                            <h3>{item['title']}</h3>
                            <p> {item['description']}</p>
                        </div>
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )

