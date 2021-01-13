# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'viaggiAutostradali'

##########################################################
# Inizio della parte da editare
##########################################################
# sostituisci i *** con le informazioni richieste
studenteNome = '***'  # sostituisci gli *** con il tuo nome
studenteCognome = '***'  # sostituisci gli *** con il tuo cognome
studenteMatricola = '***'  # sostituisci gli *** con la tua matricola
#
# DESCRIZIONE DEL LAVORO DA SVOLGERE: vedi file di testo


def creaDizCaselli(filename):
    fCaselli = open(filename, 'r')
    fileLines = fCaselli.readlines()
    fCaselli.close()
    del fileLines[:2]
    dizCas = {}
    for linea in fileLines:
        if linea[0] != '#':
            frammenti = linea.strip().split('\t')
            dizCas[frammenti[2]] = (frammenti[1], float(frammenti[0]))
    return dizCas


def caricaTariffe(filename):
    fTariffe = open(filename, 'r')
    fileLines = fTariffe.readlines()
    fTariffe.close()
    strTariffe = fileLines[3]
    tariffe = strTariffe.strip().split('\t')
    del tariffe[:2]
    strCategorie = fileLines[2]
    categorie = strCategorie.strip().split('\t')
    del categorie[0]
    dizTariffe = {}
    i = 0
    while i in range(len(tariffe)):
        dizTariffe[categorie[i]] = float(tariffe[i])
        i += 1
    return dizTariffe


def calcolaImporto(caselloIn, caselloOut, cat, dizTar, dizCas):
    distanza = abs(dizCas[caselloOut][1] - dizCas[caselloIn][1])
    return distanza * dizTar[cat]


def caricaViaggi(filename, dizCas, dizTar):
    fViaggi = open(filename, 'r')
    fileLines = fViaggi.readlines()
    fViaggi.close()
    del fileLines[0]
    dizV = {}
    for linea in fileLines:
        frammenti = linea.strip().split(':')
        targa = frammenti[1]
        categoria = frammenti[2]
        casello = frammenti[3]
        if targa not in dizV:
            dizV[targa] = [casello, None, 0.0]
        else:
            dizV[targa][1] = casello
            importo = calcolaImporto(dizV[targa][0], dizV[targa][1],
                                     categoria, dizTar, dizCas)
            dizV[targa][2] = importo
    return dizV


def calcolaImporti(fileCaselli, fileViaggi, fileTariffe):
    dizCaselli = creaDizCaselli(fileCaselli)
    dizTariffe = caricaTariffe(fileTariffe)
    dizViaggi = caricaViaggi(fileViaggi, dizCaselli, dizTariffe)
    return dizViaggi

##########################################################
# Fine della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))
print('Ciao (%s, %s, %s)' % (studenteNome, studenteCognome, studenteMatricola))
print('Eseguo la funzione calcolaImporti')
fn1 = 'autostradaA1.tsv'
fn2 = 'viaggi.csv'
fn3 = 'costoKm.txt'
diz1 = creaDizCaselli(fn1)
print('Risultato prima funzione: ')
print(diz1)
diz2 = caricaTariffe(fn3)
print('Risultato seconda funzione: ')
print(diz2)
diz3 = calcolaImporti(fn1, fn2, fn3)
print('Risultato terza funzione: ')
print(diz3)
