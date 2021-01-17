# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'Bici02'

##########################################################
# INTRODUZIONE
##########################################################
#
# I file descritti qua di seguito contengono informazioni sull'utilizzo
# di biciclette che possono essere noleggiate dalle persone e lasciate
# in un qualsiasi punto della citta.
##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e alcuni file di dati.
# I file con i dati sono:
#
#
# - File 1) spostamenti.csv
#   Questo file memorizza le informazioni sulla strada percorsa
#   dalle biciclette durante l'erogazione del servizio.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
#
#       ID_Noleggio;ID_Bici;ID_Utente;Data;MetriPercorsi;TempoImpiegato(secondi)\r\n
#       0;39;69;26/04/2010;450;45\r\n
#       1;41;93;26/02/2010;4550;455\r\n
#       2;23;73;11/04/2010;1250;156\r\n
#       3;1;6;07/12/2010;1800;450\r\n
#       4;29;24;26/07/2010;1950;487\r\n
#
#   La prima riga contiene l'intestazione delle colonne.
#   In tute le righe le informazioni sono separati da ; (punto e virgola) e
#   i \r\n rappresentano i caratteri di a capo. Seguono alcune precisazioni
#   sulle informazioni contenute nel file.
#   Ogni riga del file contiene informazioni su un noleggio effettuato.
#   Le informazioni sono:
#   * ID_Noleggio identifica univocamente un noleggio effettuato da un cliente
#   * ID_Bici identifica la bici noleggiata
#   * ID_Utente identifica l'utente che ha usufruito della bici
#   * Data identifica la data in cui e' iniziato il noleggio
#   * MetriPercorsi indica i metri percorsi
#   * TempoImpiegato indicata il tempo del noleggio in secondi


#
# - File 2) danni.csv
#   Il file memorizza le informazioni sui danni subiti dalle biciclette.
#   Un esempio del contenuto del file e' il seguente.
#   Nella prima riga c'e' intestazione del file.
#   Nell'esempio non considerate il simbolo di # e gli spazi.
#       ID_Bici;ModelloBicicletta;TipoDanno1;TipoDanno2;...;TipoDannoN;CostoRiparazione1;CostoRiparazione2;...;CostoRiparazioneN\r\n
#       0;B;2;3;18;3;8;22\r\n
#       1;D;11;7;16;18;18;20;1;17\r\n
#       2;B;18;13;9;19;2;17\r\n
#       3;D;16;7;15;7\r\n
#       4;D;17;1;15;15\r\n
#       5;D;14;7\r\n
#
#   Ogni riga del file riporta informazioni su una singola bicicletta.
#   Per esempio la prima riga di dati fornisce le seguenti informazioni:
#   * la bicicletta ha ID_Bici 0,
#   * il ModelloBicicletta e' B,
#   * la bici ha subito 3 danni, rispettivamente TipoDanno pari a 2, 3 e 18,
#     questi danni sono costati rispettivamente 3, 8 e 22 euro.
#     I costi dei danni sono sempre numeri interi.
#     In altre parole, considerando i numeri dopo ModelloBicicletta, la prima meta'
#     sono gli identificatori che individuano la tipologia di danno, la seconda meta'
#     sono i corrispondenti costi di riparazione.
#
#
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

cognome = 'Sostituiscimi con il cognome'  # inserisci qua il tuo cognome
nome = 'Sostituiscimi con il nome'  # inserisci qua il tuo nome


# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file con le informazioni sui tragitti percorsi dagli utenti.
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#       [ (ID_Noleggio, ID_Bici, ID_Utente, data, metri_percorsi, tempo_impiegato),
#               ...
#       ]
#
#   Per esempio, la funzione leggendo le seguenti righe del file (i \r\n sono stati omessi)
#       ID_Noleggio;ID_Bici;ID_Utente;Data;MetriPercorsi;TempoImpiegato(secondi)\r\n
#       0;39;69;26/04/2010;450;45
#       1;41;93;26/02/2010;4550;455
#       2;23;73;11/04/2010;1250;156
#
#   dovrebbe restituire la seguente struttura dati:
#        [ (0, 39, 69, '26/04/2010', 450, 45),
#          (1, 41, 93, '26/02/2010', 4550, 455),
#          (2, 23, 73, '11/04/2010', 1250, 156)
#        ]
def caricaSpostamenti(fname):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    f = open(fname, 'r')
    li = []
    f.readline()  # salto l'intestazione
    for line in f:
        line = line.strip('\r\n').split(';')
        idnoleggio = int(line[0])
        idbici = int(line[1])
        idutente = int(line[2])
        data = line[3]
        metri = int(line[4])
        tempo = int(line[5])
        li.append((idnoleggio, idbici, idutente, data, metri, tempo))
    return li


# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file contenente i dati sui danneggiamenti delle biciclette.
#   La funzione deve restituire le informazioni sulle biciclette,
#   sotto forma di un dizionario con la struttura descritta nell'esempio seguente:
#         {
#          id_bici1:(modello_bici1, totale_costi_riparazione_bici1),
#          id_bici2:(modello_bici2, totale_costi_riparazione_bici2),
#          ...,
#          id_biciN:(modello_biciN, totale_costi_riparazione_biciN)
#         }
#
#   Dove totale_costi_riparazione_bici... e' il totale della somma spesa
#   per le riparazioni di una singola bicicletta.
#   Per maggiori informazioni sui dati si faccia riferimento
#   alla descrizione del file contenente i dati.
#
#   Vi suggeriamo di implementare anche una funzione accessoria
#   che riceva come parametro in ingresso la stringa (oppure una lista di elementi)
#   corrispondenti ad una riga del file. La funzione accessoria dovrebbe
#   calcolare il totale dei costi di riparazione presenti in una riga.
#   Esempio di funzione accessoria: # se volete potete togliere i commenti qua sotto
#
# def calcolaTotaleCosti(...):
#    pass

# ****** Da rimuovere dal testo del compito
def calcolaTotaleCosti(li):
    posDanni = 2
    posCosti = (len(li) - posDanni)//2 + posDanni
    i = 0
    sommaCosti = 0
    while i+posDanni < posCosti:
        tipoDanno = li[posDanni+i]
        sommaCosti += int(li[posCosti+i])
        i += 1
    return sommaCosti
# l'intestazione seguente deve invece rimanere nel testo del compito


def caricaDatiBici(filename):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    diz = {}
    f = open(filename, 'r')
    diz = {}

    f.readline()  # salto l'intestazione
    for line in f:
        line = line.strip('\r\n').split(';')
        idbici = int(line[0])
        modello = line[1]
        sommaCosti = calcolaTotaleCosti(line)
        diz[idbici] = (modello, sommaCosti)
    return diz


# - La funzione seguente calcola la tariffa per un noleggio,
#   sulla base dei metri percorsi e dei minuti di utilizzo della bicicletta.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, dovete SOLO USARLA negli
#   esercizi seguenti.
def tariffazione(metri, secondi):  # NB: nel testo originale il parametro secondi era stato erroneamente chiamato minuti. Nella correzione sono state considerate valide entrambe le possibilita' (valore passato in minuti, valore passato in secondi)
    imp = metri/1000.0*0.20 + secondi/60.0*0.10
    if imp < 0.5:
        return 0.0
    else:
        return imp

# - La funzione seguente accetta come parametro in ingresso la struttura
#   dati restituita dalla funzione caricaSpostamenti()
#   La funzione deve restituire una struttura dati come la seguente:
#       { id_bicicletta1:totale_noleggi1,  id_bicicletta2:totale_noleggi2, ...}
#   dove per esempio totale_noleggi1 e' il totale dei soldi che la bicicletta1
#    ha fatto guadagnare con i noleggi.


def calcolaAddebiti(spost):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    diz = {}
    for el in spost:
        idbici = el[1]
        metri = el[4]
        secondi = el[5]
        costo = tariffazione(metri, secondi)
        if idbici in diz:
            diz[idbici] += costo
        else:
            diz[idbici] = costo
    return diz


# - La funzione seguente accetta come parametri in ingresso:
#   * spost: la struttura dati restituita dalla funzione caricaSpostamenti()
#   * danni: la struttura dati restituita dalla funzione caricaDatiBici().
#   La funzione deve restituire una struttura dati come nell'esempio seguente:
#   { ModelloBicicletta1:rapporto1, ModelloBicicletta2:rapporto2, ...
#       ModelloBiciclettaN:rapportoN}
#   dove "rapporto..." e' il rapporto tra i soldi incassati con i noleggi della bici
#   appartenenti ad una certa categoria (identificata da ModelloBicicletta)
#   e i soldi spesi per riparazioni delle biciclette della categoria.
#   Nota bene1: il rapporto deve essere calcolato per modello di bicicletta,
#               non sulle singole biciclette.
#   Nota bene2: nel dato fornito, tutte le biciclette hanno avuto una spesa per danni.
def rapportoRedditivita(spost, danni):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    noleggi = calcolaAddebiti(spost)  # { id_bicicletta1:totale_noleggi1, ...}

    # danni  id_bici1:(modello_bici1, totale_costi_riparazione_bici1),

    diznum = {}
    dizden = {}

    for idbici in noleggi:
        importo = noleggi[idbici]
        mod = danni[idbici][0]

        if mod in diznum:
            diznum[mod] += importo
        else:
            diznum[mod] = importo

    for idbici in danni:
        mod = danni[idbici][0]
        ripar = danni[idbici][1]

        if mod in dizden:
            dizden[mod] += ripar
        else:
            dizden[mod] = ripar

    diz = {}
    for idbici in diznum:
        diz[idbici] = diznum[idbici] / float(dizden[idbici])

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

print("1) Eseguo la funzione caricaSpostamenti: ")
fname1 = 'Documents/Esame uni/2017-18/2018_07_12/tr_b_bike/spostamenti.csv'
spost = caricaSpostamenti(fname1)
print(spost)

print('2) Eseguo la funzione caricaDatiBici: ')
fname2 = 'Documents/Esame uni/2017-18/2018_07_12/tr_b_bike/danni.csv'
danni = caricaDatiBici(fname2)
print(danni)

print('Eseguo la funzione tariffazione: ')
tar = tariffazione(3000, 25)
print(tar)

print('3) Eseguo la funzione calcolaAddebiti: ')
ad = calcolaAddebiti(spost)
print(ad)

print('4) Eseguo la funzione rapportoRedditivita: ')
rap = rapportoRedditivita(spost, danni)
print(rap)


print('Nome dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.

'''


### cancellami
# fai check con (nelle prime 2 righe del file) from __future__ import print_function

sep=';'
newLine='\r\n'
import random

nnoleggi=500
nbici=50
nutenti=100

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

def generaSpostamenti():
    fn='spostamenti.csv'
    f=open(fn,'w')
    header='ID_Noleggio,ID_Bici,ID_Utente,Data,MetriPercorsi,TempoImpiegato(secondi)'.split(',')
    f.write(sep.join(header)+newLine)
    liBici=[str(el) for el in range(nbici)]
    liUtenti=[str(el) for el in range(nutenti)]
    liDate= [int2data(el) for el in range(2,360)]
    liMetri=[str(el*50) for el in range(100)]
    liVel=[4, 6, 8, 10]
    elli=[liBici, liUtenti, liDate, liMetri, liVel]
    for ii in range(nnoleggi):
        li=[str(ii)] + [selectOne(li) for li in elli]
        li[-1] = str(int(int(li[-2]) / int(li[-1]))) # replacing velocity with time
        f.write(sep.join(li)+newLine)
    f.close()

def generaDanni():
    liBici=[str(el) for el in range(nbici)]
    liUtenti=[str(el) for el in range(nutenti)]
    liDate= [int2data(el) for el in range(2,360)]
    liTipiBici = [str(el) for el in 'ABCD']
    liImportiDanno=[str(el) for el in range(1,30) ]
    liTipiDanno=[str(el) for el in range(1,20) ]
    fn='danni.csv'
    header = 'ID_Bici;ModelloBicicletta;TipoDanno1;TipoDanno2;...;TipoDannoN;CostoRiparazione1;CostoRiparazione2;...;CostoRiparazioneN'.split(';')
    f=open(fn,'w')
    f.write(sep.join(header)+newLine)

    for ii in range(nbici):
        dli = [str(ii), selectOne(liTipiBici) ]
        ndanni=random.randint(1,4)
        for jj in range(ndanni):
            dli.append(selectOne(liTipiDanno))
            dli.append(selectOne(liImportiDanno))
        f.write(sep.join(dli)+newLine)
    f.close()


    

#generaSpostamenti()
#generaDanni()
    
'''
