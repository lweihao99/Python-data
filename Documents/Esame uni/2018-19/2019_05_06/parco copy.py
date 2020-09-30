# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'parcoGiochi'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituito da una delle funzioni seguenti,
# La vera struttura dati caricata dal file sara' più lunga,
# i primi elementi delle due strutture dati non è detto che coincidano.

datiLetti = [('abbonamento', 25, 17.0), ('entrata', 23, '14/1/2018'),
             ('entrata', 23, '12/1/2018'), ('entrata', 7, '15/1/2018'), ('entrata', 7, '10/1/2018'), ('entrata', 7, '22/1/2018'), ('entrata', 15, '23/1/2018'), ('entrata', 3, '3/1/2018'), ('entrata', 17, '24/1/2018'), ('entrata', 27, '19/1/2018'), ('entrata', 27, '23/1/2018'), ('entrata', 27, '29/1/2018'), ('entrata', 9, '7/1/2018'), ('entrata', 43, '30/1/2018'), ('entrata', 43, '29/1/2018'), ('entrata', 43, '9/1/2018'), ('entrata', 43, '14/1/2018'), ('entrata', 43, '19/1/2018'), ('entrata', 25, '20/1/2018'), ('entrata', 25, '21/1/2018'), ('entrata', 25, '27/1/2018'), ('entrata', 39, '22/1/2018'), ('entrata', 39, '2/1/2018'), ('entrata', 39, '29/1/2018'), ('entrata', 39, '5/1/2018'), ('entrata', 39, '1/1/2018'), ('abbonamento', 15, 13.0), ('entrata', 37, '4/2/2018'), ('entrata', 37, '10/2/2018'), ('entrata', 37, '14/2/2018'), ('entrata', 37, '24/2/2018'), ('entrata', 2, '20/2/2018'), ('entrata', 2, '2/2/2018'), ('entrata', 2, '27/2/2018'), ('entrata', 2, '10/2/2018'), ('entrata', 2, '12/2/2018'), ('entrata', 8, '24/2/2018'), ('entrata', 8, '15/2/2018'), ('entrata', 47, '15/2/2018'), ('entrata', 47, '17/2/2018'), ('entrata', 47, '5/2/2018'), ('entrata', 16, '2/2/2018'), ('entrata', 17, '19/2/2018'), ('entrata', 17, '20/2/2018'), ('entrata', 17, '9/2/2018'), ('entrata', 17, '18/2/2018'), ('entrata', 41, '1/2/2018'), ('entrata', 41, '6/2/2018'), ('entrata', 41, '9/2/2018'), ('entrata', 1, '12/2/2018'), ('entrata', 1, '1/2/2018'), ('entrata', 1, '22/2/2018'), ('entrata', 15, '10/2/2018'), ('entrata', 15, '20/2/2018'), ('entrata', 31, '1/2/2018'), ('entrata', 31, '20/2/2018'), ('entrata', 31, '7/2/2018'), ('entrata', 31, '2/2/2018'), ('abbonamento', 20, 14.0)]

##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritto qua di seguito
#
# - File 1) 'accessiParco.csv'
#   Il file memorizza i dati raccolti sugli accessi effettuati dai visitatori
#   di un parco divertimenti e sulla sottoscrizione di abbonamnti
#   dall'1/1/2018 al 31/12/2018.
#   Nel file sono presenti DUE DIVERSE TIPOLOGIE di righe.
#   Il secondo valore presente in ogni riga (tipo_riga)
#   permette di differenziare il tipo della riga
#   e puo' assumere due valori: abb o sing
#   (rispettivamente come abbonamento o ingresso singolo)
#   Nell'esempio qua sotto non considerate il simbolo di # e
#   gli spazi. Gli a capo (\r\n) sono stati omessi per semplicità.

#
#   codUtente;abb;prezzoAbbonamento
#   codUtente;sing;dataAccesso1(g/m/aaaa)...data_accessoN
#   25;abb;177
#   23;sing;14/1/2018;12/1/2018
#   90;abb;310
#   7;sing;15/1/2018;10/1/2018;22/1/2018
#   15;sing;23/1/2018
#   3;sing;3/1/2018
#   17;sing;24/1/2018
#   27;sing;19/1/2018;23/1/2018;29/1/2018
#   9;sing;7/1/2018
#   ...
#   28;sing;5/12/2018;21/12/2018;27/12/2018
#   44;sing;10/12/2018

#   ...
#
#   La primi due righe contengono una descrizione sintetica delle possibili righe successive.
#   La prima tipologia di riga ha struttura
#   codUtente;abb;prezzoAbbonamento
#   L'esempio seguente
#      25;abb;177
#   indica che l'utente con codice 25 ha sottoscritto un abbonamento per l'accesso pagando 177 euro.
#   La sconda tipologia di riga ha struttura
#   codUtente;sing;dataAccesso1(g/m/aaaa)...data_accessoN
#   In particolare, l'esempio seguente
#      23;sing;14/1/2018;12/1/2018
#   ci dice che l'utente con codice 23 e' entrato nel parco,
#   nei giorni 14/1/2018 e 12/1/2018.
#   In sintesi le righe possono assumere una delle due strutture seguenti
#   (come indicato nelle prime 2 righe del file)
#      codUtente;abb;prezzoAbbonamento
#      codUtente;sing;dataAccesso1(gg/mm/aaaa)...data_accessoN
#   e sono riconoscibili dalla stringa presente
#    dopo il primo punto e virgola, rispettivamente
#      'abb' e
#      'sing'
#   Il file nelle righe di tipo 'sing' registra tutte le entrate di un utente nel parco giochi.
#   Per uno stesso utente ci possono essere piu' righe con le informazioni di 'entrata'.
#   Le righe 'abb' registrano il prezzo pagato da quegli utenti che sottoscrivono
#   un abbonamento per l'ingresso al parco.
#   Gli utenti PAGANO ALLA FINE DELL'ANNO i loro accessi al parco (la
#   direzione del parco si fida).
#   La tariffazione puo' avvenire in due modalita' diverse, a scelta del cliente:
#   - Pagando la somma degli importi dei singoli ingressi
#     (maggiori dettagli sulle tariffe in seguito)
#   - Sottoscrivendo un abbonamento.
#   Un utente che sottoscrive un abbonamento, pagano solo la cifra dell'abbonamento
#   e non deve pagare gli ingressi singoli.
#   L'abbonamento puo' essere sottoscritto in un qualsiasi momento dell'anno (anche
#   dopo diversi ingressi). Se l'utente sottoscrive l'abbonamento,
#   il prezzo dell'abbonamento copre tutti gli ingressi dell'anno, anche quelli
#   precedenti alla sottoscrizione (quindi il cliente
#   non dovrà pagare altro, oltre al costo dell'abbonamento).
#   Il costo dell'abbonamento e' variabile, gli importi pagati sono indicati nel file.
#   L'utente che paga un abbonamento lo paga una sola volta nel periodo di
#   rilevazione dei dati, quindi per un utente ci puo' essere una
#   sola riga di abbonamento.


##########################################################
# DESCRIZIONE DEL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede
# ogni funzione vi spiegherà cosa fare in dettaglio.
# Controllate nel corpo principale del programma (in fondo
# allo script), come vengono invocate le funzioni che
# implementerete.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
# Se volete potete implementare delle funzioni aggiuntive
# rispetto a quelle gia' presenti qua sotto.


##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome = 'Sostituiscimi con il cognome'  # inserisci qua il tuo cognome
nome = 'Sostituiscimi con il nome'  # inserisci qua il tuo nome


# - La funzione seguente accetta come parametro in ingresso
#   il nome del file .csv contenente i dati sugli ingressi e sugli abbonamenti al parco.
#   La funzione deve restituire una lista di tuple, come nell'esempio seguente
#        [ ('entrata', codUtente, data),
#          ('abbonamento', codUtente, importo_abbonamento),
#          ...
#        ]
#   dove ogni tupla contiene i dati o di un ingresso di un utente o di un abbonamento pagato.
#   Le tuple con i dati degli ingressi si distingueranno dalle tuple con i dati sugli abbonamenti
#   grazie alla stringa presente nel primo attributo della tupla ('entrata' o 'abbonamento').
#   Nella lista restituita, ogni tupla di tipo 'entrata' deve contenere una sola data.
#   Se una riga del file contiene diverse date di ingresso (può accadere solo nelle righe
#   del file contenenti la stringa 'sing'), come nell'esempio seguente
#          23;sing;14/1/2018;12/1/2018
#   allora dovranno essere generate più tuple di tipo 'entrata', una per ogni data.
#   Il campo codUtente dovrà contenere un valore intero, il campo data una stringa
#   mentre importo_abbonamento un valore float.
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
#   se in via provvisoria volete far lavorare le funzioni successive senza
#   implementare l'attuale, potete utilizzare la struttura dati dichiarata
#   all'inizio del file.
#   Tale struttura dati e' una versione più corta ma analoga a quella
#   che dovrebbe restituire la vostra implementazione.
#   OVVIAMENTE, se userete la struttura dati gia' presente,
#   l'esercizio sara' considerato non svolto
def leggiDatiIngressiParco(fn):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass


# - La funzione seguente accetta come parametri in ingresso:
#   - una stringa che contiene una data nel formato gg/mm/aaaa.
#     I giorni e i mesi potrebbero usare un'unica cifra, es., 1/3/2018
#   - potete assumere che tutte le date passate saranno comprese
#     tra il 1. gennaio e il 31 dicembre 2018
#   La funzione deve restituire un valore intero corrispondente
#   alla tariffa applicata per un ingresso singolo.
#   Il costo dell'ingresso singolo varia in base al giorno della settimana
#   es., 10 euro il lunedi', 8 euro il martedi', ....
#   Per le tariffe potete usare il dizionario g2t che trovate dentro la funzione.
#   Si suggerisce di
#   - trasformare la data ricevuta in ingresso nel numero di giorni passati
#     dal 1/1/2018 (che era un lunedi'),
#   - calcolare quindi il giorno della settimana (lunedi' o martedi' o ...),
#   - individuare la tariffa e restituire il valore corrispondente
def costoGiornaliero(ds):
    # g2t e' il dizionario per convertire il giorno della settimana in tariffa,
    # la chiave 0 corrisponde a lunedi', 1 a martedi', ...;
    # il valore associato alla chiave e' la tariffa.
    g2t = {0: 10, 1: 8, 2: 6, 3: 7, 4: 11, 5: 15, 6: 16}
    # dizionario che associa ogni mese al numero di giorni contenuti nel mese
    mese2giorni = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
                   8: 31, 9: 30, 10: 31, 11: 30, 12: 31}  # mese:giorni_nel_mese
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.

    pass

    #   - La funzione seguente accetta come parametri in ingresso:
    #       - la struttura dati restituita dalla funzione leggiDatiIngressiParco()
    #   La funzione deve restituire un dizionario dove per ogni visitatore è presente una
    #   coppia chiave:valore avente per chiave il codice dell'utente e per valore la tupla
    #   (prezzo_con_abbonamento, prezzo_senza_abbonamento).
    #   Prezzo con abbonamento rappresenta il costo dell'abbonamento sottoscritto,
    #   mentre prezzo_senza_abbonamento rappresenta il prezzo che l'utente
    #   pagherebbe se non avesse sottoscritto l'abbonamento.
    #   Se un visitatore non ha sottoscritto un abbonamento i 2 valori della tupla
    #   devono coincidere e devono essere pari al prezzo senza abbonamento.
    #   Il prezzo_senza_abbonamento si ottiene sommando i prezzi degli ingressi giornalieri
    #   (calcolati utilizzando la funzione costoGiornaliero) associati a ciascun ingresso effettuato dal visitatore.


def ottieniIncassi(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass

#   - La funzione seguente accetta come parametri in ingresso:
#       - la struttura dati restituita dalla funzione leggiDatiIngressiParco()
#   La funzione deve restituire la differenza tra (a) e (b) dove
#   (a) è quanto la società gestrice del parco
#       avrebbe incassato se tutti gli utenti avessero pagato il totale
#       degli ingressi singoli (cioe' senza usufruire degli abbonamenti) e
#   (b) è quanto la societa' ha effettivamente incassato
#       permettendo gli abbonamenti.
#   Nel calcolo della differenza tra (a) e (b) devono essere escluse
#    le spese di quegli utenti in cui l'uso dell'abbonamento fa poca differenza (vedi sotto).
#   In un utente c'e' "poca differenza" se la differenza tra la somma degli ingressi singoli
#   e il costo dell'abbonamento e' inferiore al 10 per cento
#   del costo dell'abbonamento.


def valutaImpattoAbbonamenti(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass


##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################
print('Esercizio %s.' % (nomeEsercizio))

print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione leggiDatiIngressiParco: ')
nomeFile = 'Esame-uni/Documents/Esame uni/2018-19/2019_05_06/accessiParco.csv'
dp = leggiDatiIngressiParco(nomeFile)
print(dp)

print('2a) Eseguo la funzione costoGiornaliero sul 5/1/2018: ')
cg = costoGiornaliero('5/1/2018')
print(cg)

print('2b) Eseguo la funzione costoGiornaliero sul 20/5/2018: ')
cg = costoGiornaliero('20/5/2018')
print(cg)


print("3) Eseguo la funzione ottieniIncassi: ")
ip = ottieniIncassi(dp)
print(ip)

print("4) Eseguo la funzione valutaImpattoAbbonamenti: ")
imp = valutaImpattoAbbonamenti(dp)
print(imp)

print('Nome e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
