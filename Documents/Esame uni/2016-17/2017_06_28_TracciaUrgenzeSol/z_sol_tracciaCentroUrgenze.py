# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'centroUrgenze'

##########################################################
# Inizio della parte da editare
##########################################################

# sostituisci i *** con le informazioni richieste
studenteNome = '***'  # sostituisci gli *** con il tuo nome
studenteCognome = '***'  # sostituisci gli *** con il tuo cognome
studenteMatricola = '***'  # sostituisci gli *** con la tua matricola
#
# DESCRIZIONE DEL FILE CON I DATI
#
# Nel file .zip trovate il seguente file, oltre a questo script:
#
# - logUscite.txt
#   Il file contiene le informazioni relative alle uscite del mese per i
#   mezzi di un centro di primo intervento per le urgenze.
#   Il centro ha a disposizione tre tipologie di mezzi: veicoli, velivoli ed
#   imbarcazioni.
#   Le tipologie dei mezzi sono riconoscibili tramite il carattere separatore 
#   dei campi ed hanno la seguente struttura:
#       per i 'veicoli', targa#TempoInizio#TempoFine#KmPercorsi
#       per i 'velivoli', sigla*TempoInizio*TempoFine
#       per le 'imbarcazioni', codice|TempoInizio|TempoFine
#   In tutti e tre i casi, i tempi di inizio e fine missione sono codificati 
#   dd:hh:mm dove dd rappresenta il giorno del mese, hh l'ora e mm il minuto.
#   Nel file le uscite dei mezzi sono ordinate per TempoInizio crescente.
#
#   State attenti, se aprirete il file con Excel o con il 
#   notepad di windows, alcune informazioni potrebbero essere 
#   VISUALIZZATE in MANIERA DISTORTA rispetto al contenuto del file.

# DESCRIZIONE DEL LAVORO DA SVOLGERE
#
# Implementate le seguenti funzioni, il commento che precede ogni funzione vi
# spieghera' cosa fare in dettaglio.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
#
# - caricaUscite(filename). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati descritto in precedenza.
#   La funzione dovra' restituire una dizionario formata da tre liste,
#   ogni lista contiene in una tupla i dati di una riga del file, come nell'esempio
#   seguente (l'esempio si estende su piu' righe):
#   {'veicoli': [('AA000ZZ', 20, 30, 100), ... ,('BB000ZZ', 25, 30, 10)],
#    'velivoli': [('IAAA', 22, 100), ... , ('IZZZ', 1000, 1500)],
#    'imbarcazioni': [('NAAA000', 40, 743), ..., ('NZZZ999', 990, 1272)]}
#   Le chiavi del dizionario devono esere quelle indicate nell'esempio precedente.
#   Ogni tupla dovra' contenere i seguenti elementi:
#   (identificativo, mmInizio, mmFine) per i velivoli e le imnarcazioni
#   (identificativo, mmInizio, mmFine, kmPercorsi) per i veicoli
#   dove:
#           identificativo è una stringa
#           mmInizio un intero che rappresenta i minuti trascorsi dall'inizio del mese
#           mmFine un intero che rappresenta i minuti trascorsi dall'inizio del mese
#           kmPercorsi un intero che rappresenta i kilometri percorsi dal mezzo
#

def orario2Minuti(dd, hh, mm):
    return dd * 1440 + hh * 60 + mm


def str2Minuti(strOr):
    toks = strOr.split(':')
    return orario2Minuti(int(toks[0]), int(toks[1]), int(toks[2]))


def caricaUscite(filename):
    stream = open(filename, 'r')
    logUscite = stream.readlines()
    lVeicoli = []
    lVeivoli = []
    lImbarcazioni = []
    nUscite = 0
    for line in logUscite:
        nUscite += 1
        line = line.strip()
        if '#' in line:
            tokLine = line.split('#')
            lVeicoli.append((tokLine[0],
                             str2Minuti(tokLine[1]),
                             str2Minuti(tokLine[2]),
                             int(tokLine[3]))
                            )
        elif '*' in line:
            tokLine = line.split('*')
            lVeivoli.append((tokLine[0],
                             str2Minuti(tokLine[1]),
                             str2Minuti(tokLine[2])))
        elif '|' in line:
            tokLine = line.split('|')
            lImbarcazioni.append((tokLine[0],
                                  str2Minuti(tokLine[1]),
                                  str2Minuti(tokLine[2])))
        else:
            print 'error'
    # print '\nveicoli:'
    # for el in lVeicoli:
    #     print el
    # print '\nvelivoli:'
    # for el in lVeivoli:
    #     print el
    # print '\nimbarcazioni:'
    # for el in lImbarcazioni:
    #     print el
    # print 'nUscite', nUscite
    # print 'veicoli', len(lVeicoli), 'velivoli', len(lVeivoli), 'imbarcazioni', len(lImbarcazioni)
    return {'veicoli': lVeicoli, 'velivoli': lVeivoli, 'imbarcazioni': lImbarcazioni}

# - trovaFlotta(struttDati).
#   La funzione accetta come unico parametro in ingresso la struttura dati restituita
#   dalla funzione precedente e vuole ricostruire l'elenco dei mezzi apparteneti alla flotta
#   del centro e che sono stati impiegati nel mese in analisi.
#   La funzione dovra' restituire una dizionario formata da tre liste.
#   Ogni lista contiene gli identificativi dei soli mezzi associati alla tipologia dichiarata
#    nella chiave, come nell'esempio seguente (l'esempio si estende su piu' righe):
#   {'veicoli': ['AA000ZZ', ... ,'BB000ZZ'],
#    'velivoli': ['IAAA', ... , 'IZZZ'],
#    'imbarcazioni': ['NAAA000', ..., 'NZZZ999']}
#   Le chiavi del dizionario devono esere quelle indicate nell'esempio precedente.
#

def trovaFlotta(struttDati):
    dizFlotta = {'veicoli': [], 'velivoli': [], 'imbarcazioni': []}
    for tupla in struttDati['veicoli']:
        if tupla[0] not in dizFlotta['veicoli']:
            dizFlotta['veicoli'].append(tupla[0])
    for tupla in struttDati['velivoli']:
        if tupla[0] not in dizFlotta['velivoli']:
            dizFlotta['velivoli'].append(tupla[0])
    for tupla in struttDati['imbarcazioni']:
        if tupla[0] not in dizFlotta['imbarcazioni']:
            dizFlotta['imbarcazioni'].append(tupla[0])
    return dizFlotta


# - eliminaUscErr(dizUscite, dizFlotta).
#   La funzione accetta due parametri in ingresso: la struttura dati associata alle uscite
#   e quella associata ai mezzi impiegati. La funzione vuole eliminare dalla struttura dati
#   associata alle uscite tutte le tuple che corrispondono ad uscite errate.
#   Per ciascun mezzo, è da considerarsi errata un uscita che ha valore di mmInizio successivo a
#   mmFine dell'ultima missione valida per quel mezzo (tra quelle svolte in precedenza).
#   Ad esempio se per il mezzo AA000ZZ l'ultima uscita corretta è ('AA000ZZ', 20, 30, 100),
#   la tupla ('AA000ZZ', 25, 60, 100) è da considerarsi errata in quanto non rappresenta la
#   successiva uscita, mentre la tupla ('AA000ZZ', 40, 120, 100) sarebbe ammissibile.
#   La funzione dovra' restituire una struttura dati identica a quella restituita dalla funzione
#   caricaUscite, ma contente le sole uscite ammissibili.
#   Si ricorda che nella struttura dati passata in ingresso le uscite dei mezzi sono ordinate per TempoInizio crescente.


def eliminaUscErr(dizUsc, dizFlo):
    # print 'veicoli', len(dizUsc['veicoli']), 'velivoli', len(dizUsc['veivoli']), 'imbarcazioni', len(dizUsc['imbarcazioni'])
    dizTimeMezzi = {}
    dizUsciteOut = {}
    for chiave in dizFlo.keys():
        for mezzo in dizFlo[chiave]:
            dizTimeMezzi[mezzo] = 0
    usciteTot = 0
    # print 'dizUsc'
    # for el in dizUsc:
    #     usciteTot += len(dizUsc[el])
    #     print el, len(dizUsc[el])
    # print "numero uscite", usciteTot
    for chiave in dizUsc.keys():
        # print chiave
        dizUsciteOut[chiave] = []
        for uscita in dizUsc[chiave]:
            # print 'Uscita:', uscita
            if uscita[1] > dizTimeMezzi[uscita[0]]:
                dizUsciteOut[chiave].append(uscita)
                dizTimeMezzi[uscita[0]] = uscita[2]
            # print 'dizTMEzzi', dizTimeMezzi, '\n'
            # print 'dizOut', dizUsciteOut, '\n\n\n'
    usciteTot = 0
    for el in dizUsciteOut:
        usciteTot += len(dizUsciteOut[el])
    print "numero uscite", usciteTot
    return dizUsciteOut


##########################################################
# Fine della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))
print('Ciao (%s, %s, %s)' % (studenteNome, studenteCognome, studenteMatricola))
print('Eseguo la funzione caricaUscite')
fn1 = 'logUscite.txt'
dizM = caricaUscite(fn1)
print('caricaUscite\n', dizM)
dizF = trovaFlotta(dizM)
print('Risultato funzione trovaFlotta: ')
print(dizF)
dizM = eliminaUscErr(dizM, dizF)
print('Risultato funzione eliminaMerrore: ')
print(dizM)
