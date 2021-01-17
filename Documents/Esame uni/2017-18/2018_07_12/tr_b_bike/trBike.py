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
    file = open(fname, 'r')
    file.readline()
    li = []
    for line in file:
        line = line.strip('\n').strip('\r')
        content = line.split(';')
        id_nol = int(content[0])
        id_bici = int(content[1])
        id_utente = int(content[2])
        data = content[3]
        MPerc = int(content[4])
        tempoImpiegato = int(content[5])

        li.append((id_nol, id_bici, id_utente, data, MPerc, tempoImpiegato))
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
def calcolaTotaleCosti(fn):
    posDanni = 2
    posCosti = (len(fn)-posDanni)//2 + posDanni
    i = 0
    sommaCosti = 0
    while i+posDanni < posCosti:
        tipoDanno = fn[posDanni+i]
        sommaCosti += int(fn[posCosti+i])
        i += 1
    return sommaCosti


def caricaDatiBici(filename):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    file = open(filename, 'r')
    file.readline()
    di = {}
    for line in file:
        line = line.strip('\n').strip('\r')
        content = line.split(';')
        id_bici = int(content[0])
        modelloBici = content[1]
        totCostoRip = calcolaTotaleCosti(content)
        di[id_bici] = (modelloBici, totCostoRip)
    return di


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
    di = {}
    for tu in spost:
        id_bici = tu[1]
        metroPerc = tu[4]
        tempoImpiegato = tu[5]
        totNoleggio = tariffazione(metroPerc, tempoImpiegato)
        if id_bici in di:
            di[id_bici] += totNoleggio
        else:
            di[id_bici] = totNoleggio
    return di


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
    diz = {}
    dizIncassoNoleggio = {}
    dizDanni = {}

    incassoNoleggio = calcolaAddebiti(spost)

    for id_bici in incassoNoleggio:
        importo = incassoNoleggio[id_bici]
        modelloBici = danni[id_bici][0]

        if modelloBici in dizIncassoNoleggio:
            dizIncassoNoleggio[modelloBici] += importo

        else:
            dizIncassoNoleggio[modelloBici] = importo

    for id_bici in danni:
        modelloBici = danni[id_bici][0]
        costoRiparazione = danni[id_bici][1]

        if modelloBici in dizDanni:
            dizDanni[modelloBici] += costoRiparazione
        else:
            dizDanni[modelloBici] = costoRiparazione

    for modello in dizIncassoNoleggio:
        diz[modello] = dizIncassoNoleggio[modello]/float(dizDanni[modello])

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
