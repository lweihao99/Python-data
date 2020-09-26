# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'capsuleCaffe'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituita da una delle funzioni seguenti,
# La (vera) struttura dati caricata dal file sara' più lunga,
# i primi elementi di entrambe possono essere diversi.
# OVVIAMENTE, se non implementerete la funzione di lettura da file,
# quest'ultima sara' considerata non svolta

datiCapsule=[(5, '03/01/2019', 'lungo', 10, 1.41), (5, '03/01/2019', 'arabico', 40, 1.75), (5, '03/01/2019', 'normale', 20, 0.9), (5, '03/01/2019', 'ristretto', 50, 1.64), (15, '07/01/2019', 'lungo', 50, 1.35), (15, '07/01/2019', 'ristretto', 20, 1.63), (15, '07/01/2019', 'robusto', 40, 1.81), (14, '09/01/2019', 'decaffeinato', 40, 1.26), (17, '09/01/2019', 'decaffeinato', 30, 1.12), (17, '09/01/2019', 'normale', 40, 0.99), (17, '09/01/2019', 'lungo', 20, 1.59), (17, '09/01/2019', 'intenso', 20, 1.16), (2, '11/01/2019', 'decaffeinato', 30, 1.05), (2, '11/01/2019', 'robusto', 40, 1.96), (10, '13/01/2019', 'arabico', 30, 1.39), (10, '13/01/2019', 'decaffeinato', 30, 1.27), (10, '13/01/2019', 'lungo', 40, 1.77), (17, '14/01/2019', 'arabico', 30, 1.75), (17, '14/01/2019', 'robusto', 40, 1.65), (17, '14/01/2019', 'lungo', 10, 1.21), (17, '14/01/2019', 'intenso', 20, 1.28), (17, '14/01/2019', 'normale', 40, 0.93), (3, '16/01/2019', 'forte', 10, 1.41), (3, '16/01/2019', 'normale', 50, 1.0), (3, '16/01/2019', 'ristretto', 30, 1.79), (20, '21/01/2019', 'decaffeinato', 40, 1.02), (9, '22/01/2019', 'lungo', 10, 1.33), (18, '22/01/2019', 'normale', 10, 1.05), (18, '22/01/2019', 'forte', 40, 1.48), (18, '22/01/2019', 'ristretto', 30, 1.56), (18, '22/01/2019', 'robusto', 10, 1.98), (18, '22/01/2019', 'lungo', 50, 1.69), (13, '23/01/2019', 'lungo', 40, 1.75), (13, '23/01/2019', 'arabico', 20, 1.93), (13, '23/01/2019', 'decaffeinato', 10, 1.06), (13, '23/01/2019', 'forte', 10, 1.14), (7, '24/01/2019', 'lungo', 40, 1.35), (7, '24/01/2019', 'robusto', 10, 1.49), (7, '24/01/2019', 'normale', 40, 0.95), (7, '24/01/2019', 'decaffeinato', 50, 0.97), (7, '24/01/2019', 'arabico', 10, 2.02), (8, '24/01/2019', 'decaffeinato', 20, 1.22), (16, '24/01/2019', 'decaffeinato', 30, 1.17), (16, '24/01/2019', 'intenso', 50, 1.04), (16, '24/01/2019', 'robusto', 50, 1.87), (16, '24/01/2019', 'normale', 10, 0.82), (7, '27/01/2019', 'normale', 40, 0.91), (7, '27/01/2019', 'forte', 30, 1.06), (7, '27/01/2019', 'decaffeinato', 50, 1.21), (7, '27/01/2019', 'lungo', 30, 1.51), (7, '27/01/2019', 'intenso', 10, 1.04), (19, '27/01/2019', 'robusto', 20, 2.07), (19, '27/01/2019', 'arabico', 30, 1.63), (19, '27/01/2019', 'forte', 30, 1.09), (19, '27/01/2019', 'decaffeinato', 20, 0.95), (6, '28/01/2019', 'forte', 20, 1.1), (6, '28/01/2019', 'decaffeinato', 20, 0.93), (6, '28/01/2019', 'normale', 30, 1.1), (6, '28/01/2019', 'robusto', 50, 1.85), (6, '28/01/2019', 'lungo', 30, 1.2), (9, '29/01/2019', 'arabico', 40, 1.88), (5, '31/01/2019', 'ristretto', 10, 1.32), (5, '31/01/2019', 'arabico', 20, 1.76), (5, '31/01/2019', 'robusto', 30, 2.05), (5, '31/01/2019', 'lungo', 50, 1.2), (5, '31/01/2019', 'normale', 10, 1.1), (10, '04/02/2019', 'forte', 20, 1.07), (10, '04/02/2019', 'arabico', 50, 1.41), (10, '04/02/2019', 'robusto', 30, 2.12), (10, '04/02/2019', 'intenso', 30, 1.29), (20, '06/02/2019', 'robusto', 40, 1.78), (20, '06/02/2019', 'normale', 20, 0.84), (3, '06/02/2019', 'decaffeinato', 40, 1.12), (3, '06/02/2019', 'lungo', 50, 1.71), (19, '07/02/2019', 'normale', 30, 0.92), (19, '07/02/2019', 'arabico', 50, 1.95), (19, '07/02/2019', 'forte', 20, 1.41), (19, '07/02/2019', 'ristretto', 30, 1.8), (19, '07/02/2019', 'intenso', 10, 1.15), (1, '07/02/2019', 'arabico', 30, 2.0)]


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritto qua di seguito.
#
# - File 1) 'capsule.csv'
#   Il file memorizza le informazioni sugli acquisti di caffe' in capsule
#   effettuate da dei clienti.
#   Un esempio del contenuto del file e' il seguente. 
#   Nell'esempio qua sotto non considerate il simbolo di # e
#   gli spazi iniziali. Gli a capo presenti nel file (\r\n) sono stati omessi per semplicita'.
#
#   id_cliente;data;tipo_caps1;qt1;pz_unit1;tipo_caps2;qt2;pz_unit2;...;tipo_capsN;qtN;pz_unitN
#   5;03/01/2019;lungo;10;1.41;arabico;40;1.75;normale;20;0.90;ristretto;50;1.64
#   15;07/01/2019;lungo;50;1.35;ristretto;20;1.63;robusto;40;1.81
#   14;09/01/2019;decaffeinato;40;1.26
#   17;09/01/2019;decaffeinato;30;1.12;normale;40;0.99;lungo;20;1.59;intenso;20;1.16
#   2;11/01/2019;decaffeinato;30;1.05;robusto;40;1.96
#   ...
#
#   La prima riga contiene l'intestazione del file.
#   IMPORTANTE: ogni riga successiva alla prima contiene informazioni sugli
#   acquisti effettuati dai clienti.
#   In ogni record (record e' un sinonimo di 'riga') 
#   sono memorizzate le seguenti informazioni:
#   - id_cliente. Un valore numerico che identifica univocamente un cliente
#   - data. La data in cui e' avvenuto l'acquisto
#   - Da 1 a N terne di valori (il numero di terne varia di riga in riga).
#     All'interno di una riga, le terne si ripetono una dietro 
#     all'altra, ogni terna e' formata rispettivamente 
#     da 'tipo_caps', 'qt' e 'pz_unit'
#     * 'tipo_caps' e' una stringa che rappresenta il tipo di 
#       capsula acquistata (es., 'ristretto')
#     * 'qt' e' un intero che rappresenta la quantita' di capsule
#       acquistate dall'utente (del tipo specificato in 'tipo_caps')
#     * 'pz_unit' e' un float che rappresenta il costo di acquisto
#       in euro di una singola capsula. Per esempio 1.50 significa
#       che la capsula è costata 1 euro e 50 centesimi
#     
#
#   Nell'esempio seguente
#      id_cliente;data;tipo_caps1;qt1;pz_unit1;tipo_caps2;qt2;pz_unit2;...;tipo_capsN;qtN;pz_unitN
#      14;09/01/2019;decaffeinato;40;1.26
#      5;03/01/2019;lungo;10;1.41;arabico;40;1.75;normale;20;0.90;ristretto;50;1.64
#      15;07/01/2019;lungo;50;1.35;ristretto;20;1.63;robusto;40;1.81
#
#   La seconda riga (quella successiva all'intestazione) contiene solo una terna e
#     ci dice che il cliente 14 in data 09/01/2019 
#     ha acquistato 40 capsule di 'decaffeinato' pagando 1.26 euro a capsula.
#   La terza riga contiene 4 terne e ci dice che 
#     il cliente 5 in data 03/01/2019 ha acquistato 
#     10 capsule di 'lungo' pagando 1.41 euro a capsula,
#     40 capsule di 'arabico' pagando 1.75 euro a capsula,
#     20 capsule di 'normale' pagando 0.90 euro a capsula,
#     50 capsule di 'ristretto' pagando 1.64 euro a capsula.
#
#   Nota bene: 
#   * Ogni riga contiene informazioni su un solo cliente
#   * I dati di un cliente possono essere presenti su piu' righe, 
#     non necessariamente vicine tra loro (acquisti in giorni diversi). 


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
#        [ (id_cliente1, data1, tipo_capsula1, quantita1, importo_unitario1),
#          (id_cliente2, data2, tipo_capsula2, quantita2, importo_unitario2),
#          ...
#         ]
#   dove ogni tupla contiene le informazioni su un'acquisto di 
#   un singolo tipo di capsula da parte di un cliente. 
#   In id_cliente va inserito l'id del cliente, in data la data dell'acquisto, etc.
#   Se in un record del file sono presenti N terne di valori 
#   (che fanno riferimento all'acquisto di N tipologie di capsule diverse),
#   nella lista dovranno essere inserite N tuple distinte (in cui id_cliente e data si ripetono)
#   con i dati delle N tipologie di capsule acquistate.
#   Per esempio, la funzione applicata ad un file con il contenuto seguente
#      id_cliente;data;tipo_caps1;qt1;pz_unit1;tipo_caps2;qt2;pz_unit2;...;tipo_capsN;qtN;pz_unitN
#      ...
#      5;03/01/2019;lungo;10;1.41;arabico;40;1.75;normale;20;0.90;ristretto;50;1.64
#      ...
#   La funzione dovrebbe restituire una struttura dati come la seguente 
#   [ ..., 
#     (5, '03/01/2019', 'lungo', 10, 1.41), 
#     (5, '03/01/2019', 'arabico', 40, 1.75), 
#     (5, '03/01/2019', 'normale', 20, 0.90), 
#     (5, '03/01/2019', 'ristretto', 50, 1.64), 
#     ...
#   ]  
#   In ogni tupla, 
#   - id_cliente e quantita' devono essere di tipo intero, 
#   - data e tipo_capsula devono essere di tipo stringa
#   - importo_unitario deve essere di tipo float
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
#   se in via provvisoria volete far lavorare le funzioni successive senza
#   implementare l'attuale, potete utilizzare la struttura dati dichiarata
#   all'inizio di questo script (basta togliere il commento dalla prima riga di codice).

def caricaDatiCapsule(fn):
    #return datiCapsule # se non riuscite ad implementare la funzione, potete usare temporaneamente questa
    pass # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    li=[]
    fd = open(fn, 'r')
    fd.readline() # salto la riga con l'intestazione
    for line in fd:
        line=line.strip('\n').strip('\r') # Come terminatore di riga e' usato \r\n. Levo prima il \n e poi il \r
        fields = line.split(';')
        # id_cliente;data;tipo_caps1;qt1;pz_unit1;tipo_caps2;qt2;pz_unit2;...;tipo_capsN;qtN;pz_unitN
        idCliente=int(fields[0])
        data=fields[1]
        i=2
        while i<len(fields):
            tipoCapsula=fields[i]
            qt=int(fields[i+1])
            importoUnitario=float(fields[i+2])
            li.append( (idCliente, data, tipoCapsula, qt, importoUnitario) )
            i+=3
    fd.close()
    return li

# - La funzione seguente accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiCapsule().
#   La funzione seguente deve restituire un dizionario come nell'esempio seguente
#        {
#         tipo_capsula1:[totale_quantita1, incasso_totale1],
#         tipo_capsula2:[totale_quantita2, incasso_totale2],
#         ...,
#        }
#   Ogni coppia riporta informazioni sui dati di vendita di un tipo di capsula.
#   La chiave e' una stringa contenente il tipo di capsula (es., 'ristretto', 'arabico', ...).
#   Il valore associato alla chiave e' una lista formata da due valori, rispettivamente 
#   * il totale delle capsule vendute
#   * la cifra totale incassata dalla vendita
#   Deve essere presente un'unica coppia chiave valore nel dizionario
#   per ogni tipo diverso di capsula.
def totaliVenditeCapsule(ds):
    pass # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    di={}
    for tu in ds:
        tipoCapsula=tu[2]
        if tipoCapsula not in di:
            di[tipoCapsula]=[0,0]
        qt=tu[3]
        importoUnitario=tu[4]

        di[tipoCapsula][0] += qt
        di[tipoCapsula][1] += qt*importoUnitario
    return di

   

# - La funzione seguente accetta come parametro in ingresso la struttura dati
#   restituita dalla funzione caricaDatiCapsule().
#   La funzione seguente deve individuare i dati del "cliente mediano", 
#   rispetto al totale delle capsule acquistate.
#   Trovate in fondo le indicazioni su come calcolare il cliente mediano.
#   Se ci fossero piu' clienti mediani possibili, sceglietene 
#   uno come meglio preferite.
#   La funzione deve restituire la tupla seguente:
#      (id_cliente_mediano, totale_capsule_acquistate_dal_cliente_mediano)
#   I due valori all'interno della tupla devono essere entrambi interi. 
#   
#   CLIENTE MEDIANO
#   Per calcolare il cliente mediano rispetto al 
#   totale delle capsule acquistate da ogni cliente dovete:
#   1) calcolare per ogni cliente il totale delle quantita' di capsule
#       acquistate (indipendentemente dalla tipologia).
#   2) Ordinare i totali in ordine crescente. NOTA BENE: non potete usare sort(), sorted(),
#      o una funzione di ordinamento gia' implementata, 
#      dovete implementare voi un algoritmo di ordinamento.
#   3) dovete recuperare l'id del cliente le cui quantita' occupano 
#      il punto centrale della lista.
#      Data una lista li, la posizione centrale puo' essere calcolata con int(len(li)/2) 
def clienteMediano(ds):
    pass # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    diCli={}
    for tu in ds:
        # (id_cliente1, data1, tipo_capsula1, quantita1, importo_unitario1),
        idCli=tu[0]
        if idCli not in diCli:
            diCli[idCli]=0
        qt=tu[3]
        diCli[idCli] += qt

    # creo una lista di idClienti. Poi posso ordinare la lista sulla base delle qt acquistate dai clienti
    liIdCli=[]
    for idCli in diCli:
        liIdCli.append( idCli ) # memorizzo solo le chiavi, successivamente ordinero' le chiavi sulla base dei valori associati
    
    #ora, procedo ad ordinare liIdCli con il selection sort
    for i in range(len(liIdCli)-1):
        maxIdPos=i
        for j in range(i+1, len(liIdCli)):
            if diCli[liIdCli[j]] > diCli[liIdCli[maxIdPos]]:
                maxIdPos=j
        #swapping the key in position maxId with the key in position i
        temp=liIdCli[i]
        liIdCli[i] = liIdCli[maxIdPos]
        liIdCli[maxIdPos] = temp
    
    # cerco ora il mediano
    posMediano=int(len(liIdCli)/2)
    keyMediano = liIdCli[posMediano]
    totCapsuleMediano=diCli[keyMediano]
    return (keyMediano, totCapsuleMediano)


##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################

print('Esercizio %s.' % (nomeEsercizio))
print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione caricaDatiCapsule: ')
fnv='capsule.csv'
dc = caricaDatiCapsule(fnv)
print(dc)

print('2) Eseguo la funzione totaliVenditeCapsule: ')
tvc = totaliVenditeCapsule(dc)
print(tvc)

print("3) Eseguo la funzione clienteMediano")
cm = clienteMediano(dc)
print(cm)

print('Nome file e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
