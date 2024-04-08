import streamlit as st
import pandas as pd
import numpy as np

#Home Page

st.set_page_config(
    page_title="**Music for Mental Health Dashboard**",
    page_icon=" :guitar: :musical_note:",
)

st.title("Welcome in :  ")
st.title(" :musical_note: **Music for Mental Health!** :musical_note: ")

st.balloons()



st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/1_Streaming_Services.py", label="1. Streaming Services ",icon="🎷")
st.page_link("pages/2_Mental_Health.py", label="2. Mental Health ",icon="💽")


