Progetto Bonita

Il progetto si compone di due pool:
1) Pool: In questo processo ci sono due attori:
	-Sensor : Si riferisce ad una parte sensoristica, ad esempio telecamere.
	I sensori osservano il traffico in ognuna delle tratte di 
	competenza della tangenziale di Napoli. Laddove trovano un aumento del traffico
	segnalano tramite una notifica ad un Employee
	-Employee: In base alla segnalazione automatica ricevuta dal sistema di sensori,
	decide se aprire o no le sbarre della stazione in questione.
	Il sistema aziona automaticamente le telecamere, che avranno il compito di 
	salvare in un db esterno (non di nostra competenza) i numeri di targa
	delle auto che superano il casello (poichè sono state alzate le sbarre,
	gli utenti non pagheranno il pedaggio). In tal modo il costo potrà 
	essere attribuito al proprietario dell'auto in un secondo momento (non di nostra competenza).
	Nel caso in cui venga anche segnalata la causa del traffico, ed essa coincide con un
	incidente, verrà inviato un messaggio alla Operative Pool, con una richiesta di intervento.
2) Operative Pool: La Operative Pool riceve il messaggio con la richiesta di intervento e,
	se disponibile, lo accetta. L'intento è quello di trovare il prima possibile una volante di 
	SOS che si diriga sul posto.

E' inoltre presente un connettore ad un database Mysql esterno, che tiene traccia dello stato
delle varie stazioni. In particolare ogni volta che vengono alzate le sbarre e 
azionate le telecamere in una specifica stazione, verrà effettuato l update 
del rispettivo record in tabella.
Tutto questo viene effettuato in maniera automatica dal sistema con il task 'Start Reg'.
La connessione al db MySQL avviene tramite XAMPP e PhpMyAdmin, quindi se si vuole eseguire il 
progetto bisogna effettuare il download di questi due servizi.