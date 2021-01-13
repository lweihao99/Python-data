# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'ritardi'

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
# Nel file .zip trovate i seguenti file, oltre a questo script:
#
# - aeroporti.csv
#   Il file contiene informazioni su alcuni aeroporti italiani.
#   Un esempio del contenuto del file e':
#
#   Codice;Citta;Latitudine;Longitudine;Nome\r\n
#   CRV;Crotone;'3.89972';'17.0802';Crotone Airport\r\n
#   ...\r\n
#
#   La prima riga contiene l'intestazione delle colonne. Ogni riga riporta le
#   informazioni seguenti.
#   * Codice e' una stringa da 3 caratteri che identifica univocamente l'aeroporto.
#   * Citta e' la citta' dove e' situato l'aeroporto.
#   * Nome e' il nome vero e proprio dell'aeroporto (es. "Leonardo da Vinci-Fiumicino" 
#     e' il nome di uno degli aeroporti di Roma).
#   * latitudine e longitudine sono le coordinate dell'aeroporto.
#   Provate ad aprire il file con un editor di testi (state attenti, se aprirete
#   il file con un foglio di calcolo, alcune informazioni potrebbero essere 
#   visualizzate in maniera distorta rispetto al contenuto del file).
#   Il \r\n rappresentano due caratteri di "a capo".
#   SUGGERIMENTO: NON aprite il file ne' con il notepad di windows ne' con excel.
#
#
# - voli.csv contiene i dati dei voli effettuati in una settimana
#   Un esempio del contenuto del file e':
#
#   Aerop. Partenza;Aerop. Arrivo;Giorno settimana;Orario partenza ufficiale;
#                 Orario partenza effettivo;Orario arrivo ufficiale;Orario arrivo effettivo \r\n
#   BZO;NAP;6;8:40;8:40;9:30;9:44\r\n
#   FCO;REG;2;9:10;9:10;10:20;10:50\r\n
#
#   La prima riga contiene l'intestazione delle colonne. Ogni riga riporta le
#   informazioni seguenti.
#   * Aerop. Partenza: l'aeroporto da cui parte il volo
#   * Aerop. Arrivo: l'aeroporto in cui termina il volo
#   * Giorno settimana: il giorno della settimana in cui e' avvenuto il volo,
#     1 e' lunedi, 7 e' domenica
#   * Orario partenza ufficiale: Orario in cui il volo dovrebbe partire
#   * Orario partenza effettivo: Orario in cui il volo e' effettivamente partito
#   * Orario arrivo ufficiale: Orario in cui il volo dovrebbe terminare
#   * Orario arrivo effettivo: Orario in cui il volo e' effettivamente terminato
#
#
#
# DESCRIZIONE DEL LAVORO DA SVOLGERE
#
# Implementate le seguenti funzioni, il commento che precede ogni funzione vi
# spieghera' cosa fare in dettaglio.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
#
# - leggiNomiAeroporti(faero). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati sugli aeroporti italiani.
#   Nota bene: il nome del file da aprire e' passato alla funzione
#   come parametro. La funzione restituisce un dizionario formato da coppie
#   chiave valore, come nell'esempio seguente: {'MXP':'Malpensa International Airport', 
#   'BGY':'Il Caravaggio International Airport',... }. La chiave e' il
#   codice dell'aeroporto, il valore e' il nome vero e proprio dell'aeroporto.
#   
#   Il dizionario restituito dalla funzione dovra' contenere una coppia chiave valore
#   per ognuno degli aeroporti presenti nel file passato come parametro. Codici
#   e nomi devono essere letti dal file. Ricordatevi
#   di chiudere il file prima di restituire il risultato.
#   Scrivete l'implementazione della funzione qua sotto.

def leggiNomiAeroporti(faero):
    pass # Questa istruzione puo' essere eliminata. Ricordatevi di chiudere il file prima di restituire il risultato





# - leggiVoli(fvoli). La funzione accetta come parametro
#   in ingresso il nome del file con le informazioni
#   sui voli. La funzione dovra' restituire una lista formata da tante
#   tuple quante sono le righe del file che contengono informazioni sui voli.
#   Non deve essere inserita la riga contenente l'intestazione del file.
#   Ogni tupla dovrà contenere le seguenti informazioni: codice aeroporto di
#   partenza, codice aeroporto di arrivo, e i 4 orari, rispettivamente:
#   "partenza ufficiale", "partenza effettiva", "arrivo ufficiale", "arrivo effettivo".
#   Ogni orario deve essere rappresentato da un numero intero che rappresenta
#   i minuti trascorsi dall'inizio del giorno (es. le 15:50 corrispondono a
#   15*60+50=950).
#   Per esempio le righe
#   ...
#   BZO;NAP;6;8:40;8:40;9:30;9:44\r\n
#   FCO;REG;2;9:10;9:10;10:20;10:50\r\n
#   ...
#   dovrebbero essere convertite nella seguente struttura dati
#   [  ..., ('BZO', 'NAP', 520, 520, 570, 584), ('FCO', 'REG', 550, 550, 620, 650), ... ]
#   Scrivete l'implementazione della funzione qua sotto.
#   Se vi facesse comodo, qua sotto potete anche implementare funzioni aggiuntive.

def leggiVoli(fvoli):
    pass # Questa istruzione puo' essere eliminata. Ricordatevi di chiudere il file prima di restituire il risultato




# - calcolaRitardi(fvoli). La funzione accetta come parametro
#   in ingresso rispettivamente il dizionario restituito dalla funzione
#   leggiNomiAeroporti e la lista restituita dalla funzione leggiVoli.
#   La funzione deve calcolare i ritardi accumulati su una tratta.
#   Una tratta e' formata dalla coppia aeroporto di partenza aeroporto 
#   di arrivo. Andata e ritorno sono due tratte diverse, es., un volo
#   da 'MXP' a 'FCO' percorre una tratta diversa da un aereo che vola
#   da 'FCO' a ' MXP'. Il ritardo e' calcolato solo sull'aeroporto di
#   arrivo, se un aereo parte in ritardo ma arriva in orario, in quel
#   caso il ritardo e' pari a 0. Se un aereo arriva in anticipo, il ritardo
#   dovrà essere pari a 0. La funzione dovrà individuare la
#   tratta che ha accumulato i ritardi maggiori e restituire una lista
#   formata da: codice aeroporto di partenza, codice aeroporto di arrivo,
#   minuti totali di ritardo, nome aeroporto di partenza, nome aeroporto
#   di arrivo. Se ci fossero piu' tratte con lo stesso numero massimo di
#   minuti di ritardo, riportate i dati di una sola tratta individuandola
#   con un criterio a vostra scelta.
#   Un esempio di possibile risultato potrebbe essere (i dati seguenti sono
#   casuali, NON SONO le soluzioni corrette):  ['MXP', 'FCO', 1210,
#   'Malpensa International Airport', 'Leonardo da Vinci-Fiumicino Airport']
#   Suggerimento: potete dare un nome alle tratte concatenando i codici
#   degli aeroporti coinvolti.

def calcolaRitardi(aerop, dativoli):
    pass # Questa istruzione puo' essere eliminata.



# - calcolaNumDestinazioni(dativoli). La funzione accetta come parametro
#   in ingresso la lista restituita dalla funzione leggiVoli.
#   La funzione deve restituire un dizionario di coppie chiave valore
#   in cui la chiave e' il codice di un aeroporto e il valore e' il
#   numero di destinazioni diverse, cioe'  il numero di aeroporti diversi
#   raggiungibili con i voli in partenza dallo specifico aeroporto.
#   L'insieme delle chiavi e' formato dagli aeroporti in cui ci sono
#   voli in partenza nella struttura dati ricevuta come parametro
#   in ingresso. 
#   Per esempio, se nella struttura dati ricevuta in ingresso,
#   tutti i voli in partenza da 'MXP' atterrano in 3 diversi aeroporti,
#   allora nel dizionario restituito ci sara' {..., 'MXP':3, ...}. Nota
#   bene, i valori dell'esempio sono stati scritti a caso.
#   Se un aeroporto non appare mai come aeroporto di partenza, non deve
#   rientrare nel dizionario restituito.

def calcolaNumDestinazioni(dativoli):
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
print('1) Eseguo la funzione leggiNomiAeroporti')
fn1 = 'aeroporti.csv'
dbaerop = leggiNomiAeroporti(fn1)
print('Risultato: ')
print(dbaerop)

print('2) Eseguo la funzione leggiVoli: ')
fn2 = 'voli.csv'
voli=leggiVoli(fn2)
print('Risultato: ')
print(voli)

print('3) Eseguo la funzione calcolaRitardi: ')
res = calcolaRitardi(dbaerop, voli)
print('Risultato: ')
print(res)

print('4) Eseguo la funzione calcolaNumDestinazioni: ')
con=calcolaNumDestinazioni(voli)
print('Risultato: ')
print(con)
