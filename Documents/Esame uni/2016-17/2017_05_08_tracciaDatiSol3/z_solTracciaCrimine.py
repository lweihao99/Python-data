# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'LocalizzazioneBande'

##########################################################
# Inizio della parte da editare
##########################################################

# sostituisci i *** con le informazioni richieste
studenteNome = '***'  # sostituisci gli *** con il tuo nome
studenteCognome = '***'  # sostituisci gli *** con il tuo cognome
studenteMatricola = '***'  # sostituisci gli *** con la tua matricola
#
# DESCRIZIONE DEL LAVORO DA SVOLGERE: vedi file di testo


def calcolaBaricentri(filename1):
    f1 = open(filename1, 'r')
    f1.readline()  # salto le prime 2 righe che non contengono informazioni
    f1.readline()
    sommax = {}
    sommay = {}
    somman = {}
    for line in f1:
        line = line.strip('\n')
        record = line.split(';')
        x = int(record[0])
        y = int(record[1])
        banda = record[2]
        nvolte = int(record[3])
        if banda in somman:
            sommax[banda] += x * nvolte
            sommay[banda] += y * nvolte
            somman[banda] += nvolte
        else:
            sommax[banda] = x * nvolte
            sommay[banda] = y * nvolte
            somman[banda] = nvolte
    diz2ret = {}
    for banda in somman:  # avrei potuto anche scegliere sommax o sommay
        barx = int(sommax[banda] / somman[banda])
        bary = int(sommay[banda] / somman[banda])
        diz2ret[banda] = (barx, bary)
    f1.close()
    return diz2ret


def distanza(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


# city2coord={'CHICAGO':(3000,1600), ...}
def cittaPiuVicina(x1, y1, city2coord):
    tempMinDist = 10000000  # cosi' alla prima iterazione sara' sicuramente modificato
    tempCittaPiuVicina = ''  # alla prima iterazione sara' comunque modificata
    for citta in city2coord:
        vals = city2coord[citta]
        xcitta = vals[0]
        ycitta = vals[1]
        d = distanza(x1, y1, xcitta, ycitta)
        if d < tempMinDist:
            tempCittaPiuVicina = citta
            tempMinDist = d
    return tempCittaPiuVicina


def caricaCitta2coord(fn):
    f = open(fn, 'r')
    f.readline()
    f.readline()
    city2coord = {}
    for line in f:
        line = line.strip('\n')
        record = line.split(';')
        city = record[0]
        x = int(record[1])
        y = int(record[2])
        city2coord[city] = (x, y)
    f.close()
    return city2coord


def cittaVicine(fileName2, dizbar):
    city2coord = caricaCitta2coord(fileName2)
    diz2ret = {}
    for banda in dizbar:
        baricx = dizbar[banda][0]
        baricy = dizbar[banda][1]
        citta = cittaPiuVicina(baricx, baricy, city2coord)
        diz2ret[banda] = citta
    return diz2ret


##########################################################
# Fine della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))
print('Ciao (%s, %s, %s)' % (studenteNome, studenteCognome, studenteMatricola))
print('Eseguo la funzione calcolaBaricentri')
fn1 = 'episodi.txt'
dib = calcolaBaricentri(fn1)
print('Risultato prima funzione: ')
print(dib)
fn2 = 'citta.txt'
print('Eseguo la funzione cittaVicine')
res = cittaVicine(fn2, dib)
print('Risultato seconda funzione: ')
print(res)
