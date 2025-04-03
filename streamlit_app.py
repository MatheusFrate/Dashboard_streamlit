import streamlit as st
import requests 
import pandas as pd

pages = {
    "Dashboard": [
        st.Page("./streamlit_pages/dashboard.py", title="Dashboard"),      
    ],
}
pages_with_df ={
"Dashboard": [
        st.Page("./streamlit_pages/dashboard.py", title="Dashboard"),
        st.Page("./streamlit_pages/randomizer.py", title="Randomizador"),
        st.Page("./streamlit_pages/rss.py", title="rss"),
        
    ],
}

st.set_page_config(layout="wide")
if 'df' in st.session_state:
    pg = st.navigation(pages_with_df)
    pg.run()
else:
    pg = st.navigation(pages)
    pg.run()


