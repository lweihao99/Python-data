# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'flottaAuto'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituita da una delle funzioni seguenti.
# La (vera) struttura dati caricata dal file sara' diversa:
# può essere più lunga, i primi elementi possono differire come valori.

datiFlotta = [('G1', 'VU120TM', 10, 90), ('G1', 'ML147OE', 45, 359), ('G1', 'WQ616LH', 40, 518), ('G1', 'JT776XI', 5, 55), ('G1', 'GC237KT', 5, 31), ('G1', 'QZ499GB', 15, 117), ('G1', 'EK274HV', 45, 403), ('G2', 'NI744BS', 20, 154), ('G2', 'GC237KT', 10, 65), ('G2', 'EP016HP', 40, 598), ('G2', 'KF234TQ', 30, 185), ('G2', 'GM127CC', 5, 79), ('G2', 'EN065TU', 15, 248), ('G2', 'RJ530VN', 20, 360), ('G2', 'PD452QD', 20, 218), ('G2', 'QA408MW', 10, 81), ('G2', 'GV183BX', 40, 475), ('G3', 'GM127CC', 30, 552), ('G3', 'JT776XI', 5, 46), ('G3', 'RJ530VN', 5, 89), ('G3', 'EV599RN', 25, 120), ('G3', 'EP016HP', 20, 234), ('G3', 'NJ637QS', 10, 135), ('G3', 'BA867OR', 5, 64), ('G3', 'VU120TM', 15, 124), ('G3', 'OH062GK', 25, 141), ('G3', 'HN165WY', 35, 450), ('G3', 'NB994MY', 25, 403), ('G4', 'PD470UJ', 35, 504), ('G4', 'BA867OR', 50, 742), ('G4', 'EK274HV', 20, 177), ('G4', 'ML147OE', 25, 169), ('G4', 'EP016HP', 20, 286), ('G4', 'WQ616LH', 15, 266), ('G4', 'EN065TU', 20, 302), ('G4', 'GM127CC', 10, 152), ('G4', 'KF234TQ', 35, 239), ('G4', 'GG666VN', 5, 111), ('G4', 'JN795IR', 30, 344),
              ('G5', 'GC237KT', 20, 120), ('G5', 'RJ530VN', 25, 454), ('G5', 'DI052KU', 35, 407), ('G5', 'BA867OR', 20, 297), ('G5', 'QZ499GB', 25, 145), ('G6', 'EV599RN', 40, 199), ('G6', 'EK274HV', 15, 141), ('G7', 'OH062GK', 5, 30), ('G7', 'DI052KU', 40, 547), ('G7', 'PD470UJ', 40, 672), ('G7', 'EN065TU', 15, 264), ('G7', 'GG666VN', 15, 336), ('G7', 'SN351FS', 50, 950), ('G7', 'VF541LZ', 20, 180), ('G7', 'EK274HV', 10, 65), ('G7', 'GM127CC', 5, 94), ('G8', 'GG666VN', 35, 764), ('G8', 'EP016HP', 35, 368), ('G8', 'QZ499GB', 25, 206), ('G8', 'CY009LW', 35, 148), ('G8', 'RJ530VN', 50, 720), ('G8', 'NB994MY', 50, 1007), ('G8', 'OH062GK', 15, 97), ('G8', 'NJ637QS', 40, 632), ('G9', 'EN065TU', 45, 834), ('G9', 'NI744BS', 25, 192), ('G9', 'GC237KT', 10, 67), ('G9', 'BA867OR', 20, 354), ('G9', 'VF541LZ', 50, 500), ('G9', 'WQ616LH', 40, 608), ('G9', 'CY009LW', 15, 78), ('G9', 'GG666VN', 20, 444), ('G9', 'SN351FS', 40, 912), ('G9', 'QA408MW', 45, 517), ('G9', 'EV599RN', 5, 28), ('G10', 'EV599RN', 15, 104), ('G10', 'EN065TU', 30, 621), ('G10', 'GM127CC', 50, 896), ('G10', 'PD470UJ', 40, 522), ]


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da editare (questo file)
# e un file dati descritto qua di seguito.
#
# - File 'consumiFlotta.csv'
#   Il file memorizza le informazioni sulle auto utilizzate
#   da un gruppo di guidatori, sui km percorsi e sui
#   litri di carburante consumati.
#   Un esempio del contenuto del file e' contenuto nella stringa seguente.
#   La prima riga descrive la struttura delle righe successive.
#   I valori sono separati da ; e per andare a capo e' utilizzato il \n
"""
id_guidatore;targa1;litri1;km1;targa2;litri2;km2;...;targaN;litriN;kmN
G1;VU120TM;10L;90KM;ML147OE;45L;359KM
G2;NI744BS;20L;154KM;GC237KT;10L;65KM;EP016HP;40L;598KM
G3;GM127CC;30L;552KM;JT776XI;5L;46KM;RJ530VN;5L;89KM;EV599RN;25L;120KM;EP016HP;20L;234KM;NJ637QS;10L;135KM;BA867OR;5L;64KM;VU120TM;15L;124KM;OH062GK;25L;141KM;HN165WY;35L;450KM;NB994MY;25L;403KM
G4;PD470UJ;35L;504KM;BA867OR;50L;742KM;EK274HV;20L;177KM;ML147OE;25L;169KM;EP016HP;20L;286KM;WQ616LH;15L;266KM;EN065TU;20L;302KM;GM127CC;10L;152KM;KF234TQ;35L;239KM;GG666VN;5L;111KM;JN795IR;30L;344KM
G5;GC237KT;20L;120KM;RJ530VN;25L;454KM;DI052KU;35L;407KM;BA867OR;20L;297KM;QZ499GB;25L;145KM
G6;EV599RN;40L;199KM;EK274HV;15L;141KM
...
"""
#   In ogni record (record e' un sinonimo di 'riga')
#   sono memorizzate le auto guidate da un guidatore, i litri consumati ed i
#   km percorsi. Attenzione, quando un guidatore guida diversi veicoli,
#   su una riga ci sono i dati di piu' veicoli.
#   Le informazioni sono organizzate nel modo seguente.
#   - id_guidatore. E' sempre la prima informazione della riga.
#     Si tratta di una stringa che inizia con 'G' e che identifica
#     univocamente un guidatore.
#   - targa. Per esempio AA123BB, è la targa dell'auto guidata.
#   - litri. Sono i litri di carburante consumati dall'autista alla guida
#     dell'auto (la cui targa si trova a sinistra di litri).
#   - km percorsi. I km percorsi dall'autista con il veicolo.
#   - ...
#     se nella riga sono presenti i dati di piu' veicoli,
#     per ogni veicolo sono riportati (sempre nello stesso ordine)
#     targa, litri, e km percorsi. Litri e km si possono
#     riconoscere oltre che dall'ordine, anche dalla/e lettere finali,
#     rispettivamente L e KM.
#
#   Alcune note sul contenuto del file
#   - Il numero dei dati presente in ogni riga cambia in base
#     al numero di veicoli guidati dal guidatore.
#   - Lo stesso veicolo puo' essere guidato da piu' guidatori,
#     pertanto la targa di un veicolo puo' apparire in diverse righe.
#     Tuttavia, i dati presenti in una riga fanno riferimento solo
#     ai litri consumati e ai km percorsi dal guidatore
#     a cui la riga fa riferimento.
#   - In una riga, una stessa targa non puo' essere presente piu' di
#     una volta.
#
#   ***NOTA BENE***: aprite il file .csv
#     - con un editor di testo diverso da notepad
#     - senza usare excel (o programmi similari)

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
# Se volete, potete implementare delle funzioni aggiuntive
# rispetto a quelle gia' presenti qua sotto.


##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome = 'Liu'  # inserisci qua il tuo cognome
nome = 'Weihao'  # inserisci qua il tuo nome


# - La funzione seguente, caricaDatiFlotta(), accetta come parametro in ingresso
#   il nome del file .csv contenente i dati descritti in precedenza.
#   La funzione deve leggere il contenuto del file e
#   restituire una lista di tuple, come nell'esempio seguente:
#        [
#          ('id_guidatore1', 'targa_auto1', litri, km_percorsi),
#          ('id_guidatore1', 'targa_auto2', litri, km_percorsi),
#          ('id_guidatore2', 'targa_auto5', litri, km_percorsi),
#          ('id_guidatore2', 'targa_auto6', litri, km_percorsi),
#          ...
#        ]
#   dove ogni tupla contiene le informazioni su litri e km percorsi
#   da un autista su un'auto.
#   Per esempio, la funzione applicata ad un file con il contenuto seguente
"""
id_guidatore;targa1;litri1;km1;targa2;litri2;km2;...;targaN;litriN;kmN
G1;VU120TM;10L;90KM;ML147OE;45L;359KM;WQ616LH;40L;518KM
G2;NI744BS;20L;154KM
...
"""
#   deve restituire una struttura dati come la seguente
#   [
#     ('G1','VU120TM',10,90), # gli ultimi due valori sono rispettivamente i litri e i chilometri percorsi
#     ('G1','ML147OE',45,359),
#     ('G1','WQ616LH',40,518), # qui finiscono i dati della prima riga
#     ('G2','NI744BS',20,154),
#     ...
#   ]
#   In ogni tupla, litri e km percorsi devono essere valori interi.
#   NOTA BENE: il risultato restituito da questa funzione e' utilizzato dalle funzioni
#   successive, se in via provvisoria volete lavorare sulle funzioni successive
#   senza implementare l'attuale, potete utilizzare la struttura dati creata
#   all'inizio di questo script (per usarla dentro la funzione seguente,
#   basta togliere il commento dalla prima riga di codice).
#   In quest'ultimo caso tuttavia la funzione sara' considerata non implementata.


def caricaDatiFlotta(fn):
    # return datiFlotta # se non riuscite ad implementare la funzione, potete usare temporaneamente questa struttura dati
    # Implementate qua sotto il codice della funzione. La riga con il pass puo' essere cancellata.
    file = open(fn, 'r')
    file.readline()
    li = []
    for line in file:
        line = line.strip('\n').strip('\r')
        content = line.split(';')
        idGuidatore = content[0]
        temp = 1
        while temp < len(content):
            targa = content[temp]
            litri = content[temp+1]
            litri = litri.split('L')
            litriInt = int(litri[0])
            km = content[temp+2]
            km = km.split('KM')
            kmInt = int(km[0])
            temp += 3
            li.append((idGuidatore, targa, litriInt, kmInt))
    return li

# - La funzione trovaPiedePesante() accetta come parametri in ingresso
#   la struttura dati restituita dalla funzione caricaDatiFlotta().
#   La funzione trovaPiedePesante() deve restituire le informazioni sul
#   guidatore che ha il valore piu' basso dell'indicatore
#   km_per_litro = (totale chilometri percorsi dal guidatore) / (totale dei litri consumati dal guidatore).
#   Precisazione: un auto puo' essere usata da piu' guidatori, tuttavia
#   nel calcolo dell'indicatore per un guidatore vanno considerati
#   solo i km percorsi e il carburante da lui consumato.
#   Se ci fossero piu' guidatori a pari merito, con il valore piu' basso
#   dell'indicatore km_per_litro, sceglietene uno come meglio preferite.
#   La funzione deve restituire una tupla come la seguente
#   (id_guidatore, km_totali, litri_totali, km_per_litro)
#   con i dati del guidatore selezionato.
#   km_totali rappresenta i km totali percorsi dal guidatore,
#   litri_totali e' il totale dei litri consumati dal guidatore,
#   km_per_litro e' il rapporto tra i due valori precedenti e
#   deve essere di tipo float.


def trovaPiedePesante(ds):
    # Implementate qua sotto il codice della funzione. La riga con il pass puo' essere cancellata.
    dizKm = {}
    dizLt = {}
    for tu in ds:
        (idGuidatore, targa, litri, km) = tu
        if idGuidatore not in dizKm:
            dizKm[idGuidatore] = km
            dizLt[idGuidatore] = litri
        else:
            dizKm[idGuidatore] += km
            dizLt[idGuidatore] += litri

    minKmPerLitro = 99999999
    minKm = 0
    minLitro = 0
    idG = ''
    for idGuidatore in dizKm:
        kmPerLitro = int(dizKm[idGuidatore] / dizLt[idGuidatore])

        if minKmPerLitro > kmPerLitro:
            minKmPerLitro = kmPerLitro
            minKm = int(dizKm[idGuidatore])
            minLitro = int(dizLt[idGuidatore])
            idG = idGuidatore

    return (idG, minKm, minLitro, minKmPerLitro)


# - La funzione trovaAuto() accetta come parametri in ingresso
#   la struttura dati restituita dalla funzione caricaDatiFlotta().
#   La funzione trovaAuto() deve individuare le 5 auto che hanno
#   percorso piu' strada (considerando la strada percorsa da tutti
#   i guidatori).
#   La funzione deve restituire una lista di 5 targhe, come
#   nell'esempio seguente (i valori non coincidono con il risultato
#   che dovrete ottenere)
#      ['AA123BB', 'CC456DD', ... 'kk747JJ']
#   Le targhe devono essere ordinate, da sinistra verso destra
#   in ordine decrescente di km percorsi. Se ci fossero
#   auto con pari percorrenza, scegliete voi in che ordine disporli.
#   In ogni caso, la lista restituita deve avere solo 5 elementi.
# - Facoltativo: non utilizzate le funzioni di ordinamento presenti
#   in libreria ma implementate voi un algoritmo di ordinamento.
#   Facoltativo significa che non siete obbligati a farlo, ma se lo fate
#   potreste prendere dei punti extra.
def trovaAuto(ds):
    # Implementate qua sotto il codice della funzione. La riga con il pass puo' essere cancellata.
    di = {}
    for tu in ds:
        (idGuidatore, targa, litri, km) = tu
        if targa not in di:
            di[targa] = km
        else:
            di[targa] += km

    temp_li = []
    # usare il commando del dizionario per ordinare in ordine crescente dei values. che non mi ricordo


# - La funzione seguente, accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiFlotta().
#   La funzione deve individuare l'auto che e' stata guidata dal maggior numero
#   di guidatori, considerando tuttavia solo le persone che
#   hanno guidato almeno 4 auto diverse.
#   La funzione deve restituire una stringa con la targa dell'auto che soddisfa
#   i criteri appena descritti. Se ci fossero piu' auto a pari merito,
#   sceglietene una come meglio preferite.
def piuGuidata(ds):
    # Implementate qua sotto il codice della funzione. La riga con il pass puo' essere cancellata.
    diz = {}
    diz_t = {}
    for tu in ds:
        (idGuidatore, targa, litri, km) = tu
        if idGuidatore not in diz_t:
            diz_t[idGuidatore] = 1
        else:
            diz_t[idGuidatore] += 1

        if idGuidatore not in diz:
            diz[idGuidatore] = targa

    di = {}
    for idGuidatore in diz_t:
        if diz_t[idGuidatore] >= 4:
            targa = diz[idGuidatore]
            if targa not in di:
                di[targa] = 1
            else:
                di[targa] += 1

    max = 0
    maxTag = ''
    for targa in di:
        if di[targa] > max:
            max = di[targa]
            maxTag = targa

    return maxTag


##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################
print('-'*30)
print('Esercizio %s.' % (nomeEsercizio))
print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione caricaDatiFlotta: ')
csvfn = 'consumiFlotta.csv'
dflo = caricaDatiFlotta(csvfn)
print(dflo)

print('2) Eseguo la funzione trovaPiedePesante: ')
res2 = trovaPiedePesante(dflo)
print(res2)

print('3) Eseguo la funzione trovaAuto: ')
res3 = trovaAuto(dflo)
print(res3)

print("4) Eseguo la funzione piuGuidata:  ")
res4 = piuGuidata(dflo)
print(res4)

print('Nome file e autore dello script eseguito')
print('Autore: %s, %s' % (nome, cognome))
print('-'*30)
