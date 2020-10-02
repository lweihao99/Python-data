# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'prenotazioniRistoranti'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituita da una delle funzioni seguenti,
# La (vera) struttura dati caricata dal file sara' più lunga,
# i primi elementi di entrambe possono essere diversi.
# OVVIAMENTE, se non implementerete la funzione di lettura da file,
# quest'ultima sara' considerata non svolta

datiPrenotazioni = [(0, 1, 12, 3, [7630, 5656, 6738]), (0, 1, 13, 3, [4944]), (0, 1, 12, 3, [2520, 803, 2432, 3146]), (0, 1, 14, 2, [3009, 5237, 1863]), (0, 1, 13, 2, [9484, 5200, 682, 9372]), (0, 1, 14, 2, [9325, 2536]), (0, 1, 12, 3, [6860, 8280, 5124]), (0, 1, 13, 1, [3698]), (0, 1, 13, 3, [5107, 3801, 6254]), (0, 1, 13, 3, [6947, 3732, 5178]), (0, 1, 14, 3, [3207, 6892, 1195]), (0, 1, 13, 1, [2538, 3917, 7875]), (0, 1, 13, 1, [67, 8231]), (0, 1, 13, 3, [8230, 1385]), (0, 1, 14, 2, [9151]), (0, 1, 14, 1, [4762, 1427, 4253]), (0, 1, 14, 2, [7602, 7692, 6122, 9022]), (0, 1, 13, 2, [1009, 4890]), (0, 1, 14, 2, [2426]), (0, 1, 13, 1, [7392]), (0, 1, 19, 1, [213, 6865, 5663]), (0, 1, 22, 3, [5174, 3040, 5977]), (0, 1, 19, 1, [5976, 1375, 4430]), (0, 1, 21, 1, [1433, 1646, 4150]), (0, 1, 20, 3, [2895, 8185]), (0, 1, 22, 3, [2719]), (0, 1, 19, 3, [929, 9359]), (0, 1, 19, 1, [4528, 8550, 5884, 1365]), (0, 1, 20, 3, [7772]), (0, 1, 20, 2, [7884, 4836]), (0, 1, 20, 1, [1733, 6040, 50]), (0, 1, 19, 2, [5960, 6915]), (0, 1, 20, 2, [436, 8447]), (0, 1, 21, 3, [6304, 1112, 6208]), (0, 1, 20, 1, [1793]), (0, 1, 19, 2, [1277, 5665]), (0, 1, 22, 3, [6209]), (0, 1, 21, 2, [4671, 3428]), (0, 1, 20, 1, [8538, 9689, 3737]), (0, 1, 19, 1, [6688]), (0, 1, 19, 2, [7021, 6298, 7668, 6098]), (1, 1, 13, 1, [9376]), (1, 1, 12, 2, [8385, 7561, 471, 316]), (1, 1, 13, 1, [2552]), (1, 1, 14, 3, [8803, 8754, 1821, 9981]), (1, 1, 13, 3, [2284, 9176, 6194, 6926]), (1, 1, 13, 3, [3330]), (1, 1, 14, 3, [5710, 706, 4776]), (1, 1, 12, 1, [4983, 3232]), (1, 1, 14, 1, [7092]), (1, 1, 13, 3, [5742, 5735, 1010]), (1, 1, 13, 2, [1729]), (1, 1, 12, 1, [5330, 8561]), (1, 1, 12, 1, [4757]), (1, 1, 13, 1, [2551, 1666]), (1, 1, 13, 1, [2651]), (1, 1, 12, 2, [6661, 3044]), (1, 1, 13, 1, [8413, 1132, 7895, 6432]), (1, 1, 14, 3, [7828, 4530, 4001, 5620]), (1, 1, 20, 3, [3958, 7729]), (1, 1, 20, 2, [7346, 2259]), (1, 1, 22, 1, [1067]), (1, 1, 20, 3, [151, 9038, 5513, 730]), (1, 1, 20, 1, [4030, 1227, 560, 3512]), (1, 1, 19, 2, [6634, 4320, 3869]), (1, 1, 20, 2, [1422]), (1, 1, 19, 3, [765, 2158, 9397]), (1, 1, 21, 1, [9162, 7210]), (1, 1, 20, 3, [9580, 8207, 831]), (1, 1, 21, 3, [7809, 7874, 2247, 4438]), (1, 1, 19, 3, [3809, 3550, 2643, 1164]),
                    (1, 1, 19, 1, [7020, 2755, 9653, 595]), (1, 1, 22, 1, [251, 4408]), (1, 1, 21, 3, [301, 4779, 9317]), (1, 1, 21, 1, [53, 9572, 6528, 2873]), (1, 1, 21, 3, [9449, 6475, 8987, 2038]), (2, 1, 13, 3, [3659, 9312, 6233, 1149]), (2, 1, 14, 2, [7518, 1395]), (2, 1, 13, 1, [9653, 4918, 7069, 3792]), (2, 1, 12, 2, [9219, 7156]), (2, 1, 22, 3, [3691]), (2, 1, 20, 1, [6291, 8379, 2727]), (2, 1, 22, 2, [9741, 8018, 7991, 1859]), (2, 1, 21, 2, [6756, 6243, 8116, 3493]), (2, 1, 22, 1, [4523]), (2, 1, 21, 1, [202, 9567, 6258, 4714]), (3, 1, 13, 1, [8585, 5491]), (3, 1, 12, 1, [5390, 2712, 7506]), (3, 1, 13, 1, [4504, 2811]), (3, 1, 12, 1, [9198]), (3, 1, 14, 3, [8092, 9039]), (3, 1, 13, 1, [1263, 1773, 920]), (3, 1, 12, 3, [9505]), (3, 1, 12, 2, [9948]), (3, 1, 12, 2, [3881, 8159]), (3, 1, 13, 3, [4526, 7651]), (3, 1, 14, 1, [3422]), (3, 1, 12, 1, [1880]), (3, 1, 12, 3, [1954, 8183, 8843, 6907]), (3, 1, 12, 3, [3984, 198, 5217, 6816]), (3, 1, 13, 3, [935, 6724, 9229]), (3, 1, 12, 3, [7141, 9114]), (3, 1, 12, 3, [432, 5156, 8478]), (3, 1, 13, 3, [1675, 8696, 7283]), (3, 1, 14, 1, [6463, 7064]), (3, 1, 14, 2, [3748]), (3, 1, 12, 3, [5836, 6888, 2084]), (3, 1, 14, 2, [6413, 5600, 282, 25]), (3, 1, 13, 2, [3184]), (3, 1, 12, 1, [4027, 9089, 7445]), (3, 1, 13, 1, [6680, 7475]), (3, 1, 14, 3, [2861, 4754, 5667, 6690]), (3, 1, 13, 1, [2537, 1954, 149]), (3, 1, 13, 1, [9900, 68]), (3, 1, 12, 1, [5185, 9588, 4219]), (3, 1, 13, 1, [6502, 2732, 8055]), (3, 1, 13, 2, [3450, 5343]), (3, 1, 12, 1, [1122]), (3, 1, 22, 3, [6682, 9306]), (3, 1, 22, 1, [8733, 3446, 7134]), (3, 1, 19, 1, [6072, 1394, 200, 2155]), (3, 1, 21, 1, [483, 437, 4632]), (3, 1, 20, 1, [1503]), (3, 1, 20, 3, [5303, 1926, 4824, 5953]), (3, 1, 19, 3, [2992, 1250]), (3, 1, 21, 1, [5883, 6156, 5740, 683]), (3, 1, 19, 3, [4431, 2347]), (3, 1, 20, 1, [3780, 4585, 732, 4097]), (3, 1, 19, 2, [1351, 7066]), (3, 1, 21, 1, [3213, 4791]), (3, 1, 22, 3, [7047, 5803]), (3, 1, 22, 3, [3997, 4542, 9998]), (3, 1, 22, 2, [6885]), (3, 1, 21, 1, [9860]), (3, 1, 19, 3, [9049, 6212, 441, 2450]), (3, 1, 20, 3, [3694, 6431, 8283]), (0, 5, 12, 3, [7630, 5656]), (3, 1, 19, 1, [1488, 1152]), (3, 1, 20, 2, [7871]), (3, 1, 22, 2, [5249, 3203]), (4, 1, 20, 1, [8116])]


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritto qua di seguito.
#
# - File 1) 'prenotazioni.csv'
#   Il file memorizza le informazioni sulle prenotazioni
#   dei tavoli (di una catena di ristoranti) effettuate dai clienti.
#   Un esempio del contenuto del file e' il seguente.
#   Nell'esempio qua sotto non considerate
#   il simbolo di # e gli spazi iniziali.
#   Gli a capo presenti nel file (\r\n) sono stati omessi per semplicita'.
#
#   id_ristorante;giorno:oraInizio:durata;id_cliente1;...;id_clienteN
#   0;1:13:1;87;25;8;24
#   0;1:12:3;74;30
#   0;1:13:1;51;86;94
#   0;1:13:1;94;47;48;93
#   0;1:12:1;67;68;82
#   0;1:13:2;21
#   0;1:13:2;62;51;38
#   0;1:13:2;64;69;37;51
#   0;1:14:3;32;68;11
#   ...
#
#   La prima riga contiene l'intestazione del file.
#   IMPORTANTE: ogni riga successiva alla prima contiene informazioni sulle
#   prenotazioni effettuate dai clienti.
#   In ogni record (record e' un sinonimo di 'riga')
#   sono memorizzate le seguenti informazioni:
#   - id_ristorante. Un valore numerico che identifica univocamente
#     il ristorante presso il quale e' stata effettuata la prenotazione
#   - giorno:oraInizio:durata. Tre valori numerici interi
#     separati da : che rappresentano rispettivamente:
#     * giorno. il giorno del mese nel quale e' stata fatta la prenotazione.
#       Il file contiene i dati di un solo mese.
#     * oraInizio. L'ora per la quale è stato prenotato il tavolo.
#     * durata. Il numero di ore per le quali è stato prenotato il tavolo,
#       puo' assumere valori pari a 1, 2 o 3.
#   - id_cliente1;...;id_clienteN. Un insieme di valori numerici
#     (il cui numero puo' variare riga per riga) che identificano
#     i clienti che mangeranno al tavolo.
#     Il numero di clienti varia da una prenotazione all'altra
#     ma sempre tra un minimo di 1 persona ed un massimo di 4 persone.
#     Per esempio in
#       0;1:13:1;87;25;8;24
#     sono presenti tre id_cliente, rispettivamente 25, 8 e 24.
#     mentre in
#       0;1:13:2;21
#     la prenotazione e' stata effettuata per il solo cliente 21.
#     In quest'ultima prenotazione, il tavolo è stato prenotato
#     per due ore, a partire dalle ore 13.
#
#   Nota bene:
#   * Ogni riga contiene informazioni su una sola prenotazione
#   * Le prenotazioni di un ristorante sono sparse
#     su diverse righe, non necessariamente vicine tra loro.


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

cognome = 'Sostituiscimi con il cognome'  # inserisci qua il tuo cognome
nome = 'Sostituiscimi con il nome'  # inserisci qua il tuo nome


# - La funzione seguente accetta come parametro in ingresso
#   il nome del file .csv contenente i dati descritti in precedenza.
#   La funzione deve leggere il contenuto del file e
#   restituire una lista di tuple, come nell'esempio seguente.
#        [ (id_ristorante1, giorno1, oraInizio1, durata1, [id_cliente1, id_cliente2, ...]),
#          (id_ristorante2, giorno2, oraInizio2, durata2, [id_cliente5,  ...]),
#          ...
#         ]
#   dove ogni tupla contiene le informazioni su una prenotazione.
#   Per esempio, la funzione applicata ad un file con il contenuto seguente
#      id_ristorante;giorno:oraInizio:durata;id_cliente1;...;id_clienteN
#      ...
#      0;1:13:1;87;25;8;24
#      5;1:12:3;74;30
#      8;1:13:1;51;86;94
#      ...
#   dovrebbe restituire una struttura dati come la seguente
#   [ ...,
#     (0, 1, 13, 1, [87, 25, 8, 24] ), # l'ultimo elemento della tupla e' una lista
#     (5, 1, 12, 3, [74, 30] ),
#     (8, 1, 13, 1, [51, 86, 94] ),
#     ...
#   ]
#   In ogni tupla,
#   - I valori di id_ristorante, giorno, oraInizio e durata
#     devono essere di tipo intero.
#   - La lista con all'interno gli id_cliente non
#     ha dimensione costante.
#   - I valori degli id_cliente nella lista interna
#     devono essere di tipo intero.
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
#   se in via provvisoria volete lavorare sulle funzioni successive senza
#   implementare l'attuale, potete utilizzare la struttura dati dichiarata
#   all'inizio di questo script (basta togliere il commento dalla prima riga di codice).
def caricaDatiPrenotazioni(fn):
    #        [ (id_ristorante1, giorno1, oraInizio1, durata1, [id_cliente1, id_cliente2, ...]),
    #          (id_ristorante2, giorno2, oraInizio2, durata2, [id_cliente5,  ...]),
    #          ...
    #         ]
    file = open(fn, 'r')
    file.readline()
    li = []
    for line in file:
        line = line.strip('\n').strip('\r')
        content = line.split(';')

        idRistorante = int(content[0])
        data = content[1]
        new_data = data.split(':')
        gg = int(new_data[0])
        ora_inizio = int(new_data[1])
        durata = int(new_data[2])
        temp_li = []
        for item in range(2, len(content)):
            temp_li.append(int(content[item]))
        li.append((idRistorante, gg, ora_inizio, durata, temp_li))

    file.close()

    return li


# - La funzione seguente accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiPrenotazioni().
#   La funzione seguente deve restituire un dizionario come nell'esempio seguente
#        {
#           id_cliente1:num_prenotazioni1, id_cliente2:num_prenotazioni2, ...
#        }
#   Dove ad ogni id_cliente deve essere associato il numero delle prenotazioni
#   in cui il cliente e' coinvolto (considerando tutti i ristoranti).
#   Per vostra semplicità, se un cliente non ha prenotazioni,
#   non deve essere presente nel dizionario.
def clientiAssidui(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    di = {}
    for item in ds:
        li_idCliente = item[4]
        for idCliente in li_idCliente:
            if idCliente not in di:
                di[idCliente] = 1
            else:
                di[idCliente] += 1

    return di


# - La funzione seguente accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiPrenotazioni().
#   La funzione seguente deve restituire un dizionario come nell'esempio seguente
#        {
#         id_ristorante1:{'giornoA_oraX':numero_prenotazioni, 'giornoB_oraY':numero_prenotazioni, ...},
#         id_ristorante2:{'giornoC_oraZ':numero_prenotazioni, 'giornoD_oraK':numero_prenotazioni, ...},
#         ...,
#        }
#   Nel dizionario piu' esterno ci devono essere tante coppie chiave:valore
#   quanti sono i ristoranti (prenotati). Associato ad ogni id_ristorante,
#   ci deve essere un dizionario con diverse coppie
#      'giornoC_oraZ':numero_prenotazioni,
#   in cui la chiave e' una stringa formata da giorno e ora separati da un '_'
#   e il valore è un intero con il numero di prenotazioni
#   previste nel ristorante nel tal giorno e ora. Per vostra semplicita',
#   le combinazioni di giorno e ora in cui in un ristorante non è presente
#   alcuna prenotazione non devono essere inserite nella struttura dati
#   associata all'id del ristorante.
#   Sempre per vostra semplicita', i ristoranti che non hanno prenotazioni
#   non devono essere inseriti nella struttura dati restituita.
def numeroPrenotazioni(ds):
    #        {
    #         id_ristorante1:{'giornoA_oraX':numero_prenotazioni, 'giornoB_oraY':numero_prenotazioni, ...},
    #         id_ristorante2:{'giornoC_oraZ':numero_prenotazioni, 'giornoD_oraK':numero_prenotazioni, ...},
    #         ...,
    #        }
    di = {}
    for tu in ds:
        idRistorante = tu[0]
        if idRistorante not in di:
            di[idRistorante] = {}

        giorno = tu[1]
        ora = tu[2]
        durata = tu[3]
        for i in range(ora, ora+durata):
            giorno_ora = str(giorno)+'_'+str(i)
            if giorno_ora not in di[idRistorante]:
                di[idRistorante][giorno_ora] = 1
            else:
                di[idRistorante][giorno_ora] += 1
    return di

    # - La funzione seguente accetta come parametro in ingresso la struttura dati
    #   restituita dalla funzione caricaDatiPrenotazioni().
    #   La funzione seguente deve individuare la coppia di utenti che più frequentemente
    #   prenotano assieme (sul concetto di coppia, trovate alcune indicazioni aggiuntive
    #   in fondo a questo commento).
    #   Se ci fossero piu' coppie con lo stesso numero di prenotazioni,
    #   sceglietene una come meglio preferite.
    #   La funzione deve restituire la tupla seguente:
    #      (id_cliente1, id_cliente2, n_prenotazioni_assieme)
    #   I tre valori all'interno della tupla restituita devono essere entrambi interi.
    #
    #   COPPIE DI UTENTI
    #   Le prenotazioni singole, non contano per il computo del numero di apparizione delle coppie.
    #   Le prenotazioni con due persone, contano 1 nel conteggio delle coppie.
    #   Nelle prenotazioni con 3 o 4 persone, vanno identificate tutte le coppie possibili
    #   (tutte le possibili combinazioni di persone prese a due a due), es., se nella prenotazione erano presenti
    #   4 persone (A B C D), le possibili coppie sono: AB, AC, AD, BC, BD, CD.
    #   Ognuna di queste coppie conta 1 nel conteggio delle coppie.
    #   L'ordine delle persone non conta nella coppia, cioè AB e BA sono la stessa coppia.
    #   Una coppia non puo' essere formata dalla stessa persona. Per vostra semplicita',
    #   precisiamo che nei dati delle prenotazioni contenute nel file .csv,
    #   una persona appare al massimo una volta nella stessa prenotazione.


def coppieFrequenti(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    di = {}
    for tu in ds:
        idCliente = tu[4]
        i = 0
        while i < len(idCliente):
            j = i+1
            # per avere tutte le coppie possibili 1,2 1,3 1,4 2,3 2,4....
            while j < len(idCliente):
                if idCliente[i] < idCliente[j]:
                    k = (idCliente[i], idCliente[j])
                else:
                    k = (idCliente[j], idCliente[i])

                if k not in di:  # 每个组合判断一遍有没有在字典里
                    di[k] = 1
                else:
                    di[k] += 1
                j += 1
            i += 1
    maxPair = -1
    maxPair2 = -1
    numPrenotazione = -1
    for key in di:
        if di[key] > numPrenotazione:
            numPrenotazione = di[key]
            maxPair = key[0]
            maxPair2 = key[1]

    return ((int(maxPair), int(maxPair2)), numPrenotazione)


##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################
print('Esercizio %s.' % (nomeEsercizio))
print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione caricaDatiPrenotazioni: ')
fnv = 'Esame-uni/Documents/Esame uni/2020_07_01/prenotazioni.csv'
dpr = caricaDatiPrenotazioni(fnv)
print(dpr)

print('2) Eseguo la funzione clientiAssidui: ')
ca = clientiAssidui(dpr)
print(ca)

print('3) Eseguo la funzione numeroPrenotazioni: ')
numpr = numeroPrenotazioni(dpr)
print(numpr)

print("4) Eseguo la funzione coppieFrequenti")
cf = coppieFrequenti(dpr)
print(cf)

print('Nome file e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
