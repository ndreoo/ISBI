Progetto PowerBI

Il dataset utilizzato è 'MusicNY' documentato nel progetto 'venv' .

Il progetto si articola in 4 Sheet:
1) Overview : in questo sheet, è presente un filtro dei dati
	che consente all'utente di selezionare uno tra 
	gli streaming service. In automatico si aggiornerà il grafico
	a torta presente sulla destra. In particolare per un dato 
	servizio di streaming selezionato, verranno mostrate la percentuale
	di persone per ogni gruppo d'età.
2) Fav genre: in alto a sinistra è presente un istogramma a colonne in pila.
	Per ogni età, viene calcolato il numero di persone che ascolta un
	determinato genere musicale (tra quelli presenti nella legenda).
	In alto a destra un semplice grafico a torta che mostra le 
	percentuali di utilizzo di ogni streaming service.
	In basso a sinistra un grafico a barre in pila che mostra i tempi
	di utilizzo (Media di ore al giorno).
	In basso a destra si trova un misuratore che conta il numero di 
	persone che hanno scelto come genere favorito il rock.
3) General : in questo sheet è presente un istogramma a colonne raggruppate
	che calcola il numero di persone di una determinata età che 
	ascoltano il genere musicale presente sull'ascissa x.
	I dati sono appunto raggruppati per Fav Genre.
4) Anxiety: Questo sheet è uno studio riguardo le statistiche dell'ansia.
	Il grafico a dispersione evidenzia che il genere 'Video Game Music' 
	è ascoltato da persone con età intorno ai 20 anni, in corrispondenza
	delle quali è associato un valore medio di ansia molto elevato.
	Viene evidenziata dunque questa possibile correlazione tra
	il genere ed il valore dell'ansia.
	In basso è presente una mappa che evidenzia la collocazione geografica 
	delle persone in base ai livelli d'ansia. In particolare la dimensione
	delle bolle indica la media dell'ansia, mentre il colore indica la 
	frequenza di ascolto della Video Game music.