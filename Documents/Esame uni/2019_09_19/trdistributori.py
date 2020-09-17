# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'distributoriAutomatici'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituita da una delle funzioni seguenti,
# La (vera) struttura dati caricata dal file sara' più lunga,
# i primi elementi di entrambe potrebbero non coincidere.
# OVVIAMENTE, se non implementerete la funzione di lettura da file,
# quest'ultima sara' considerata non svolta

datiMacchinette = [(1, 0, 400), (1, 29, 65), (3, 0, 200), (3, 16, 165), (3, 0, 300), (19, 0, 300), (13, 0, 300), (17, 0, 200), (17, 17, 20), (17, 12, 105), (17, 0, 100), (18, 0, 200), (6, 0, 100), (6, 18, 5), (6, 7, 50), (6, 0, 100), (6, 27, 120), (5, 0, 100), (5, 31, 60), (5, 0, 500), (0, 0, 100), (0, 0, 100), (0, 3, 170), (0, 0, 200), (0, 17, 110),
                   (11, 0, 400), (8, 0, 200), (8, 36, 180), (8, 0, 500), (8, 16, 35), (4, 0, 500), (4, 31, 25), (14, 0, 400), (14, 15, 100), (14, 36, 140), (12, 0, 100), (9, 0, 100), (9, 14, 95), (9, 0, 500), (9, 6, 55), (9, 11, 85), (7, 0, 400), (7, 25, 125), (7, 22, 180), (7, 0, 200), (15, 0, 400), (15, 7, 185), (10, 0, 200), (10, 36, 70), (10, 0, 400)]


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritto qua di seguito.
#
# - File 1) 'macchinette.csv'
#   Il file memorizza le informazioni sui soldi caricati e spesi su
#   macchinette distributrici di caffe', snack, etc.
#   I clienti hanno delle chiavette su cui possono caricare soldi, e dalle
#   quali vengono detratti gli importi delle consumazioni effettuate.
#   Un esempio del contenuto del file e' il seguente.
#   Nell'esempio qua sotto non considerate il simbolo di # e
#   gli spazi iniziali. Gli a capo (\r\n) sono stati omessi per semplicita'.
#
#
#        id_cliente;tipo_operazione1;importo1;...;tipo_operazioneN;importoN
#        1;0;400;29;65
#        3;0;200;16;165;0;300
#        19;0;300
#        13;0;300
#        17;0;200;17;20;12;105;0;100
#        18;0;200
#        6;0;100;18;5;7;50;0;100;27;120
#        5;0;100;31;60;0;500
#        0;0;100;0;100;3;170;0;200;17;110
#        ...
#
#   La prima riga contiene l'intestazione del file.
#   Ogni riga del file contiene informazioni sulle operazioni svolte
#   da un cliente su una macchinetta.
#   IMPORTANTE: in ogni riga ci possono essere le informazioni su
#    una o più operazioni svolte dal cliente.
#   In ogni record (record e' un sinonimo di 'riga')
#   sono memorizzate le seguenti informazioni:
#   - id_cliente. Un valore numerico che identifica univocamente un cliente
#   - Da 1 a N coppie di valori, dove ogni coppia e' formata rispettivamente
#     da 'tipo_operazione' e 'importo'
#     * Se 'tipo_operazione' e' uguale a 0 allora si tratta di una
#       ricarica di soldi nella chiavetta e 'valore' rappresenta l'importo caricato.
#     * Se 'tipo_operazione' e' maggiore di 0, allora si tratta di un acquisto.
#       Il valore presente in 'tipo_operazione' in questo caso rappresenta
#       l'identificatore del prodotto acquistato,
#       mentre in 'importo' e' memorizzato il costo del prodotto.
#     * In entrambi i casi precedenti, i valori degli importi sono
#       espressi in centesimi di euro, quindi, per esempio,
#       150 rappresenta 1 euro e mezzo.
#    Nell'esempio seguente
#        id_cliente;tipo_operazione1;importo1;...;tipo_operazioneN;importoN
#        1;0;400;29;65
#        3;0;200;16;165;0;300
#   La seconda riga (quella successiva all'intestazione) ci dice che il cliente 1
#   ha ricaricato 4 euro e ha acquistato il prodotto 29 pagando 65 centesimi di euro.
#   La terza riga ci dice che il cliente 3 ha ricaricato 2 euro,
#   poi ha acquistato il prodotto 16 (costo 1,65 euro), poi ha caricato 3 euro.
#   Nota bene:
#   * Ogni riga contiene informazioni su un solo cliente
#   * L'ordine delle operazioni puo' variare da riga a riga
#     (la ricarica non e' sempre la prima operazione)
#   * I dati di un cliente possono essere presenti su righe diverse, non vicine tra loro.


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
#   il nome del file .csv contenente i dati descritti in precedenza.
#   La funzione deve restituire una lista di tuple, come nell'esempio seguente.
#        [ (id_cliente1, prodotto_o_operazione1, importo1),
#          (id_cliente2, prodotto_o_operazione2, importo2),
#          ...
#          (id_clienteN, prodotto_o_operazioneN, importoN)
#        ]
#   dove ogni tupla rappresenta un'operazione svolta da un cliente.
#   In id_cliente va inserito l'id del cliente,
#   in prodotto_o_operazione andrà 0 se si tratta di una ricarica
#   oppure l'id del prodotto se si tratta di un acquisto,
#   in importo andra' l'importo della ricarica o dell'acquisto.
#   Tutti i valori della tupla devono essere di tipo intero,
#   in importo i valori dovranno essere espressi in centesimi di euro.
#   Per esempio, la funzione applicata ad un file con il contenuto seguente
#        id_cliente;tipo_operazione1;importo1;...;tipo_operazioneN;importoN
#        1;0;400;29;65
#        3;0;200;16;165;0;300
#   dovrebbe restituire
#   [ (1, 0, 400), (1, 29, 65), (3, 0, 200), (3, 16, 165), (3, 0, 300) ]
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
#   se in via provvisoria volete far lavorare le funzioni successive senza
#   implementare l'attuale, potete utilizzare la struttura dati dichiarata
#   all'inizio di questo script (basta togliere il commento alla prima riga della funzione).

def caricaDatiMacchinette(fn):
    # return datiMacchinette # se non riuscite ad implementare la funzione, potete usare temporaneamente qs dati
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass


# - La funzione seguente accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiMacchinette().
#   La funzione deve restituire un valore intero corrispondente al totale incassato
#   con la vendita dei prodotti il cui prezzo di vendita e'
#   compreso tra "1 euro e 50 centesimi" e "2 euro" (estremi esclusi).
def incassoTotale(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass


# - La funzione seguente accetta come parametro in ingresso la struttura dati
#   restituita dalla funzione caricaDatiMacchinette().
#   La funzione seguente deve restituire un dizionario come nell'esempio seguente
#        {
#         id_cliente1:saldo_residuo1,
#         id_cliente2:saldo_residuo2,
#         ...,
#         id_clienteN:saldo_residuoN
#        }
#   Ogni coppia riporta informazioni sulla quantita' di
#   denaro rimasta nella chiavetta del cliente (il saldo residuo)
#   dopo lo svolgimento delle operazioni descritte nel file csv.
#   Nella struttura dati restituita,
#   * id_cliente riporta l'identificatore del cliente,
#   * saldo_residuo riporta la somma rimasta nella chiavetta.
#   Tutte le chiavette hanno un credito iniziale
#   pari a 0 prima del primo utilizzo.
def saldoResiduo(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass


# - La funzione seguente accetta come parametro in ingresso la struttura dati
#   restituita dalla funzione caricaDatiMacchinette().
#   La funzione seguente deve restituire un dizionario come nell'esempio seguente
#        {
#          id_cliente1:[id_prodottoX, num_acquistiX],
#          id_cliente2:[id_prodottoY, num_acquistiY],
#          ...
#          id_clienteN:[id_prodottoZ, num_acquistiZ],
#        }
#   Ogni chiave del dizionario corrisponde all'id di un cliente che ha almeno effettuato
#   una ricarica o un'acquisto alle macchinette.
#   Ad ogni chiave deve essere associata una lista con due informazioni:
#   *  l'id del prodotto piu' acquistato dal cliente
#   *  il numero di volte in cui il prodotto
#      (del punto precedente) e' stato acquistato
#      dal cliente.
#   Alcune precisazioni che vi possono essere utili:
#   - Per vostra semplicita', ogni acquisto nelle  macchinette corrisponde
#     all'erogazione di un unico prodotto.
#   - Se piu' prodotti a pari merito risultano tra i piu' acquistati da un cliente,
#     sceglietene uno con un criterio a vostra scelta.
#   - se per un id_cliente non ci fossero vendite, inserire
#     * il valore -1 come id prodotto e
#     * il valore -1 come num_acquisti
def prodottoPiuVenduto(ds):
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

print('1) Eseguo la funzione caricaDatiMacchinette: ')
fnv = './macchinette.csv'
dv = caricaDatiMacchinette(fnv)
print(dv)

print("2) Eseguo la funzione incassoTotale: ")
it = incassoTotale(dv)
print(it)

print('3) Eseguo la funzione saldoResiduo: ')
sr = saldoResiduo(dv)
print(sr)

print("4) Eseguo la funzione prodottoPiuVenduto: ")
ppv = prodottoPiuVenduto(dv)
print(ppv)

print('Nome file e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
