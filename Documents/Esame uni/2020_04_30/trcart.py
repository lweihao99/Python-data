# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'ecommerceCart'

# Vi forniamo esempi di strutturea dati che potrebbero
# essere restituite dalle funzioni seguenti.
# La (vera) struttura dati caricata dal file sara' più lunga,
# i primi elementi di entrambe possono essere diversi.

datiCarrelli = [(17, 'ADD', 18, 3), (17, 'ADD', 5, 1), (24, 'ADD', 43, 4), (16, 'ADD', 3, 8), (17, 'ADD', 5, 7), (17, 'ADD', 6, 1), (17, 'DROP', 6, 1), (17, 'ADD', 6, 4), (24, 'ADD', 43, 3), (16, 'DROP', 3, 1), (24, 'CHECKOUT'), (17, 'CHECKOUT'), (29, 'ADD', 26, 9), (16, 'ADD', 3, 9), (14, 'ADD', 40, 8), (14, 'DROP', 40, 5), (14, 'ADD', 51, 3), (14, 'ADD', 59, 2), (14, 'DROP', 59, 2), (14, 'ADD', 59, 5), (14, 'CHECKOUT'), (29, 'ADD', 26, 6), (16, 'CHECKOUT'), (13, 'ADD', 50, 9), (1, 'ADD', 57, 4), (1, 'DROP', 57, 2), (2, 'ADD', 0, 4), (1, 'ADD', 57, 6), (1, 'CHECKOUT'), (5, 'ADD', 8, 1), (8, 'ADD', 45, 6), (21, 'ADD', 17, 6), (13, 'DROP', 50, 2), (5, 'ADD', 8, 5), (5, 'ADD', 57, 1), (5, 'DROP', 57, 1), (5, 'ADD', 57, 9), (5, 'ADD', 49, 5), (22, 'ADD', 4, 6), (5, 'DROP', 49, 3), (28, 'ADD', 17, 2), (5, 'CHECKOUT'), (2, 'DROP', 0, 3), (27, 'ADD', 3, 1), (21, 'DROP', 17, 1), (30, 'ADD', 47, 4), (2, 'ADD', 52, 2), (30, 'DROP', 47, 2), (2, 'DROP', 52, 1), (2, 'ADD', 32, 6), (21, 'CHECKOUT'), (0, 'ADD', 3, 2), (13, 'ADD', 50, 6), (30, 'ADD', 47, 6), (27, 'ADD', 3, 9), (1, 'ADD', 29, 9), (8, 'ADD', 45, 4), (30, 'ADD', 17, 2), (2, 'ADD', 32, 3), (20, 'ADD', 30, 7), (30, 'DROP', 17, 1), (30, 'ADD', 15, 6), (25, 'ADD', 10, 2), (25, 'CHECKOUT'), (22, 'ADD', 12, 1), (28, 'ADD', 5, 9), (30, 'CHECKOUT'), (17, 'ADD', 41, 9), (22, 'ADD', 12, 8), (8, 'ADD', 24, 8), (27, 'CHECKOUT'), (11, 'ADD', 12, 4), (17, 'ADD', 22, 3), (11, 'DROP', 12, 2), (13, 'CHECKOUT'), (8, 'DROP', 24, 3), (0, 'ADD', 3, 4), (0, 'ADD', 56, 4), (2, 'CHECKOUT'), (1, 'ADD', 29, 5), (1, 'ADD', 13, 8), (11, 'ADD', 12, 3), (17, 'DROP', 22, 2), (11, 'CHECKOUT'), (3, 'ADD', 17, 4), (25, 'ADD', 34, 9), (28, 'DROP', 5, 8), (19, 'ADD', 6, 7), (28, 'CHECKOUT'), (3, 'DROP', 17, 1), (1, 'DROP', 13, 1), (29, 'ADD', 23, 9), (0, 'ADD', 32, 3), (8, 'ADD', 24, 3), (0, 'DROP', 32, 2), (0, 'CHECKOUT'), (25, 'CHECKOUT'), (22, 'CHECKOUT'), (3, 'ADD', 25, 8), (3, 'ADD', 15, 4), (8, 'ADD', 43, 7), (15, 'ADD', 7, 9), (18, 'ADD', 53, 6), (6, 'ADD', 58, 7), (18, 'ADD', 26, 8), (17, 'ADD', 22, 8), (29, 'CHECKOUT'), (20, 'DROP', 30, 1), (1, 'CHECKOUT'), (8, 'CHECKOUT'), (18, 'CHECKOUT'), (17, 'ADD', 9, 5), (28, 'ADD', 15, 9), (3, 'DROP', 15, 4), (30, 'ADD', 50, 5), (5, 'ADD', 31, 7), (20, 'ADD', 30, 7), (28, 'DROP', 15, 8), (3, 'ADD', 15, 4), (5, 'DROP', 31, 2), (28, 'ADD', 15, 8), (28, 'CHECKOUT'), (4, 'ADD', 29, 5), (10, 'ADD', 31, 8), (3, 'CHECKOUT'), (30, 'ADD', 50, 7), (20, 'ADD', 40, 5), (10, 'DROP', 31, 3), (19, 'ADD', 6, 1), (30, 'ADD', 27, 8), (5, 'CHECKOUT'), (14, 'ADD', 9, 5), (9, 'ADD', 29, 6), (22, 'ADD', 2, 5), (17, 'CHECKOUT'), (6, 'ADD', 58, 4), (15, 'DROP', 7, 1), (4, 'DROP', 29, 5), (19, 'ADD', 51, 3), (19, 'DROP', 51, 2), (20, 'DROP', 40, 4), (25, 'ADD', 17, 1), (12, 'ADD', 11, 1), (12, 'CHECKOUT'), (30, 'ADD', 27, 7), (25, 'CHECKOUT'), (30, 'CHECKOUT')] 
composizioneCarrelli = [(24, {43: 7}), (17, {18: 3, 5: 8, 6: 4}), (14, {40: 3, 51: 3, 59: 5}), (16, {3: 16}), (1, {57: 8}), (5, {8: 6, 57: 9, 49: 2}), (21, {17: 5}), (25, {10: 2}), (30, {17: 1, 47: 8, 15: 6}), (27, {3: 10}), (13, {50: 13}), (2, {0: 1, 32: 9, 52: 1}), (11, {12: 5}), (28, {17: 2, 5: 1}), (0, {56: 4, 32: 1, 3: 6}), (25, {34: 9}), (22, {4: 6, 12: 9}), (29, {26: 15, 23: 9}), (1, {29: 14, 13: 7}), (8, {24: 8, 43: 7, 45: 10}), (18, {26: 8, 53: 6}), (28, {15: 9}), (3, {17: 3, 25: 8, 15: 4}), (5, {31: 5}), (17, {41: 9, 22: 9, 9: 5}), (12, {11: 1}), (25, {17: 1}), (30, {50: 12, 27: 15}), (20, {40: 1, 30: 13}), (5, {2: 7, 29: 3}), (12, {26: 8}), (10, {0: 8, 31: 5}), (14, {9: 14}), (9, {29: 6}), (8, {2: 6, 3: 4}), (0, {0: 5, 8: 12, 21: 7}), (15, {7: 8, 15: 8}), (8, {45: 5}), (14, {7: 4}), (28, {0: 5, 20: 7, 15: 2}), (1, {0: 7, 57: 3, 43: 7}), (22, {2: 3}), (29, {1: 7, 21: 3}), (10, {20: 2}), (0, {12: 3}), (25, {25: 5, 3: 12}), (7, {3: 1, 45: 2, 29: 8}), (17, {40: 5, 3: 8}), (30, {13: 17, 54: 3}), (11, {19: 17, 58: 1, 27: 5}), (27, {33: 1, 34: 13, 28: 9}), (19, {51: 1, 37: 7, 6: 8}), (6, {57: 15, 58: 11}), (18, {18: 3, 2: 15, 13: 9}), (21, {35: 2}), (10, {0: 1, 48: 7, 42: 8}), (2, {49: 11, 34: 1, 4: 1}), (28, {31: 4, 30: 5, 39: 2}), (14, {8: 8, 32: 4, 58: 2}), (0, {1: 3, 10: 4, 47: 11}), (15, {42: 4, 58: 12, 54: 3}), (29, {58: 4, 45: 13, 38: 11}), (8, {56: 3, 57: 2, 47: 12}), (1, {0: 13, 4: 6, 44: 8}), (23, {38: 2}), (21, {52: 10, 53: 3}), (28, {16: 7}), (7, {5: 1})]  # ****** da aggiungere

##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritto qua di seguito.
#
# - File 1) 'cart.csv'
#   Un gruppo di utenti utilizza un sito online per effettuare acquisti.
#   Il sito mette a disposizione un carrello virtuale
#   (carrello d'ora in poi), che può essere usato da un cliente per tener
#   traccia dei prodotti che vuole acquistare.
#   L'utente, con un carrello può:
#   - inserire i prodotti (ADD)
#   - eliminare un prodotto precedentemente inserito (DROP)
#   - terminare le operazioni effettuando l'acquisto di tutti gli elementi
#     contenuti nel carrello (CHECKOUT)
#   Ogni volta che un utente esegue un'operazione di ADD, DROP, o CHECKOUT
#   viene registrata una riga nel file csv.
#   Il sito interagisce con più utenti contemporaneamente, le operazioni dei
#   diversi utenti vengono tutte memorizzate nello stesso file csv.
#   Le informazioni presenti in una riga variano a seconda del tipo di
#   operazione memorizzato (ADD, DROP, CHECKOUT).
#   Un esempio del contenuto del file e' il seguente. Ci sono alcune
#   differenze rispetto all'effettivo contenuto, es.: il simbolo #;
#   gli spazi iniziali; gli a capo presenti nel file (\r\n) sono stati omessi.
#
#   TIME;CUSTOMER;OPERATION;...;...
#   00:16:01;17;ADD;18;3
#   00:16:55;17;ADD;5;1
#   00:17:39;24;ADD;43;4
#   00:19:57;16;ADD;3;8
#   00:20:43;17;ADD;5;7
#   00:21:16;17;ADD;6;1
#   00:23:17;17;DROP;6;1
#   00:30:58;17;ADD;6;4
#   00:32:16;24;ADD;43;3
#   00:35:47;16;DROP;3;1
#   00:37:27;24;CHECKOUT      # Qua c'e' un checkout
#   00:41:04;17;CHECKOUT      # Qua c'e' un checkout
#   ...
#
#   La prima riga contiene l'intestazione del file.
#   In ogni record (record e' un sinonimo di 'riga')
#   può essere memorizzata un'operazione (ADD, DROP o CHECKOUT), 
#   maggiori dettagli qua sotto.
#   Una precisazione: anche se le operazioni svolte dai diversi utenti sono
#   memorizzate nello stesso file, ogni utente interagisce solo il contenuto del suo
#   carrello (non vede cioè i carrelli degli altri utenti).
#   - ADD. Una riga con tale operazione, contiene le seguenti informazioni.
#     * TIME. Il momento della giornata in cui è avvenuta l'operazione.
#           Il tempo è espresso nel formato hh:mm:ss (rispettivamente, ore, minuti, secondi).
#           Il file contiene i dati di un solo giorno.
#           Tutti i record sono ordinati in ordine crescente di tempo.
#     * CUSTOMER. Un numero intero che identifica univocamente un utente.
#     * OPERATION. Indica il tipo di operazione memorizzato nella riga,
#           In questo caso è la stringa ADD.
#     * ID_PRODUCT. Un numero intero che identifica il prodotto che l'utente
#           ha inserito nel carrello.
#     * QUANTITY. Un intero che memorizza la quantità di prodotto inserita nel
#           carrello.
#   - DROP. Una riga con tale operazione, contiene le seguenti informazioni.
#     * TIME. ... come sopra.
#     * CUSTOMER. ... come sopra.
#     * OPERATION. E' presente la stringa DROP.
#           Se per esempio nel carrello erano state caricate in precedenza
#            3 unità del prodotto X,
#           L'utente potrebbe fare un drop (cioè una eliminazione) di 1, 2, o 3
#           unità del prodotto X.
#     * ID_PRODUCT. Il prodotto i cui elementi devono essere eliminati dal
#           carrello.
#     * QUANTITY. Un intero che indica la quantità di prodotto da eliminare dal
#           carrello.
#   - CHECKOUT. Una riga con tale operazione, contiene le seguenti informazioni.
#           Attenzione, il numero di elementi è diverso rispetto alle altre
#           tipologie di righe.
#     * TIME. ... come sopra.
#     * CUSTOMER. ... come sopra.
#     * OPERATION. E' presente la stringa CHECKOUT.
#
#   Le operazioni di checkout aiutano di fatto a capire quando un utente
#   termina una sessione di acquisti.
#   Il checkout ha come effetto quello di svuotare il carrello dell'utente
#   (perché l'utente ha terminato l'acquisto).
#   Nota bene: uno stesso utente può anche compiere più acquisti nello stesso
#   giorno.
#   Se un utente inserisce prodotti nel carrello dopo un checkout,
#   significa che l'utente ha dato inizio ad una nuova sessione di acquisto.
#
#   I record presenti nel file sono memorizzati in ordine temporale crescente.
#
#   Nell'esempio seguente
#      TIME;CUSTOMER;OPERATION;...;...
#      ...
#      00:17:39;63;ADD;13;2
#      ...
#      00:22:30;63;ADD;13;1
#      ...
#      00:32:16;63;ADD;27;4
#      ...
#      00:37:27;63;CHECKOUT
#      ...
#   L'utente 63 inserisce 3 unità (2+1) del prodotto 13 nel carrello
#   (2 la priva volta e 1 la seconda volta), 4 unità del prodotto 27
#   e infine esegue il checkout.
#   Nell'esempio seguente
#      TIME;CUSTOMER;OPERATION;...;...
#      ...
#      00:16:01;11;ADD;18;3
#      ...
#      00:21:16;11;ADD;6;1
#      ...
#      00:23:17;11;DROP;6;1
#      ...
#      00:30:58;11;DROP;18;1
#      ...
#      00:41:04;17;CHECKOUT
#   l'utente 11 al momento del checkout acquista 2 unità del prodotto 18 (3-1=2).
#   Il prodotto 6 non viene acquistato perché viene rimosso completamente dal
#    carrello prima del checkout.
#
#   Nota bene:
#   * Ogni riga contiene informazioni su una singola operazione svolta da un
#    cliente.
#   * I dati di un cliente possono essere presenti su piu' righe,
#       non necessariamente vicine tra loro.
#   * Un cliente può svolgere anche diversi checkout.
#   * Cercate di aprire il file .csv con un editor di testo diverso da notepad.


##########################################################
# INTRODUZIONE AL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede
# ogni funzione vi spiegherà in dettaglio che cosa fare.
# Controllate nel corpo principale del programma (in fondo
# allo script), come vengono invocate le funzioni che
# implementerete.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
# Se volete, potete implementare funzioni aggiuntive
# rispetto a quelle gia' presenti qua sotto.

##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################
#
# Se vi sorgessero dei dubbi sull'interpretazione delle richieste qua sotto,
# descrivete in un commento le assunzioni (aggiuntive) sulle quali vi baserete. 
# Assunzioni in evidente violazione delle richieste qua sotto non saranno
# considerate valide. 

cognome = 'Sostituiscimi con il cognome'  # inserisci qua il tuo cognome
nome = 'Sostituiscimi con il nome'  # inserisci qua il tuo nome


# - La funzione seguente accetta come parametro in ingresso
#   il nome del file .csv contenente i dati descritti in precedenza.
#   La funzione deve leggere il contenuto del file e
#   restituire una lista di tuple come nell'esempio seguente.
#        [ (id_cliente1, 'ADD', id_prodottoA, qtA),
#          ...
#          (id_cliente2, 'DROP', id_prodottoB, qtB),
#          ...
#          (id_cliente3, 'CHECKOUT'),
#          ...
#         ]
#   dove ogni tupla contiene le informazioni su un'operazione descritta in una
#   riga del file.
#   Le tre tuple nell'esempio qua sopra memorizzano informazioni sulle
#   operazioni rispettivamente di ADD, DROP e CHECKOUT.
#   L'ordine delle tuple deve essere lo stesso con cui si susseguono le righe
#   nel file.
#   In id_cliente, id_prodotto e qt vanno inseriti valori di tipo intero,
#   'ADD', 'DROP' e 'CHECKOUT' devono essere di tipo stringa.
#
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni
#   successive, se in via provvisoria volete lavorare sulle funzioni successive
#   senza implementare l'attuale, potete utilizzare la struttura dati dichiarata
#   all'inizio di questo script (basta togliere il commento dalla prima riga di
#   codice).
#
def caricaDatiCarrelli(fn):
    #return datiCarrelli # se non riuscite ad implementare la funzione, potete usare temporaneamente questa struttura dati. Tuttavia se lo fate la funzione sarà considerata non svolta.
    # Implementa il codice della funzione qua sotto. Questa riga può essere cancellata.
    pass



# - La funzione seguente accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiCarrelli().
#   La funzione deve restituire una struttura dati come la seguente
#        [ (id_cliente1, {id_prodottoA:qtA, id_prodottoB:qtB, ...}),
#          ...
#          (id_cliente2, {id_prodottoC:qtC, id_prodottoD:qtD, ...}),
#          ...
#          (id_cliente1, {id_prodottoE:qtE, id_prodottoF:qtF, ...}),
#         ]
#   Ogni tupla riporta informazioni sui prodotti acquistati da un cliente al momento
#   del checkout.
#   id_cliente e id_prodotto rappresentano rispettivamente gli utenti che
#   effettuano il checkout e l'id dei prodotti acquistati.
#   I qt rappresentano invece le quantità di prodotti acquistati e
#   non devono essere presenti valori di qt pari a 0 (se un prodotto viene prima aggiunto e
#   poi tolto completamente dal carrello, non deve apparire nella struttura dati).
#   Un utente può effettuare diversi acquisti (corrispondenti a diversi checkout),
#   come id_cliente1 nell'esempio qua sopra. In tal caso, ci deve essere una tupla per ogni
#   checkout.
#
def calcolaComposizione(ds):
    #return composizioneCarrelli # se non riuscite ad implementare la funzione, potete usare temporaneamente questa struttura dati. Tuttavia se lo fate la funzione sarà considerata non svolta.
    # Implementa il codice della funzione qua sotto. Questa riga può essere cancellata.
    pass



# - La funzione seguente accetta come parametro in ingresso la struttura dati
#   restituita dalla funzione calcolaComposizione().
#   La funzione seguente deve restituire una tupla come la seguente
#      ('id_cliente*id_prodotto', qt) #### Corretto un errore rispetto al testo originale
#   dove 'id_cliente*id_prodotto' è una stringa formata da due informazioni separate dall'*.
#   Le due informazioni nella stringa rappresentano la combinazione di
#   id_cliente e id_prodotto che hanno generato la quantità maggiore di prodotto venduta
#   comprensiva di tutte le sessioni ad un singolo cliente.
#   Per esempio ('18*23', 55) #### Corretto un errore rispetto al testo originale
#   significa che l'id_cliente 18 ha acquistato l'id_prodotto 23
#   per un totale di 55 unità, e tale combinazione è la combinazione di utente e prodotto
#   che ha venduto di più. Se l'id_utente 18 ha acquistato l'id_prodotto 23 in diverse
#   sessioni di acquisto (ognuna quindi con il suo checkout), il valore 55 rappresenta
#   il totale delle unità di id_prodotto 23 acquistate nei diversi checkout.
#   Se ci fossero più combinazioni di id_cliente e id_prodotto che a pari merito hanno
#   effettuato la stessa quantità massima di unità acquistate, sceglietene una con il
#   criterio che preferite.
#
def combinazioneMaggiore(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    



##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))
print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione caricaDatiCarrelli: ')
fnv = 'cart.csv'
ds1 = caricaDatiCarrelli(fnv)
print(ds1)

print('2) Eseguo la funzione calcolaComposizione: ')
ds2 = calcolaComposizione(ds1)
print(ds2)

print("3) Eseguo la funzione combinazioneMaggiore: ")
cm = combinazioneMaggiore(ds2)
print(cm)

print('Nome file e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
