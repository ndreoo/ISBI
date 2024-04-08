import random
import streamlit as st
import pandas as pd
import numpy as np

#dataset_string=('C:/Users/andre/venv/dataset/oversmp_ds.csv')
dataset_string=('./dataset/provaNYMusic.csv')


@st.cache_data
# Carica i dati dal file CSV, utilizzando il meccanismo della cache per velocizzare gli accessi e le operazioni
def loaddata(datastring):
    df=pd.read_csv(datastring)
    return df

st.title("**Music for Mental Health**")

#acquisizione e pulizia dei dati 
data=loaddata(dataset_string)
data.dropna(inplace=True)
st.write(data)
st.write("nr. row ", data.shape[0]) #1680 rows

data['Date'] = pd.to_datetime(data['Timestamp']).dt.date
data = data.drop('Timestamp', axis=1)
st.dataframe(data)
st.write("nr. row ", data.shape[0])
#-------------------------------------------------COSTRUZIONE CON CITY, LAT E LON ---------------------------------------------

#Ho utilizzato il dataset uber-raw-data-sep14.csv mostrato a lezione per prendere coordinate casuali ed 
#associarle ad ognuna delle persone presenti nel dataset MusicxMentalHealth
url_ll_ny = './dataset/uber-raw-data-sep14.csv'

#Aggiungo la colonna city (==New York) al dataset
for i in range(len(data)):
    data.at[i, 'city'] = 'New York'

ny_ll = loaddata(url_ll_ny)

ny_ll_first10 = ny_ll.sort_values(by=['Lat','Lon'], ascending=True).rename(columns={'Lat':'lat','Lon':'lon'}).head(1887)
#head(1887) --> facendo in questo modo riesco ad ottenere le stesse dimensioni tra i dataframe che desidero unire
ny_ll_first10df = ny_ll_first10[['lat', 'lon']].drop_duplicates() #.to_dict(orient='records')
unique_coords=ny_ll_first10df.to_dict(orient='records')
#unique_coords ha 1088 record proprio come data
st.write(ny_ll_first10df)
st.write(ny_ll_first10df.shape[0])

#st.write(merged_data)
random_indices = random.sample(range(len(ny_ll_first10df)), len(data))

# Aggiungi le colonne del dizionario al dataset allegato in modo casuale
for i in range(len(data)):
    idx = random_indices[i]
    row = unique_coords[idx]
    data.at[i, 'lat'] = row['lat']
    data.at[i, 'lon'] = row['lon']
st.dataframe(data)
st.write("nr. row ", data.shape[0])

data.dropna(inplace=True)
data.to_csv('./dataset/MusicNY.csv',index=False)