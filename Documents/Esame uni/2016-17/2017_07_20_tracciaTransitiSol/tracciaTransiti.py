# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'transiti'

alfabeto='abcdefghijklmnopqrstuvwxyz'
cifre='0123456789'
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
# Nel file .zip trovate il seguente file, oltre a questo script:
#
# - File 1) transiti.csv
#   In una citta' le automobili che entrano nel centro storico devono pagare
#   una tassa. Nel file transiti.csv sono contenuti gli ingressi effettuati
#   da alcune auto. Nel file, entra nel centro storico al massimo una volta
#   al giorno. 
#   Il file ha questa struttura:
#   targa_automobile,gg/mm/aa,hh:mm\r\n
#   dove gg/mm/aa,hh:mm indicano il giorno e l'ora dell'ingresso.
#   L'importo da pagare per l'ingresso dipende dalla classe inquinante del veicolo.
#   La targa del veicolo e' composta da alcune lettere alfabetiche, seguite da
#   alcuni numeri, seguiti infine da altre lettere alfabetiche, come negli esempi
#   seguenti: def6543ghai, faei72no (sia il numero di cifre numeriche sia il numero
#   di lettere alfabetiche non sono costanti). Nelle targhe sono utilizzate solo
#   lettere dell'alfabeto minuscole e cifre numeriche. La classe inquinante del
#   veicolo e' individuata utilizzando le cifre alfabetiche a destra delle cifre
#   numeriche (se la targa e' 'def6543ghai' la classe inquinante e' individuata dalle
#   ultime cifre alfabetiche a destra 'ghai'). Le cifre alfabetiche a destra di quelle
#   numeriche sono un numero variabile, ma sono sempre almeno 2.
#   Le classi inquinanti possibili sono 5 individuate dai numeri che vanno da 0 a 4.
#   La classe inquinante e' individuata utilizzando il seguente algoritmo. Premessa:
#   ogni lettera dell'alfabeto ha associato un valore numerico dato dalla posizione
#   della lettera all'interno della variabile alfabeto ('a' ha posizione 0, 'b'
#   ha posizione 1, etc. vedi la dichiarazione di "alfabeto" all'inizio di questo script).
#   Per calcolare la classe inquinante, si considerando solo le lettere alfabetiche
#   a destra delle cifre numeriche. Dalla seconda lettera alfabetica fino all'ultima,
#   si associa un numero ad ogni lettera cosi' calcolato: sia (pc) la posizione della
#   lettera corrente nell'alfabeto e (pp) la posizione della lettera precedente,
#   il valore numerico da associare alla lettera corrente
#   e' dato da pc+2**pp (** sta per elevato).  Si sommano tra loro i valori numerici 
#   ottenuti e si calcola il resto della divisione intera per 5.
#   Per esempio, data la sottostringa 'ghai' della targa, si eseguono questi calcoli:
#   classe_inquinante = (7+2**6  + 0+2**7 + 8+2**0) resto divisione intera per 5.
#   Se si moltiplica la classe inquinante per 1.50 euro si ottiene la tassa che
#   il veicolo deve pagare per ogni ingresso. Quindi i veicoli in classe 0 non pagano la tassa,
#   il veicolo in classe 1 paga 1.50 euro, il veicolo di classe 2 paga 3 euro, ...
#   Nei mesi di gennaio e febbraio (solo gennaio e febbraio) e' stato applicato il
#   provvedimento delle targhe alterne.
#   Nei giorni pari potevano circolare solo le auto con targa pari, nei giorni dispari potevano
#   circolare solo le auto con targa dispari. Una targa e' pari o dispari a seconda che
#   la cifra numerica piu' a destra della targa sia pari o dispari. Per esempio
#   def6543ghai e' una targa dispari e faei72no e' una targa pari. Se nei mesi del provvedimento
#   a targhe alterne un'auto e' entrata nel centro storico nel giorno sbagliato, al posto di
#   pagare la tassa d'ingresso deve pagare una tassa di 50 euro (in altre parole, una multa).
#   La prima riga del file contiene l'intestazione.
#   I \r\n rappresentano due caratteri di "a capo".
#   Provate ad aprire il file con un editor di testi. State attenti, se aprirete il file con Excel 
#   o con il notepad di windows, alcune informazioni potrebbero essere 
#   VISUALIZZATE in MANIERA DISTORTA rispetto al contenuto del file.
#
# DESCRIZIONE DEL LAVORO DA SVOLGERE
#
# Implementate le seguenti funzioni, il commento che precede ogni funzione vi
# spieghera' cosa fare in dettaglio.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
#
# - caricaAccessi(nomeFile). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati descritto in precedenza.
#   La funzione dovra' restituire una lista formata da tuple,
#   dove ogni tupla contiene i dati di una riga del file, come nell'esempio
#   seguente (l'esempio si estende su piu' righe):
#   [  (targa, giorno, mese, anno, ora, minuto, classe_inquinante),
#      (targa, giorno, mese, anno, ora, minuto, classe_inquinante),
#      ...
#   ]
#   Ad eccezione di targa, tutti gli altri valori restituiti devono essere valori interi
#   Se volete potete implementare delle funzioni aggiuntive. Potete
#   utilizzare lo spazio qua sotto

def caricaAccessi(nomeFile):
    pass # Questa istruzione puo' essere eliminata. Ricordatevi di chiudere il file prima di restituire il risultato

# - calcolaCostiAuto(dati). La funzione accetta come parametro
#   in ingresso la struttura dati restituita dalla funzione precedente.
#   La funzione deve calcolare e restituire il costo totale pagato per
#   le tasse dalle auto.
#   La funzione deve restituire un dizionario di coppie chiave valore, dove
#   la chiave e' rappresentata dalla targa dell'auto e il valore e' un float
#   contenente la somma totale che l'auto ha dovuto pagare considerando
#   gli accessi contenuti nel file.
#   Se volete potete implementare delle funzioni aggiuntive. Potete
#   utilizzare lo spazio qua sotto

def calcolaCostiAuto(dati):
    pass # Questa istruzione puo' essere eliminata.

# - calcolaPicchi(dati).  La funzione accetta come parametro
#   in ingresso la struttura dati restituita dalla funzione caricaAccessi.
#   La funzione deve restituire una lista di 24 valori numerici interi,
#   dove ogni valore rappresenta il numero di ingressi di auto svolti nell'ora corrispondete.
#   Per esempio [2, 6, 10, 25, ...] significa che tra le 00:00 e le 00:59 nei diversi giorni
#   ci sono stati 2 ingressi, tra le 1:00 e le 1:59 ci sono stati 6 ingresi, ...

def calcolaPicchi(dati):
    pass # Questa istruzione puo' essere eliminata.

##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione. 
##########################################################

print('Esercizio %s.' % (nomeEsercizio))
print('Ciao (%s, %s, %s)' % (studenteNome, studenteCognome, studenteMatricola))

print('1) Eseguo la funzione caricaAccessi')
fn = 'transiti.csv'
la = caricaAccessi(fn)
print('Risultato: ')
print(la)

print('2) Eseguo la funzione calcolaCostiAuto: ')
di=calcolaCostiAuto(la)
print('Risultato: ')
print(di)

print('3) Eseguo la funzione calcolaPicchi: ')
lp = calcolaPicchi(la)
print('Risultato: ')
print(lp)

