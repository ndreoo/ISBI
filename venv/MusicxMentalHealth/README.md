Dashboard MusicxMentalHealth.

Dataset originale documentato ampiamente al link:
"https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results?rvi=1"

ATTENZIONE !!!
Lo script genDS.py serve a generare il dataset utilizzato (modificato) per costruire la dashboard! Nel dataset originale non erano presenti informazioni riguardo la collocazione
geografica dei partecipanti al sondaggio. Per questo motivo ho creato questo script
affinchè generasse il dataset MusicNY.csv in modo da aggiungervi tre colonne: City (che
ha sempre il valore New York), lat (latitudine) e lon (longitudine).
I dati sulla latitudine e longitudine sono stati prelevati dal dataset "uber-raw-data-sep14.csv", presente nella directory 'dataset' e visto a lezione in una dashboard di esempio.

La dashboard MusicxMentalHealth si articola in 3 pagine (Streamlit pages):
1) Home.py --> è la home, sono presenti solo collegamenti alle altre due pagine
2) 1_Streaming_Services.py -->  sono presenti dati e statistiche rilevanti per gli streaming 
    services utilizzati dagli utenti del sondaggio.
    Il codice è ampiamento commentato.
3) 2_Mental_Health.py --> sono presenti dati e statistiche rilevanti per l'apporto della 
    musica nell'ambito Mental Health.
    Il codice è ampiamente commentato.