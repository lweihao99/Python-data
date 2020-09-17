# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'Riserva01'

##########################################################
# INTRODUZIONE
##########################################################
#
# I file descritti qua di seguito contengono informazioni sui movimenti
# di una popolazione di orsi che vivono in un parco naturale. 
# Il rilevamento della posizione di un orso non e' continuo ma avviene solamente
# quando l'orso passa vicino a certi punti (chiamati postazioni di rilevazione).
##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e alcuni file di dati.
# I file con i dati sono:
#
# - File 1) distanze.csv
#   Il file memorizza le distanze tra le postazioni di rilevazione.
#   Una postazione di rilevazione e' identificata da una lettera
#   maiuscola dell'alfabeto.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
#
#        Postazione1;Postazione2;Distanza
#        A;B;211\r\n
#        A;C;470\r\n
#        A;D;275\r\n
#        A;E;229\r\n
#        A;F;290\r\n
#        A;G;299\r\n
#        A;H;348\r\n
#
#   La prima riga contiene l'intestazione delle colonne.
#   In tute le righe le informazioni sono separati da ; (punto e virgola) e
#   i \r\n rappresentano i caratteri di a capo.
#   Nell'esempio qua sopra, la prima riga di dati ci dice la
#   postazione A dista 211 metri dalla postazione B.
#   Nota bene: se nel file e' presente la distanza tra A e B (come
#   nell'esempio qua sopra), per risparmiare spazio non viene memorizzata
#   la distanza tra B ed A, visto che e' identica.
#
#
# - File 2) percorsi.csv
#   Questo file memorizza lo spostamento fatto dagli orsi
#   nelle giornate di osservazione.
#   Un esempio del contenuto del file e' il seguente.
#   Nella prima riga c'e' intestazione del file.
#   Nell'esempio non considerate il simbolo di # e gli spazi.
#
#      id_orso;data;Postazione1;Postazione2;...;PostazioneN\r\n
#      0;01/03/2010;J;Y;W\r\n
#      1;01/03/2010;U;Q\r\n
#      2;01/03/2010;V;A;J;Z;I;Q\r\n
#      ...
#
#   Ogni riga contiene informazioni sul percorso svolto da un orso in uno specifico giorno.
#   Per esempio, la prima riga di dati
#   0;01/03/2010;J;Y;W
#   ci dice che l'orso 0 il giorno 01/03/2010 ha svolto un percorso che e' passato per le
#   postazioni di rilevamento J, Y e W (nell'ordine con cui sono elencate).
#   Le postazioni di rilevamento sono identifiate con le
#   Lettere dell'alfabeto. I percorsi svolti dagli orsi possono toccare un
#   numero variabile di postazioni, per questo motivo il numero di postazioni toccate
#   puo' variare da una riga all'altra.


##########################################################
# DESCRIZIONE DEL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede
# ogni funzione vi spieghera' cosa fare in dettaglio.
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

cognome='Sostituiscimi con il cognome' # inserisci qua il tuo cognome
nome='Sostituiscimi con il nome' # inserisci qua il tuo nome


# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file contenente le distanze tra le postazioni.
#   La funzione deve restituire le informazioni sulle distanze tra postazioni,
#   sotto forma di un dizionario con la struttura descritta nell'esempio seguente:
#         {
#          'AB':518, 'BC':231,
#          ...
#         }
#   La prima coppia chiave valore nell'esempio qua sopra indica che la distanza tra
#   la postazione A e la postazione B e' di 518 metri, la seconda coppia chiave
#   valore indica che la distanza tra la postazione B e la postazione C e' 231 metri.
#   Si ricorda che ogni singola postazione e' contraddistinta da un'unica lettera dell'alfabeto.
#   Per maggiori informazioni sui dati coinvolti si faccia riferimento
#   alla descrizione del file contenente i dati.
#   Nell'esempio qua sopra le distanze devono essere valori interi, mentre la chiave 
#   deve essere una stringa formata dalle due postazioni coinvolte.
def leggiDistanzePostazioni(filename):
    pass  # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    dizDistanze = {}
    with open(filename, 'r') as stream:
        stream.readline()
        for line in stream:
            frammenti = line.strip().split(';')
            coppia = frammenti[0] + frammenti[1]
            dizDistanze[coppia] = int(frammenti[2])
    return dizDistanze



# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file con le informazioni sulle postazioni raggiunte
#   dagli orsi durante gli spostamenti.
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#              [ (id_orso, giorno, stringa_percorso), (id_orso, giorno, stringa_percorso), ...   ]
#   Per esempio, la funzione leggendo le seguenti righe del file (i \r\n sono stati omessi)
#        id_orso;data;Postazione1;Postazione2;...
#        0;01/03/2010;J;Y;W
#        2;01/03/2010;V;A;J;Z;I;Q
#        ...
#   dovrebbe restituire la seguente struttura dati:
#        [ (0,'01/03/2010', 'JYW'),  (2,'01/03/2010', 'VAJZIQ'), ... ]
#   Ogni elemento della lista e' una tupla che contiene, l'id dell'orso, la data in cui l'orso
#   ha svolto il suo percorso e una stringa formata dalle lettere delle Postazioni toccate dall'orso.
def caricaPercorsi(fname):
    pass  # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    lSpots = []
    with open(fname, 'r') as stream:
        stream.readline()
        for line in stream:
            frammenti = line.strip().split(';')
            orso = int(frammenti[0])
            data = frammenti[1]
            percorso = ''
            for el in frammenti[2:]:
                percorso += el
            lSpots.append((orso, data, percorso))
    return lSpots

# - La funzione seguente accetta come parametri in ingresso
#   le strutture dati restituite rispettivamente dalle funzioni
#   leggiDistanzePostazioni() e caricaPercorsi().
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#        {id_orso1:totale_strada_percorsa1, id_orso2:totale_strada_percorsa2, ...}
#           ...
#   dove per ogni orso deve essere calcolato il totale dello spazio percorso sulla
#   base dei dati ricevuti in ingresso.

def calcolaLunghezzaCammini(distanze, percorsi):
    pass  # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    dizCamminiOrsi = {}
    for percorso in percorsi:
        strPercorso =  percorso[2]
        # print strPercorso
        orso = percorso[0]
        distanza = 0
        for i in range(len(percorso[2]) - 1):
            tappa = strPercorso[i:i+2]
            # print tappa
            if tappa in distanze:
                dTappa = distanze[tappa]
            else:
                dTappa = distanze[tappa[1]+tappa[0]]
            distanza += dTappa
            # print dTappa
        if orso not in dizCamminiOrsi:
            dizCamminiOrsi[orso] =  distanza
        else:
            dizCamminiOrsi[orso] +=  distanza
        # print distanza
    return dizCamminiOrsi

# - La funzione seguente classifica una distanza percorsa in scaglioni.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, dovete SOLO USARLA negli
#   esercizi seguenti.
def categoriaOrso(distanza):
    if distanza < 300:
        return 'Ammalato'
    elif distanza <500:
        return 'Pigro'
    elif distanza <1000:
        return 'Ok'
    else:
        return 'Iperattivo'

# - La funzione seguente accetta in ingresso la struttura dati restituita dalla funzione calcolaLunghezzaCammini().
#   La funzione deve classificare le distane totali percorse dagli orsi in scaglioni utilizzando la funzione dichiarata qua sopra.
#   La funzione deve restituire la seguente struttura dati
#   { 'Ammalato':[id_orso, metri_percorsi], 'Pigro':[id_orso, metri_percorsi], ...}
#   In cui per ogni categoria vengono riportati i dati dell'orso (appartenente alla categoria) che ha percorso piu' strada.
def individua(lunghezza):
    pass  # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    dizScaglioni = {'Ammalato': ['xxx', -1], 'Pigro': ['xxx', -1], 'Ok': ['xxx', -1], 'Iperattivo': ['xxx', -1]}
    for orso in lunghezza:
        distanza = lunghezza[orso]
        scaglione = categoriaOrso(distanza)
        if distanza >= dizScaglioni[scaglione][1]:
            dizScaglioni[scaglione] = [orso, distanza]
    return dizScaglioni



# - La funzione seguente accetta in ingresso la struttura dati
#   restituita dalla funzione caricaPercorsi().
#   La funzione deve individuare l'id dell'orso che per primo arriva a visitare
#   tutte le stazioni A, B, C, D, E, F, G, H, I in un qualsiasi ordine.
#   Considerate i dati ottenuti dalla funzione caricaPercorsi()
#   come se fossero ordinati temporalmente.
def giramondo(percorsi):
    pass  # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    dizOrsiStazioni = {}
    i = 0
    lTargets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    vincitore = False
    for  percorso in percorsi:
        orso = percorso[0]
        stazioni = percorso[2]
        # print orso, stazioni
        if orso not in dizOrsiStazioni:
            dizOrsiStazioni[orso] = stazioni
        else:
            dizOrsiStazioni[orso] += stazioni
        points = 0
        for tgt in lTargets:
            if tgt in dizOrsiStazioni[orso]:
                points += 1
        if points >= len(lTargets):
            print(orso, dizOrsiStazioni[orso])
            return orso



##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))

print('Ciao %s, %s .' % (nome, cognome))

print("1) Eseguo la funzione leggiDistanzePostazioni: ")
fname1='distanze.csv'
dist = leggiDistanzePostazioni(fname1)
print(dist)

print('2) Eseguo la funzione caricaPercorsi: ')
fname2='percorsi.csv'
perc = caricaPercorsi(fname2)
print(perc)

print('3) Eseguo la funzione calcolaLunghezzaCammini: ')
lung = calcolaLunghezzaCammini(dist, perc)
print(lung)

print('4) Eseguo la funzione categoriaOrso: ')
categoria = categoriaOrso(5500)
print(categoria)

print('Eseguo la funzione individua: ')
ris = individua(lung)
print(ris)

print('5) Eseguo la funzione giramondo: ')
ris = giramondo(perc)
print(ris)


print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.


### cancellami
# fai check con (nelle prime 2 righe del file) from __future__ import print_function

# sep=';'
# newLine='\r\n'
# import random
#
# caratteri=[str(unichr(i)) for i in range(65,90+1)] # da A a Z
#
# def int2data(giorniDaInizio, annoInizio=2010, separator='/'):
#         prog = giorniDaInizio % 365
#         anno = giorniDaInizio // 365 + annoInizio
#         #print(prog)
#         assert 0 <= prog <= 365
#         lungm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         mese = 1
#         giorni = prog
#         while giorni > lungm[mese - 1]:
#             giorni -= lungm[mese - 1]
#             mese += 1
#         st = '%2d/%2d/%4d' % (giorni, mese, anno)
#         st = st.replace(' ', '0')
#         st = st.replace('/',separator)
#         return st
#
# def generaDistanze():
#     f=open('distanze.csv','w')
#     intestazione="Postazione1,Postazione2,Distanza".split(',')
#     f.write(sep.join(intestazione)+newLine)
#     #caratteri= ... spostato su
#     #print(caratteri)
#     for ii,pos1 in enumerate(caratteri[:-1]):
#         for jj in range(ii+1,len(caratteri)):
#             pos2=caratteri[jj]
#             distanza = random.randint(100,500)
#             assert pos1<pos2
#             info=[pos1,pos2,str(distanza)]
#             #print(info)
#             f.write(sep.join(info)+newLine)
#     f.close()
#     print('Wrote distanze.csv')
#
# def generaSpostamenti():
#     f=open('percorsi.csv','w')
#     intestazione='id_orso,data,Postazione1,Postazione2,...,PostazioneN'.split(',')
#     f.write(sep.join(intestazione)+newLine)
#     orsi=range(20)
#     for gg in range(60,100):
#         data=int2data(gg)
#         for orso_id in orsi:
#             percorso = random.sample(caratteri, random.randint(2,6))
#             line = [str(orso_id), data ] + percorso
#             print(line)
#             f.write(sep.join(line)+newLine)
#     f.close()
#     print('Wrote percorsi.csv')
#
#
# import random
# random.seed(10)

#generaDistanze()
#generaSpostamenti()
