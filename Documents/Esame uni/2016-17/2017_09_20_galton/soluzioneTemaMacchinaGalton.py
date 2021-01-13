#!/usr/bin/env ipython
# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'macchinaDiGalton'

# DESCRIZIONE DEL PROGRAMMA

# Il programma da implementare serve per simulare il funzionamento
# della macchina di Galton, un congegno meccanico utilizzato per la dimostrazione
# pratica del teorema del limite centrale e della distribuzione normale.
# La macchina, illustrata nel file Galton.pdf, è costitutita da una intercapedine verticale
# avente nella parte superiore un serbatoio ripieno di palline che escono per gravità
# attraverso un foro centrale. Le palline cadono su una griglia di chiodini ed urtandoli
# vengono spostate verso destra o sinistra in maniera casuale.
# Al termine della griglia (e degli urti), le palline vengono raccolte ed impilate
# in molteplici contenitori posti alla base della macchina.
# Se la numerosità delle palline ed il numero dei contenitori è sufficientemente
# grande si noterà che esse tendono a disporsi secondo una distribuzione approssimativamente
# "a campana".
# Il programma deve riprodurre il funzionamento della macchina attraverso la simulazione dello
# spostamento delle palline e il loro incasellamento nei contenitori. Inoltre, si richiede
# di illustrare lo stato finale della macchina stampando a video e scrivendo su file l'istogramma
# della distribuzione ottenuta da una esecuzione del programma medesimo.



##########################################################
# Inizio della parte da editare
##########################################################

# sostituisci i *** con le informazioni richieste
studenteNome = '***'  # sostituisci gli *** con il tuo nome
studenteCognome = '***'  # sostituisci gli *** con il tuo cognome
studenteMatricola = '***'  # sostituisci gli *** con la tua matricola


# DESCRIZIONE DEL LAVORO DA SVOLGERE

# importare la libreria per la generazione di numeri pseudo-casuali

import random as rnd

# inizializzare un dizionario, DIZSPOST, per gli spostamenti con chiavi
# 'S' per sinistra, 'D' per Destra e valori -1 ed +1 rispettivamente.
DIZSPOST = {'S': -1, 'D': +1}

# Inizializzare due variabili intere per il numero di palline (numero di lanci)
# e l'altezza (ovvero il numero massimo di spostamenti che la pallina può
# effettuare), pari a 50 e 5 rispettivamente.
intPalline = 50
intAltezza = 5



# Implementate le seguenti funzioni

# - evento(pDestra). La funzione accetta come unico parametro in ingresso un
# valore che indichi la probabilità che avvenga un evento/urto verso destra.
# La funzione simula un evento/urto e restituisce la stringa 'D' per destra o
# 'S' per sinistra  a seconda che la probabilità sia maggiore o uguale a pDestra
# oppure minore di tale valore.


def evento(pDestra):
    """Simula un evento/urto e restituisce destra 'D' o sinistra 'S'."""
    if (rnd.random() >= pDestra):
        return 'S'
    else:
        return 'D'

# - generaEsperimento(nPalline, nAltezza). La funzione accetta due parametri in
# ingresso: il numero di palline totali nel "serbatoio" della macchina di Galton
# e l'altezza (numero di eventi/urti )
# la funzione restituisce una lista di liste che descrive, per ogni pallina
# (una delle liste annidate), la sequenza degli spostamento rispetto alla
# posizione iniziale, come nell'esempio qui di seguito:
# [['D', 'D', 'D'], ['D', 'S', 'S'], ['S', 'D', 'D'], ['D', 'S', 'D']].
# Per il calcolo delle direzioni si utilizzi la funzione evento passando come
# parametro il valore 0.5 (è equiprobabile che la pallina sia deviata a
# D oppure a S).


def generaEsperimento(nPalline, nAltezza):
    """Genera l'esperimento per nPalline da altezza nAltezza."""
    lCadute = []
    for caduta in range(nPalline):
        lCaduta = []
        for i in range(nAltezza):
            lCaduta.append(evento(0.5))
        lCadute.append(lCaduta)
    #print lCadute
    return lCadute


# - spostamentoPallina(lista, nPassi). La funzione accetta due parametri in ingresso:
# la lista degli spostamenti (lista di 'S' oppure 'D') della pallina e
# il numero di passi, ovvero l'altezza o numero di eventi/urto di interesse
# per l'analisi (eventualmente anche minore dell'altezza massima della macchina).
# La funzione deve restituire il valore dello spostamento della pallina
# rispetto alla posizione iniziale.
# La funzione deve utilizzare il dizionario degli spostamenti DIZSPOST per
# calcolare il valore numerico dello spostamento in base alla sequenza di urti
# ed alla direzione di ogni singolo urto.

def spostamentoPallina(lista, nPassi):
    #print lista
    #print nPassi
    """Calcola lo spostamento rispetto alla posizione iniziale per nPassi."""
    spostamento = 0
    for passo in lista[:nPassi]:
        spostamento += DIZSPOST[passo]
    #print spostamento
    return spostamento


# -istogrammaCadute(lCadute, nStrato). La funzione accetta due parametri in ingresso:
# la lista annidata che tiene traccia degli spostamenti di ogni singola pallina
# ed il numero di strati di interesse per l'analisi delle tracce.
# La funzione restituisce un dizionario che ha per chiavi le entità dello
# spostamento (coordinate) e per valori la numerosità delle palline (valore intero)
# che hanno avuto tale spostamento, come nell'esempio seguente:
# {1: 5, 3: 1, 5: 1, -5: 1, -3: 1, -1: 1}


def istogrammaCadute(lCadute, nStrato):
    """Calcola l'istogramma del numero di palline per spostamento."""
    #print lCadute
    #print nStrato
    lSpostamenti = []
    for caduta in lCadute:
        lSpostamenti.append(spostamentoPallina(caduta, nStrato))
    dizIstogramma = {}
    for spostamento in lSpostamenti:
        if spostamento not in dizIstogramma:
            dizIstogramma[spostamento] = 1
        else:
            dizIstogramma[spostamento] += 1
    #print dizIstogramma
    return dizIstogramma

# -stampaIstogramma(dizIsto). La funzione accetta come unico parametro in
# ingresso il dizionario restituito dalla funzione istogrammaCadute e ha come
# scopo quello di stampare a video l'istogramma di frequenza delle palline
# cadute, come nell'esempio qui di seguito riportato:
# -5  ** 2
# -4
# -3  ********* 9
# -2
# -1  ************ 12
# 0
# 1   **************** 16
# 2
# 3   ******** 8
# 4
# 5   *** 3
# In particolare l'istogramma deve riportare dapprima il valore dello spostamento,
# quindi tanti "*" quante le palline che hanno avuto quello spostamento, ed
# infine il numero di palline in ogni barra.


def stampaIstogramma(dizIsto):
    """Stampa a video l'istogramma del numero di palline cadute."""
    lSpostamenti = dizIsto.keys()
    lSpostamenti = sorted(lSpostamenti)
    lPosizioni = range(lSpostamenti[0], lSpostamenti[-1] + 1, 1)
    for posizione in lPosizioni:
        if posizione in dizIsto:
            linea = str(posizione) + '\t' + '*' * dizIsto[posizione]
            linea += ' ' + str(dizIsto[posizione])
            print linea
        else:
            print str(posizione)

# -stampaIstogrammaVerticale(dizIsto). La funzione accetta come unico parametro
# in ingresso il dizionario restituito dalla funzione istogrammaCadute e ha
# come scopo quello di scrivere in un file di nome 'istogramma.txt' un istogramma
# che rappresenti attraverso colonne di '*' il numero di palline cadute in ogni
# "contenitore".
# A differenza della precedente funzione, nella presente l'istogramma deve avere
# un layout verticale come nell'esempio riportato qui sotto:
#       *
#       *
#       *
#       *
#     * *
#     * *
#     * *
#   * * *
#   * * * *
#   * * * *
#   * * * *
#   * * * *
#   * * * *
#   * * * * *
# * * * * * *
# * * * * * *


def stampaIstogrammaVerticale(dizIsto):
    """Scrive in un file l'istogramma del numero di palline cadute."""
    lSpostamenti = dizIsto.keys()
    lSpostamenti = sorted(lSpostamenti)
    lPosizioni = range(lSpostamenti[0], lSpostamenti[-1] + 1, 1)
    altMax = max(dizIsto.values())
    lRighe = range(0, altMax)
    fStream = open('istogramma.txt', mode='w')
    for riga in lRighe:
        for posizione in lPosizioni:
            if posizione in dizIsto and riga >= altMax - dizIsto[posizione]:
                fStream.write('*')
            else:
                fStream.write(' ')
        fStream.write('\n')
    fStream.close()

##########################################################
# Fine della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


lEsperimento = generaEsperimento(intPalline, intAltezza)
# print lEsperimento
isto = istogrammaCadute(lEsperimento, 10)
# print isto
stampaIstogramma(isto)
stampaIstogrammaVerticale(isto)
