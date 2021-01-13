# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'viaggiAutostradali'

##########################################################
# Inizio della parte da editare
##########################################################

# sostituisci i *** con le informazioni richieste
studenteNome = '***'  # sostituisci gli *** con il tuo nome
studenteCognome = '***'  # sostituisci gli *** con il tuo cognome
studenteMatricola = '***'  # sostituisci gli *** con la tua matricola
#
# DESCRIZIONE DEL FILE CON I DATI
#
# Nel file .zip trovate i seguenti file:
#
# - autostradaA1.tsv con i dati relativi ai caselli autostradali.
#   Ciascuna riga contiene le seguenti informazioni:
#   KmProgressivo NomeCasello CodiceCasello
#       KmProgressivo - la distanza in Km del casello dall'inizio della
#           tratta autostradale
#       NomeCasello - è la stringa contente il nome del casello
#       CodiceCasello - è la stringa che identifica il casello
#   In una stringa python, il tabulatore (chiamato anche tab) e' rappresentato da '\t'
#
# - costoKm.txt con i dati relativi al costo chilometrico da applicare
#   al viaggio suddiviso per categoria del veicolo (A,B,3,4,5) e per tipologia
#   di strada (pianura, montagna). I dati sono in formato tabulare (tab separated values).
#
# - viaggi.csv con i dati, in ordine cronologico, relativi alle rilevazioni
#   dei veicoli al passaggio ai caselli di entrata o di uscita.
#   Ciascuna riga contiene le seguenti informazioni:
#   time targa categoria casello
#       time - è il tempo [secondi], a partire dall'accensione del sistema,
#           a cui è avvenuta la rilevazione
#       targa - è la targa che identifica in maniera univoca il veicolo
#           associato alla rilevazione
#       categoria - è la classe associata al veicolo rilevato (A,B,3,4,5)
#       casello - è la stringa identificativa del casello a cui è avvenuta la
#           rilevazione
#   E' possibile associare un viaggio ad un veicolo tramite l'identificazione
#   del casello di entrata e quello di uscita

# DESCRIZIONE DEL LAVORO DA SVOLGERE
#
# Implementate le seguenti funzioni, per favore non usate input() o raw_input()
# nel codice che scriverete.
#
# - creaDizCaselli(fileName1). La funzione accetta come unico parametro in ingresso
#   la stringa contenete il nome del file con i dati relativi ai caselli autostradali.
#   Nota bene: il nome del file deve essere passato dal programma chiamante come parametro.
#   La funzione restituisce un dizionario formato da coppie chiave valore, come nell'esempio seguente:
#   {'708': ('Frosinone', 624.2), '709': ('Ceprano', 642.0),...}.
#   La chiave e' una stringa con il codice del casello (ricavato sulla base del contenuto del file),
#   il valore associato alla chiave e' una tupla contenente rispettivamente la stringa con il nome del casello ed
#   il valore numerico del chilometro a cui è situato il casello.
#   Il dizionario restituito dalla funzione dovra' contenere una coppia chiave valore per ognuno dei caselli i cui
#   dati sono riportati nel file in ingresso. Ricordatevi di chiudere il file prima di restituire il risultato.
def creaDizCaselli(filename):
    pass


# - caricaTariffe(filename).La funzione accetta come unico parametro in ingresso
#   la stringa contenete il nome del file con i dati relativi alle tariffe chilometriche.
#   Nota bene: il nome del file deve essere passato dal programma chiamante come parametro.
#   La funzione restituisce un dizionario formato da coppie chiave valore contente la tariffazione
#   per il solo percorso in pianura, come nell'esempio seguente:
#   {'A': 0.07135, 'B': 0.07302, ...}.
#   La chiave e' una stringa con il codice della categoria (ricavato sulla base del contenuto del file),
#   il valore associato alla chiave e' il valore numerico del costo al Km in euro associato alla classe.
#   Il dizionario restituito dalla funzione dovra' contenere una coppia chiave valore per ogni tariffa
#   di pianura i cui dati sono riportati nel file in ingresso.
#   Ricordatevi di chiudere il file prima di restituire il risultato.
def caricaTariffe(filename):
    pass


# - calcolaImporti(fileCaselli, fileViaggi, fileTariffe).
#   La funzione accetta come parametri in ingresso le stringhe contenenti il
#   nome dei tre file con i dati relativi ai caselli, ai Viaggi ed alle tariffe chilometriche.
#   Nota bene: i nomi dei file devono essere passato dal programma chiamante come parametro.
#   Tenete conto che nel file viaggi, ogni macchina presente compie un unico viaggio.
#   La funzione restituisce un dizionario formato da coppie chiave valore contente l'importo
#   associato a ciascun viaggio, come nell'esempio seguente:
#   {'IP474GN': ['24', '37', 45.821594000000005], 'RS226IC': ['95', '3', 0.9469203699999997], ...}.
#   La chiave e' una stringa con la targa associata al veicolo (ricavato sulla base del contenuto del file),
#   il valore associato alla chiave e' una lista composta nell'ordine dal codice del casello in entrata,
#   codice del casello in uscita, valore numerico dell'importo espresso in euro corrispondente al viaggio.
#   Il dizionario restituito dalla funzione dovra' contenere una coppia chiave valore per ogni viaggio
#   i cui dati sono riportati nel file in ingresso fileViaggi.
#   L'importo relativo al viaggio deve essere calcolato come il valore assoluto della differenza
#   tra il kilometraggio del casello in uscita e quello in ingresso.
#   Ricordatevi di chiudere il file prima di restituire il risultato.
def calcolaImporti(fileCaselli, fileViaggi, fileTariffe):
    pass


##########################################################
# Fine della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))
print('Ciao (%s, %s, %s)' % (studenteNome, studenteCognome, studenteMatricola))
print('Eseguo la funzione calcolaImporti')
fn1 = 'autostradaA1.tsv'
fn2 = 'viaggi.csv'
fn3 = 'costoKm.txt'
diz1 = creaDizCaselli(fn1)
print('Risultato prima funzione: ')
print(diz1)
diz2 = caricaTariffe(fn3)
print('Risultato seconda funzione: ')
print(diz2)
diz3 = calcolaImporti(fn1, fn2, fn3)
print('Risultato terza funzione: ')
print(diz3)
