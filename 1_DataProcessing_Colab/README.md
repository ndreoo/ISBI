Documentazione dataset al link:
"https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results"

Il dataset è composto da 33 features e raccoglie dati rilevanti
riguardo i generi e le preferenze musicali dei partecipanti al sondaggio.

In particolare questo dataset può essere utile nel caso in cui si voglia 
prevedere il genere musicale preferito di una determinata classe (in base
a fattori come l'età, ad esempio) e fornisce anche delle feature direttamente
collegate agli effetti della musica nella Mental Health.
In particolare ogni utente ha inserito un valore (da 0 a 10) per ognuna delle
seguenti patologie (di cui crede o no di essere affetto): Depressione, Ansia,
Insonnia e OCD (Disturbo ossessivo compulsivo).
Dunque può essere interessante addestrare ad esempio una rete neurale per
predire qual è la classe (target group) più affine a questi disagi in 
base alle preferenze musicali.

- BIAS:
  Il dataset si presenta squilibrato: la maggioranza delle persone
  che hanno partecipato inserendo i propri dati è compresa nella fascia
  d'età tra i 15 ed i 25 anni.
  La piattaforma di streaming più utilizzata è Spotify.
  Inoltre bisogna notare che i valori nelle feature come
  Depression, Anxiety, OCD non sono stati inseriti e documentati da esperti
  settoriali (ad esempio psicologi) ma dall'utente stesso, che potrebbe
  confondere alcuni stati d'animo, in quanto non ne possiede la completa conoscenza.
  Un altro problema è che i record sono pochi se rapportati alla varianza dei risultati.
  Per tutti i motivi qui citati, ho scelto di effettuare un oversampling del dataset
  (è tutto commentato e spiegato nel codice sorgente).
