import random
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
#qui bisogna cambiare l url se fai un git clone
dataset_string=('C:/Users/andre/venv/MusicxMentalHealth/dataset/MusicNY.csv')

#Page config
st.set_page_config(
    page_title="Music for Mental Health Dashboard",
    page_icon=" :guitar: :musical_note:",
)

st.title("**The best Streaming Services**  :guitar: :musical_note:")

@st.cache_data
# Carica i dati dal file CSV --> utilizza il metodo cache_data per velocizzare i futuri accessi 
def loaddata(datastring):
    df=pd.read_csv(datastring)
    return df




data=loaddata(dataset_string)

    
#data.dropna(inplace=True)   Questo controllo è stato effettuato nell'altro script prima di creare il nuovo csv
all_genre= data['Fav genre'].unique()

on = st.toggle('Visualize Dataset')  #Se si clicca sul toggle vengono mostrati i dati appena letti dal csv
if on:
   st.data_editor(data) 


#Creo 3 tabs nella stessa pagina
tab1,tab2, tab3= st.tabs(["Best Streaming service","All Streaming Service","Favorite Genre"])

with tab1:
    left_column, right_column = st.columns(2) #Nella tabs1 divido in due colonne, ognuna dedicata ad uno dei due Streaming
    with left_column:                         #Service più utilizzati: Spotify e Youtube                   

        #creo un df solo per Spotify, contando quante persone (raggruppate per età) lo utilizzano come primary service
        #faccio la stessa cosa nella colonna di dx ma per Youtube. 

        spotify_df = data[data['Primary streaming service'] == 'Spotify'].groupby('Age').size().reset_index(name='SPOTIFY_USERS')
        st.subheader("Andamento in base all'età dell'utilizzo di Spotify")
        st.bar_chart(spotify_df, x='Age', y='SPOTIFY_USERS')


    with right_column:
        yt= data[data['Primary streaming service'] == 'YouTube Music'].groupby('Age').size().reset_index(name='YOUTUBE_USERS') 
        st.subheader("Andamento in base all' età dell' utilizzo di YouTube")
        st.bar_chart(yt, x='Age', y='YOUTUBE_USERS')




# ----- COLOR MAPPING PER USARE ST.MAP()
# ----- TABS2 Mostra le statistiche di tutti gli streaming service
# Di seguito verranno calcolate il numero di persone (raggruppate per età) che ascoltano musica per 
#ognuno degli streaming service (come fatto in precedenza per Youtube e Spotify)
with tab2:
    am=data[data['Primary streaming service'] == 'Apple Music'].groupby('Age').size().reset_index(name='APPLE_USERS')
    ns=data[data['Primary streaming service'] == 'I do not use a streaming service.'].groupby('Age').size().reset_index(name='NO_SERV_USERS')
    pa=data[data['Primary streaming service'] == 'Pandora'].groupby('Age').size().reset_index(name='PANDORA_USERS')
    ot=data[data['Primary streaming service'] == 'Other streaming service'].groupby('Age').size().reset_index(name='OTHER_USERS')

    #Merge di tutti i df costruiti per darlo in input al bar_chart di streamlit
    chart_df=pd.merge((pd.merge((pd.merge(spotify_df, yt, on = "Age", how = "outer")),
                      (pd.merge(am, ns, on = "Age", how = "outer")),on = "Age", how="outer")),
                       (pd.merge(pa,ot,on="Age",how="outer")),on = "Age", how = "outer" 
                    ).fillna(0)

    st.subheader("Streaming Services più utilizzati")
    st.bar_chart(chart_df, x="Age")

    #---- Color Mapping per la mappa che genero con streamlit
    color_mapping = {
        'Spotify': '#008000',        # verde
        'YouTube Music': '#FF0000',  # rosso
        'Apple Music': '#000000',    # nero
        'I do not use a streaming service.': '#808080',  # grigio
        'Other streaming service': '#FFFFE0', #giallo
        'Pandora': '#FFC0CB'         # rosa
    }


    colored_df=data.copy()  #Non modifico il dataframe originale

    #Aggiungo la colonna Color al dataframe colored_df
    colored_df['Color'] = colored_df['Primary streaming service'].map(color_mapping)
    colored_df.dropna(inplace=True)


    # Crea lo slider per l'età
    age = st.slider("Age", 0, 99,(25 , 75)) #Attenzione!!! Age è una tupla

    # Filtra il dataset in base all'età selezionata
    filtered_df = colored_df[   
                                (colored_df["Age"] >= age[0]) &
                                (colored_df["Age"] <= age[1])].reset_index()

    o= st.toggle("Visualize Filtered Data")
    if o:
        st.dataframe(filtered_df)

    # Mappa interattiva
    #Problema ---><---->----<>------------------------------------------------------------
    #https://github.com/streamlit/streamlit/issues/8077
    st.map(filtered_df, latitude='lat', longitude='lon',color='Color')
    ##st.map(filtered_df,latitude='lat',longitude='lon')

    with st.expander("Legend  :world_map:"):
        st.write("Spotify :large_green_circle:")      
        st.write("YouTube Music :red_circle:")
        st.write ("Apple Music :black_circle: " )   
        st.write("Pandora :large_purple_circle:")
        st.write("I do not use a streaming service :white_circle:")
        st.write("Other streaming service :large_yellow_circle:")

# ---- TABS3 --> In questa tabs 3 si può utilizzare la slidebar
# Il grafico visualizzato cambia dinamicamente in base alle scelte fatte dall utente.
with tab3:
    st.subheader("Qui puoi utilizzare la slidebar per settare i parametri che desideri :smile:")
    st.subheader("Il grafico si aggiornerà in automatico! :notes:")
    with st.sidebar:
        add_service = st.radio("Seleziona una piattaforma di streaming:",
                               ("Spotify","YouTube Music","Apple Music","Pandora","Other streaming service","I do not use a streaming service."))
        add_genre = st.selectbox("Seleziona un genere musicale",options=all_genre)
        select_age = st.slider("Age", 0, 99,(0 , 99))
#Costruzione del df da dare come input a bar_chart --> conteggio delle statistiche per ognuno degli
# Streaming Service, in base al genere preferito e più ascoltato.


    filtered_df= data[(data['Primary streaming service'] == add_service) &
                      (data['Fav genre'] == add_genre) &
                      (data['Age'] >= select_age[0] )  &
                      (data['Age'] <= select_age[1] ) 
                      ].groupby("Age").size().reset_index(name='Total')
    st.bar_chart(filtered_df,x="Age",y='Total')



