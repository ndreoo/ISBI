Climate in Delhi

In questa dashboard si vuole studiare l'andamento della temperatura media 
nella città di Delhi, tramite l'applicazione dell'analisi di serie storiche.
Il dataset è documentato al seguente link: "https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data"

In particolare dei due file .csv forniti, ho utilizzato solo DailyDelhiClimateTrain.csv (77 Kb).

Il codice tsa.py è commentato per spiegare passo passo i vari procedimenti.

Nel mio caso specifico, ho osservato dalla dashboard che il modello a crescita lineare
si presta meglio rispetto quello a crescita logistica.
Forse perchè il modello lineare può essere utile se i dati mostrano un aumento o una
diminuzione lineare nel tempo. Nel nostro caso è così, poichè effettivamente la 
temperatura media sta aumentando (non solo a Delhi) ma in tutto il mondo.
Tuttavia questo aumento non è esponenziale, ma molto contenuto nell'intervallo di tempo 
di acquisizione dei dati del dataset (dal 2013 al 2017).

