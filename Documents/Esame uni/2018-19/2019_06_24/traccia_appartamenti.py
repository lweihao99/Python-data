# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe
from __future__ import print_function

nomeEsercizio = 'appartamenti'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituito da una delle funzioni seguenti,
# La vera struttura dati caricata dal file sara' più lunga,
# i primi elementi delle due strutture dati non è detto che coincidano.

datiAppartamenti = [
    ('inserimento', 0, 1, 50, 100000),
    ('modifica', 0, 2, 90000),
    ('vendita', 0, 3),
    ('inserimento', 1, 5, 60, 300000),
    ('modifica', 1, 6, 346000),
    ('vendita', 1, 8),
    ('inserimento', 91, 9, 290, 1160000),
    ('inserimento', 76, 11, 120, 480000),
    ('modifica', 91, 19, 1344000),
    ('modifica', 76, 21, 416000),
    ('modifica', 91, 49, 1074000),
    ('modifica', 91, 62, 1109000),
    ('vendita', 76, 255),
    ('vendita', 91, 318)
]
##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritto qua di seguito
#
# - File 1) 'appartamenti.csv'
#   Il file memorizza le informazioni sugli annunci di vendita
#   di appartamenti pubblicati attraverso un sito web.
#   Nel file sono presenti TRE DIVERSE TIPOLOGIE di righe,
#   il tipo riga è riconoscibile in base alla stringa presente
#   subito dopo tr=  come negli esempi qua sotto. I valori sono separati da ;
#   Nel file non c'è intestazione (la prima riga contiene già dati).
#   Nell'esempio qua sotto non considerate il simbolo di # e
#   gli spazi iniziali. Gli a capo (\r\n) sono stati omessi per semplicità.
#
#        tr=inserimento;idAp=0;data=1;m2=50;prezzo=100000
#        tr=modifica;idAp=0;data=25;prezzo=90000
#        tr=vendita;idAp=0;data=131
#        ...
#
#  Nel file sono presenti TRE DIVERSE TIPOLOGIE di righe, rispettivamente righe con
#     * tr=inserimento. Questa riga contiene le informazioni su un annuncio di vendita, con
#       queste informazioni:
#         - idAp è un valore numerico che identifica univocamente l'appartamento,
#         - data è la data di pubblicazione dell'annuncio. Una data è un valore intero compreso
#           tra 1 e 365 che rappresenta il giorno dell'anno in cui è avvenuta la pubblicazione.
#         - m2 rappresenta i metri quadrati dell'appartamento
#         - prezzo rappresenta il prezzo, espresso come valore intero, al quale inizialmente
#            è stato messo in vendita l'appartamento
#     * tr=modifica. Questa riga contiene le informazioni su una modifica di prezzo di un appartamento
#       precedentemente messo in vendita. Ogni volta che viene modificato il prezzo di vendita,
#       al file viene aggiunta una riga come questa che riporta il nuovo prezzo di vendita.
#       Le informazioni contenute nella riga sono:
#       - idAp è l'identificatore dell'appartamento a cui è stato cambiato il prezzo
#       - data è la data in cui è avvenuta la modifica. Anche questa data può assumere
#         un valore intero compreso tra 1 e 365
#       - prezzo è il nuovo prezzo
#       Un appartamento può subire diverse modifiche di prezzo (o può non subirne).
#       Ogni volta che viene effettuata una modifica, si aggiunge una riga nel file
#     * tr=vendita. Questa riga contiene le informazioni sulla data in cui è stato
#       venduto l'appartamento. Le informazioni contenute nelle righe di questo tipo sono:
#       - idAp è l'identificatore dell'appartamento venduto
#       - data è la data in cui è avvenuta la vendita. Anche qua data può assumere un valore intero
#         compreso tra 1 e 365
#
#  Nota bene: per ogni appartamento nel file c'è sicuramente una riga di tipo "inserimento"
#  e una riga di tipo "vendita".
#  Per un appartamento, le righe di "modifica" possono essere assenti o essercene più di una.
#  Le informazioni presenti nel file sono ordinate in base alla data. Quindi le informazioni
#  sull'inserimento, modifica (prezzo) e vendita di uno stesso appartamento possono essere
#  anche distanti tra loro.


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
#   il nome del file .csv contenente i dati sugli annunci di vendita.
#   La funzione deve restituire una lista di tuple, come nell'esempio seguente
#        [
#          ('inserimento', idAp, data, m2, prezzo),
#          ('modifica', idAp, data, prezzo),
#          ('vendita', idAp, data),
#          ...
#        ]
#   dove ogni tupla contiene i dati di una riga del file.
#   L'ordine delle tuple deve essere lo stesso ordine con cui le righe sono presenti nel file.
#   Il primo elemento (stringa) di ogni tupla permette di distinguere il tipo riga letto.
#   Tutti gli altri elementi della tupla devono essere valori interi,
#   le informazioni 'idAp=', 'data=', ... presenti nel file non devono essere inserite nella tupla.
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
#   se in via provvisoria volete far lavorare le funzioni successive senza
#   implementare l'attuale, potete utilizzare la struttura dati dichiarata in precedenza.
#   Tale struttura dati e' una versione più corta ma analoga a quella
#   che dovrebbe restituire la vostra implementazione.
#   OVVIAMENTE, se userete la struttura dati gia' presente,
#   l'esercizio sara' considerato non svolto
def caricaDatiAppartamenti(fn):
    # return datiAppartamenti # se non riuscite ad implementare la funzione, potete usare temporaneamente qs dati
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    file = open(fn, 'r')
    li = []
    for i in file:
        i = i.strip('\n').strip('\r')
        temp = i.split(';')
        temp_dict = {}
        for item in temp:
            new_temp = item.split('=')
            temp_dict[new_temp[0]] = new_temp[1]
        if temp_dict['tr'] == 'inserimento':
            tu = (temp_dict['tr'], temp_dict['idAp'],
                  temp_dict['data'], temp_dict['m2'], temp_dict['prezzo'])
        if temp_dict['tr'] == 'modifica':
            tu = (temp_dict['tr'], temp_dict['idAp'],
                  temp_dict['data'], temp_dict['prezzo'])
        if temp_dict['tr'] == 'vendita':
            tu = (temp_dict['tr'], temp_dict['idAp'], temp_dict['data'])
        li.append(tu)
    return li


# - La funzione seguente accetta come parametro in ingresso la struttura dati
#   restituita dalla funzione caricaDatiAppartamenti()
#   La funzione seguente deve restituire una lista di tuple come nell'esempio seguente
#        [ (idAp, data_pubblicazione, data_vendita, prezzo_iniziale, prezzo_vendita, numero_variazioni),
#          ...
#        ]
#   Ogni tupla riporta informazioni su un appartamento.
#   Il prezzo di vendita di un appartamento è il prezzo riportato nell'ultima modifica
#   (se ci sono state modifiche), oppure il prezzo_iniziale (se non ci sono state modifiche).
#   Il prezzo_iniziale è il prezzo inserito al momento della pubblicazione dell'annuncio.
#   L'elemento numero_variazioni rappresenta il numero di variazioni di prezzo,
#   è pari a 0 per gli appartamenti che non hanno subito variazioni di prezzo.
#   I valori nella tupla devono essere tutti interi.
#   Alcune precisazioni che vi possono essere utili:
#   - le righe presenti nel file sono in ordine di data,
#   - per ogni appartamento esiste sempre nel file
#     una riga di tipo 'inserimento' e una di tipo 'vendita', in giorni diversi
#   - un appartamento può avere o non avere righe di tipo  'variazione'.
#   - se per un appartamento ci sono state più variazioni di prezzo, queste sono avvenute in giorni diversi
def sommarioAppartamenti(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    temp_dict = {}
    for item in ds:
        tipo = item[0]
        idAp = item[1]
        if tipo == 'inserimento':
            # 没有的数据写0,0是为了占位置,这样方便索引
            temp_dict[idAp] = [item[2], 0, item[4], 0, 0]
        if tipo == 'modifica':
            temp_dict[idAp][3] = item[3]  # prezzo vendita
            temp_dict[idAp][4] += 1  # 每次发生了价格的变动,就加一次numero variazioni
        if tipo == 'vendita':
            temp_dict[idAp][1] = item[2]  # data vendita
    li = []
    for key in temp_dict:
        li.append((key, temp_dict[key][0], temp_dict[key][1],
                   temp_dict[key][2], temp_dict[key][3], temp_dict[key][4]))
    return li


# - La funzione seguente accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione sommarioAppartamenti().
#   La funzione deve restituire un dizionario con una struttura come nell'esempio seguente
#   {
#       'aumenti':[idAp1, idAp2, ...],
#       'diminuzioni':[idAp3, idAp5, ...]
#   }
#   dove alla chiave 'aumenti' deve essere associata una lista contenente gli identificatori degli appartamenti (idAp) in cui il prezzo di vendita è risultato maggiore del prezzo iniziale (cioè il prezzo al momento della pubblicazione dell'annuncio).
#   Alla chiave 'diminuzioni' deve essere invece associata una lista con gli idAp degli appartamenti in cui il prezzo di vendita è risultato inferiore al prezzo iniziale.
#   Gli appartamenti con prezzo di vendita invariato non devono essere inseriti nella struttura dati.
def variazioniPrezzi(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    li_aumenti = []
    li_diminuzioni = []
    for item in ds:
        prezzo_iniziale = int(item[3])
        prezzo_vendita = int(item[4])
        id_app = int(item[0])
        if prezzo_vendita > prezzo_iniziale:
            li_aumenti.append(id_app)
        elif prezzo_iniziale > prezzo_vendita:
            li_diminuzioni.append(id_app)
    di = {'aumenti': li_aumenti, 'diminuzioni': li_diminuzioni}
    return di


# - La funzione seguente accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione sommarioAppartamenti().
#   La funzione deve restituire un dizionario con una struttura come nell'esempio seguente
#   {
#       0:numero_appartamenti0, 1:numero_appartamenti1, 2:numero_appartamenti2, ...
#   }
#   dove alla chiave 0 deve essere associato il numero di appartamenti che hanno subito 0 modifiche al prezzo,
#   alla chiave 1 deve essere associato il numero di appartamenti che hanno subito 1 modifica al prezzo, ...
#   alla chiave n deve essere associato il numero di appartamenti che hanno subito n modifiche al prezzo.
#
def contaVariazioniAppartamenti(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    di = {}
    for item in ds:
        num_variazioni = int(item[5])
        if num_variazioni in di:
            di[num_variazioni] += 1
        else:
            di[num_variazioni] = 1
    return di


##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################
print('Esercizio %s.' % (nomeEsercizio))
print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione caricaDatiAppartamenti: ')
fna = 'Esame-uni/Documents/Esame uni/2018-19/2019_06_24/appartamenti.csv'
da = caricaDatiAppartamenti(fna)
print(da)

print('2) Eseguo la funzione sommarioAppartamenti: ')
sa = sommarioAppartamenti(da)
print(sa)

print("3) Eseguo la funzione variazioniPrezzi: ")
vp = variazioniPrezzi(sa)
print(vp)

print("4) Eseguo la funzione contaVariazioniAppartamenti: ")
varap = contaVariazioniAppartamenti(sa)
print(varap)

print('Nome file e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
