# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'Review01'

##########################################################
# INTRODUZIONE
##########################################################
#
# I file descritti qua di seguito contengono informazioni sulle review (valutazioni)
# che i clienti di alcuni ristoranti hanno scritto sul servizio ricevuto.
##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e alcuni file di dati.
# I file con i dati sono:
#
#
# - File 1) fastfood.csv
#   Il file memorizza le informazioni sui locali oggetto delle valutazioni.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
#
#        ID_FastFood;NomeFastFood;Citta;MetriQuadrati\r\n
#        0;PiadineriaRivazzurra;Lecce;640\r\n
#        1;Caffe600;Roma;640\r\n
#        2;Caffe600;Firenze;480\r\n
#        3;Panzer8;Bari;80\r\n
#        4;Farinata;Milano;80\r\n
#
#   La prima riga contiene l'intestazione delle colonne.
#   In tute le righe le informazioni sono separati da ; (punto e virgola) e
#   i \r\n rappresentano i caratteri di a capo. Seguono alcune precisazioni sulle informazioni
#   contenute nel file.
#   - ID_FastFood e' un intero che identifica univocamente il locale
#   - NomeFastFood e' il nome del fast food. Nota bene: lo stesso nome puo'
#     essere usato da locali diversi, sia nella stessa citta' sia in citta' diverse.
#     E' l'ID_FastFood che permette di distinguere locali diversi che pero'
#     hanno lo stesso nome.
#   - Citta e' il luogo in cui il fast food e' situato
#   - MetriQuadrati rappresenta la superficie del fast food
#
#
# - File 2) valutazioni.csv
#   Questo file memorizza le valutazioni date dagli utenti al servizio
#   ricevuto nel fast food.
#   Un esempio del contenuto del file e' il seguente.
#   Nella prima riga c'e' intestazione del file.
#   Nell'esempio non considerate il simbolo di # e gli spazi.
#
#      ID_Valutazione;ID_FastFood;ID_Utente;Data;Valutazioni...\r\n
#      0;25;143;11/09/2010;Atmosfera;Parcheggio;4.5;0.5\r\n
#      1;12;179;28/02/2010;Parcheggio;1.0\r\n
#      2;8;216;26/09/2010;Cibo;Costi;AccessoDisabili;5.0;4.0;2.5\r\n
#      3;14;5;07/08/2010;Cibo;3.0\r\n
#
#   Ogni riga contiene la valutazione fatta da un utente su un fast food.
#   Per esempio, la prima riga di dati
#   0;25;143;11/09/2010;Atmosfera;Parcheggio;4.5;0.5
#   contiene una valutazione (ID_Valutazione pari a 0) sull'ID_FastFood 25,
#   fatta dall'ID_Utente 143 nel giorno 11/09/2010. L'utente ha valutato
#   solo 2 "aspetti", Atmosfera e Parcheggio con voti rispettivamente pari a 4.5 e 0.5.
#   Ogni valutazione puo' contenere un numero variabile di voti, ognuno dato ad un
#   "aspetto" diverso. Per esempio nella riga successiva (ID_Valutazione pari a 1) e'
#   stato valutato solamente il "Parcheggio". 
#   Gli "aspetti" valutabili sono: 'Parcheggio,AccessoDisabili,Atmosfera,Cibo,Costi'.
#   In ogni riga sono prima elencati gli "aspetti" valutati e poi i voti corrispondenti.
#   Ogni riga può contenere da 1 a 5 voti diversi.

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
#   ingresso il nome del file contenente l'elenco dei fast food.
#   La funzione deve restituire le informazioni sui fast food,
#   sotto forma di un dizionario con la struttura descritta nell'esempio seguente:
#         {
#          id_fast_food:[NomeFastFood, Citta, MetriQuadrati]
#          ...
#         }
#   
#   Per maggiori informazioni sui dati coinvolti si faccia riferimento
#   alla descrizione del file contenente i dati.
#   Nell'esempio qua sopra id_fast_food e MetriQuadrati devono essere valori interi
def leggiFastFood(filename):
    pass  # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    f=open(filename, 'r')
    di={}
    f.readline() # salto l'intestazione
    for line in f:
        line=line.strip('\r\n').split(';')
        (id_fast_food, nome, citta, mq) = line
        di[id_fast_food] = (nome, citta, int(mq))
    f.close()
    return di


# - La funzione seguente restituisce una lista contenente 
#   l'elenco degli aspetti valutati dagli utenti.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, dovete SOLO USARLA negli
#   esercizi seguenti.
def listaAspetti():
    return ['Parcheggio','AccessoDisabili','Atmosfera','Cibo','Costi']


# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file con le informazioni sulle valutazioni effettuate dagli utenti.
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#        [ (ID_Valutazione, ID_FastFood, ID_Utente, {aspetto1:voto1, aspetto2:voto2,... }),
#        ...
#        ]
#   Per esempio, la funzione leggendo le seguenti righe del file (i \r\n sono stati omessi)
#      ID_Valutazione;ID_FastFood;ID_Utente;Data;Valutazioni...
#      0;25;143;11/09/2010;Atmosfera;Parcheggio;4.5;0.5
#      1;12;179;28/02/2010;Parcheggio;1.0
#        ...
#   deve restituire la seguente struttura dati:
#        [ (0, 25, 143, {'Atmosfera'4.5, 'Parcheggio':0.5}),
#          (1, 12, 179, {'Parcheggio':1.0}),
#          ...
#        ]
#   Il dizionario contenuto in ogni tupla ha come chiavi gli aspetti valutati e come
#   valori i voti corrispondenti attribuiti dall'utente.
#   L'elenco dei possibili aspetti valutati e' quello restituito dalla funzione listaAspetti().
def leggiValutazioni(fname):
    pass  # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    f=open(fname,'r')
    f.readline() # salto l'intestazione
    li=[]
    for line in f:
        line=line.strip('\r\n').split(';')
        id_val=int(line[0])
        id_loc=int(line[1])
        id_ut=int(line[2])
        posInizialeAsp=4
        posInizialeVoti = int( (len(line) - posInizialeAsp)/2 + posInizialeAsp ) # In python2 l'int() non serve
        diz={}
        i=0
        while posInizialeAsp+i<posInizialeVoti:
            asp=line[posInizialeAsp+i]
            voto=float(line[posInizialeVoti+i])
            diz[asp]=voto
            i+=1
        li.append( (id_val, id_loc, id_ut, diz) )
    return li



# - La funzione seguente accetta come parametri in ingresso
#   * la struttura dati restituita dalla funzione leggiValutazioni()
#   * il nome di un "aspetto" oggetto di valutazione.
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#
#        {id_fast_food1:media_score1, id_fast_food2:media2, ...}
#
#   dove per ogni fast_food deve essere calcolato il punteggio medio ottenuto
#   rispetto all'aspetto passato come parametro.
#   Il parametro "aspetto" sara' una stringa con uno dei seguenti
#   valori (non occorre fare verifiche):
#   'Parcheggio', 'AccessoDisabili', 'Atmosfera', 'Cibo', 'Costi'
#   Se un fast food non riceve mai valutazioni sullo specifico aspetto,
#   allora non deve essere presente nella struttura dati restituita.

def valutazioneMediaAspetto(valutaz, aspetto):
    pass  # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    numdiz={}
    dendiz={}
    for el in valutaz:
        ffid=el[1]
        valdiz=el[3]
        if aspetto in valdiz:
            if ffid in numdiz:
                numdiz[ffid]+=valdiz[aspetto]
                dendiz[ffid]+=1
            else:
                numdiz[ffid]=valdiz[aspetto]
                dendiz[ffid]=1
    mediediz={}
    for k in numdiz:
        mediediz[k] = numdiz[k] / dendiz[k]
    return mediediz


# - La funzione seguente accetta come parametri in ingresso:
#   * valutaz: la struttura dati restituita dalla funzione leggiValutazioni()
#   * listaID_FastFood: una lista di id_fast_food, es. [0, 5, 6, 8, 12]
#   La funzione deve restituire una struttura dati come nell'esempio seguente:
#        { if_fast_food1:[media_aspetto_parcheggio, media_aspetto_accessodisabili,
#                         media_aspetto_atmosfera', media_aspetto_cibo, media_aspetto_costi],
#         ...}
#   Dove ogni chiave del dizionario restituita e' un id_fast_food,
#   ad ogni id_fast_food e' associata una lista con dentro le medie dei giudizi
#   dati dagli utenti ai diversi aspetti oggetto di valutazione. 
#   L'ordine dei valori nelle liste deve essere quello dell'esempio qua sopra,
#   ed e' lo stesso con cui gli "aspetti" sono elencati nella lista restituita
#   dalla funzione listaAspetti().
#   Si suggerisce di sfruttare la precedebte funzione valutazioneMediaAspetto()
#   nell'implementare questa funzione.
#   Decidete voi come gestire l'eventuale caso di un fast food non ha valutazioni
#   su un singolo aspetto.
#   Nel dizionario restituito, devono essere presenti solo i fast food
#   i cui ID sono stati passati nel parametro in ingresso listaID_FastFood.
def generaRapporto(valutaz, listaID_FastFood):
    pass  # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    elAspetti=listaAspetti()
    diz={}
    i=0
    while i<len(elAspetti):
        nomeAspetto=elAspetti[i]
        val =  valutazioneMediaAspetto(valutaz, nomeAspetto)
        for id in val:
            if id in listaID_FastFood:
                voto = val[id]
                if id not in diz:
                    diz[id] = [0.0, 0.0, 0.0, 0.0, 0.0]
                diz[id][i]=voto
        i+=1
    return diz



##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))

print('Ciao %s, %s .' % (nome, cognome))

print("1) Eseguo la funzione leggiFastFood: ")
fname1='fastfood.csv'
ffood = leggiFastFood(fname1)
print(ffood)

print('2) Eseguo la funzione leggiValutazioni: ')
fname2='valutazioni.csv'
valut = leggiValutazioni(fname2)
print(valut)

print('3) Eseguo la funzione valutazioneMediaAspetto: ')
vma = valutazioneMediaAspetto(valut, 'Cibo')
print(vma)

print('Eseguo la funzione listaAspetti: ')
ris = listaAspetti()
print(ris)

print('4) Eseguo la funzione generaRapporto: ')
ffli=[0, 5, 6,8,12]
rap = generaRapporto(valut, ffli)
print(rap)

print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.



'''

### cancellami
# fai check con (nelle prime 2 righe del file) from __future__ import print_function

sep=';'
newLine='\r\n'
import random

nlocali=50

def int2data(giorniDaInizio, annoInizio=2010, separator='/'):
         prog = giorniDaInizio % 365
         anno = giorniDaInizio // 365 + annoInizio
         #print(prog)
         assert 0 <= prog <= 365
         lungm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
         mese = 1
         giorni = prog
         while giorni > lungm[mese - 1]:
             giorni -= lungm[mese - 1]
             mese += 1
         st = '%2d/%2d/%4d' % (giorni, mese, anno)
         st = st.replace(' ', '0')
         st = st.replace('/',separator)
         return st

def selectOne(li):
    i = random.randint(0,len(li)-1)
    return li[i]

def generaFastFood():
    fn='fastfood.csv'
    f=open(fn,'w')
    header='ID_FastFood,NomeFastFood,Citta,MetriQuadrati'.split(',')
    f.write(sep.join(header)+newLine)
    liNome = ['PaninoSbagliato','McDavid','BurgherKilo','RossoPeperoncino','PiadineriaRivazzurra','Panzer8','BeerWurstel','Caffe600','Chianina','Farinata','VeganOrganic','ViveLaCrepe']
    liCitta='Milano,Roma,Bologna,Firenze,Varese,Como,Lecco,Bari,Catania,Lecce'.split(',')
    limq=[80,120,260,340,420,480,500,560,640]
    limq=[str(el) for el in limq]
    elli=[liNome, liCitta, limq]
    for ii in range(nlocali):
        li=[str(ii)] + [selectOne(li) for li in elli]
        f.write(sep.join(li)+newLine)
    f.close()

def generaValutazioni():
    nvalutazioni=500
    fn='valutazioni.csv'
    #aspettiLi = 'Prenotazione,Parcheggio,AccessoDisabili,AttesaIngresso,Atmosfera,Cibo,Personale,Costi'.split(',')
    
    aspettiLi = 'Parcheggio,AccessoDisabili,Atmosfera,Cibo,Costi'.split(',')

    header='ID_Valutazione,ID_FastFood,ID_Utente,Data,Valutazioni...'.split(',')
    f=open(fn,'w')
    f.write(sep.join(header)+newLine)

    localiLi=[str(el) for el in range(nlocali)]
    reviewerLi=[str(el) for el in range(300)]
    dataLi = [int2data(el) for el in range(2,360)]
    elli = [localiLi, reviewerLi, dataLi]

    votiLi=[str(num*.5) for num in range(11) ]
    
    for ii in range(nvalutazioni):
        dli=[str(ii)] + [selectOne(li) for li in elli]
        aspettiVotati = random.sample(aspettiLi, random.randint(1,3))
        voti = [selectOne(votiLi) for _ in range(len(aspettiVotati))]
        f.write(sep.join(dli+aspettiVotati+voti)+newLine)
    f.close()

#generaFastFood()
#generaValutazioni()
    
'''
