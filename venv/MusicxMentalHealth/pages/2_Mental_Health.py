import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Music for Mental Health Dashboard",
    page_icon=" :guitar: :musical_note:",
)

st.title("**Welcome in mental health page!** ")

#'C:/Users/andre/venv/MusicxMentalHealth/dataset/MusicNY.csv'
dataset_string=('C:/Users/andre/venv/MusicxMentalHealth/dataset/MusicNY.csv')
@st.cache_data
# Carica i dati dal file CSV
def loaddata(datastring):
    df=pd.read_csv(datastring)
    return df


data=loaddata(dataset_string)
total_row= data.shape[0]
#st.write(data)

## ---- Creazione di due colonne

deprecol, anxcol = st.columns(2)
#deprecol è la colonna dedicata alle statistiche sulla depressione 
#anxcol è la colonna dedicata allae statistiche sull'ansia
#cast ad intero tutte le colonne analizzate in questa parte
data['Depression'].astype(int) #--> Inizialmente erano dei float, ma trasformandoli in int risulta più semplice per l'utente scorrere lo slider
data['Anxiety'].astype(int)
music_effect=data['Music effects'].unique()
with deprecol:
    #In questa parte, l utente seleziona il valore specifico X di Depression (da 0 a 10) e l effetto Y della Musica (Improve, Worsen o No eff)
    #La statistica calcolata è la percentuale di utenti che hanno indicato X come valore di Depr e Y come effetto 
    sel=st.selectbox("Scegli un'opzione da visualizzare",('Improve','Worsen','No effect'))
    st.write('Hai selezionato:', sel)
    depress_value= st.slider('Select Depression Value',0,10)
   
   #Qui viene calcolata la percentuale di cui sopra
    filter=(data['Depression'] == depress_value) & (data['Music effects']==sel)
    how_many_dep_sel=data.where(filter).groupby(['Depression','Music effects']).size().reset_index(name='total')
    tot=how_many_dep_sel['total'].astype(int)
    percentage = (tot[0]/ total_row)*100
    val = '%.2f' % percentage
    st.write(val,"%")


    dep_df = pd.DataFrame()  # Creazione del dataframe vuoto

    #Questo doppio ciclo for --> Costruisce un dataframe nel quale
    #per ogni valore di Depression (tra 0 e 10) e per ogni valore di Music Effects (Improve, No eff, Worsen)
    # calcola il num di persone. Ad esempio --> Per valore di depression =5 e per effetto Improve, abbiamo un 
    #determinato numero totale di persone.. etc etc etc
    for item in music_effect:
        for i in range(0,11):
            f=data[(data['Depression'] == i) & (data['Music effects']==item)].groupby(['Depression','Music effects']).size().reset_index(name='total')
            dep_df=pd.concat([dep_df,f], axis=0)
            
            
    final_df = dep_df.copy()
    final_df['total'] = (final_df['total'] / total_row) * 100   #il valore contato viene mostrato in percentuale

 
    
    selected_effect = st.multiselect ("Scegli i Music Effects da plottare",
                                      ['Improve','No effect','Worsen'])
    filtered_df=final_df[
            (final_df['Music effects'].isin(selected_effect))
    ]
   
    st.line_chart(filtered_df.reset_index(),x="Depression", y="total",color='Music effects')


## -- anxcol è la colonna per le statistiche sull'ansia.
# Il codice è identico a quello riportato sopra per la depression, basta appunto sostituire il nome della colonna
# 'Depresison' con 'Anxiety'. Per quanto riguarda il modo di generare i grafici e calcolare le statistiche
# è identico a quanto mostrato sopra. Per questo motivo non commenterò il codice da qui in poi.
#Lo stesso processo sarà effettuato per ocdcol (colonna dedicata al disturbo ocd) e insomniacol (dedicata all insonnia)
#che si trovano sempre sotto.
with anxcol:
    
    sel=st.selectbox("Scegli un'opzione da visualizzare",('Improve','Worsen','No effect'),key=2)
    st.write('Hai selezionato:', sel)
    anxiety_value= st.slider('Select Anxiety Value',0,10)
    filter=(data['Anxiety'] == anxiety_value) & (data['Music effects']==sel)
    how_many_anx_sel=data.where(filter).groupby(['Anxiety','Music effects']).size().reset_index(name='total')
    tot=how_many_anx_sel['total'].astype(int)
    percentage = (tot[0]/ total_row)*100
    val = '%.2f' % percentage
    st.write(val,"%")

    #prova a fare line_chart con la percentuale che esce meglio.
    #prova a farlo col multiselect

    anx_df = pd.DataFrame()  # Creazione del dataframe vuoto

    for item in music_effect:
        for i in range(0,11):
            f=data[(data['Anxiety'] == i) & (data['Music effects']==item)].groupby(['Anxiety','Music effects']).size().reset_index(name='total')
            anx_df=pd.concat([anx_df,f], axis=0)
            
            
    final_df = anx_df.copy()
    final_df['total'] = (final_df['total'] / total_row) * 100

 
    
    selected_effect = st.multiselect ("Scegli i Music Effects da plottare",
                                      ['Improve','No effect','Worsen'],key=3)
    filtered_df=final_df[
            (final_df['Music effects'].isin(selected_effect))
    ]
   
    st.line_chart(filtered_df.reset_index(),x="Anxiety", y="total",color='Music effects')

ocdcol, insomniacol= st.columns(2)

with ocdcol:
    
    sel=st.selectbox("Scegli un'opzione da visualizzare",('Improve','Worsen','No effect'),key=4)
    st.write('Hai selezionato:', sel)
    OCD_value= st.slider('Select OCD Value',0,10)
    filter=(data['OCD'] == OCD_value) & (data['Music effects']==sel)
    how_many_ocd_sel=data.where(filter).groupby(['OCD','Music effects']).size().reset_index(name='total')
    tot=how_many_ocd_sel['total'].astype(int)
    percentage = (tot[0]/ total_row)*100
    val = '%.2f' % percentage
    st.write(val,"%")

    #prova a fare line_chart con la percentuale che esce meglio.
    #prova a farlo col multiselect

    ocd_df = pd.DataFrame()  # Creazione del dataframe vuoto

    for item in music_effect:
        for i in range(0,11):
            f=data[(data['OCD'] == i) & (data['Music effects']==item)].groupby(['OCD','Music effects']).size().reset_index(name='total')
            ocd_df=pd.concat([ocd_df,f], axis=0)
            
            
    final_df = ocd_df.copy()
    final_df['total'] = (final_df['total'] / total_row) * 100

 
    
    selected_effect = st.multiselect ("Scegli i Music Effects da plottare",
                                      ['Improve','No effect','Worsen'],key=5)
    filtered_df=final_df[
            (final_df['Music effects'].isin(selected_effect))
    ]
   
    st.line_chart(filtered_df.reset_index(),x="OCD", y="total",color='Music effects')

with insomniacol:
    sel=st.selectbox("Scegli un'opzione da visualizzare",('Improve','Worsen','No effect'),key=6)
    st.write('Hai selezionato:', sel)
    ins_value= st.slider('Select Insomnia Value',0,10)
    filter=(data['OCD'] == ins_value) & (data['Music effects']==sel)
    how_many_ins_sel=data.where(filter).groupby(['Insomnia','Music effects']).size().reset_index(name='total')
    tot=how_many_ins_sel['total'].astype(int)
    percentage = (tot[0]/ total_row)*100
    val = '%.2f' % percentage
    st.write(val,"%")


    ins_df = pd.DataFrame()  # Creazione del dataframe vuoto

    for item in music_effect:
        for i in range(0,11):
            f=data[(data['Insomnia'] == i) & (data['Music effects']==item)].groupby(['Insomnia','Music effects']).size().reset_index(name='total')
            ins_df=pd.concat([ins_df,f], axis=0)
            
            
    final_df = ins_df.copy()
    final_df['total'] = (final_df['total'] / total_row) * 100

 
    
    selected_effect = st.multiselect ("Scegli i Music Effects da plottare",
                                      ['Improve','No effect','Worsen'],key=7)
    filtered_df=final_df[
            (final_df['Music effects'].isin(selected_effect))
    ]
   
    st.line_chart(filtered_df.reset_index(),x="Insomnia", y="total",color='Music effects')