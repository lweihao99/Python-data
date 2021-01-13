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


# inizializzare un dizionario, DIZSPOST, per gli spostamenti con chiavi
# 'S' per sinistra, 'D' per Destra e valori -1 ed +1 rispettivamente.


# Inizializzare due variabili intere, intPalline e intAltezza, per il numero
# di palline (numero di lanci) e l'altezza (ovvero il numero massimo di
# spostamenti che la pallina può effettuare), pari a 50 e 5 rispettivamente.



# Implementate le seguenti funzioni

# - evento(pDestra). La funzione accetta come unico parametro in ingresso un
# valore che indichi la probabilità che avvenga un evento/urto verso destra.
# La funzione simula un evento/urto e restituisce la stringa 'D' per destra o
# 'S' per sinistra  a seconda che la probabilità sia maggiore o uguale a pDestra
# oppure minore di tale valore.


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



# - spostamentoPallina(lista, nPassi). La funzione accetta due parametri in ingresso:
# la lista degli spostamenti (lista di 'S' oppure 'D') della pallina e
# il numero di passi, ovvero l'altezza o numero di eventi/urto di interesse
# per l'analisi (eventualmente anche minore dell'altezza massima della macchina).
# La funzione deve restituire il valore dello spostamento della pallina
# rispetto alla posizione iniziale.
# La funzione deve utilizzare il dizionario degli spostamenti DIZSPOST per
# calcolare il valore numerico dello spostamento in base alla sequenza di urti
# ed alla direzione di ogni singolo urto.



# -istogrammaCadute(lCadute, nStrato). La funzione accetta due parametri in ingresso:
# la lista annidata che tiene traccia degli spostamenti di ogni singola pallina
# ed il numero di strati di interesse per l'analisi delle tracce.
# La funzione restituisce un dizionario che ha per chiavi le entità dello
# spostamento (coordinate) e per valori la numerosità delle palline (valore intero)
# che hanno avuto tale spostamento, come nell'esempio seguente:
# {1: 5, 3: 1, 5: 1, -5: 1, -3: 1, -1: 1}


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
