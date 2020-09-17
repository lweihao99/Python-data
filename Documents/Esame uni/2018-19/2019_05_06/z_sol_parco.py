# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe
from __future__ import print_function

nomeEsercizio = 'parcoGiochi'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituito da una delle funzioni seguenti,
# La vera struttura dati caricata dal file sara' più lunga,
# i primi elementi delle due strutture dati non è detto che coincidano.

datiLetti = [('abbonamento', 25, 17.0), ('entrata', 23, '14/1/2018'),
('entrata', 23, '12/1/2018'), ('entrata', 7, '15/1/2018'), ('entrata', 7, '10/1/2018'), ('entrata', 7, '22/1/2018'), ('entrata', 15, '23/1/2018'), ('entrata', 3, '3/1/2018'), ('entrata', 17, '24/1/2018'), ('entrata', 27, '19/1/2018'), ('entrata', 27, '23/1/2018'), ('entrata', 27, '29/1/2018'), ('entrata', 9, '7/1/2018'), ('entrata', 43, '30/1/2018'), ('entrata', 43, '29/1/2018'), ('entrata', 43, '9/1/2018'), ('entrata', 43, '14/1/2018'), ('entrata', 43, '19/1/2018'), ('entrata', 25, '20/1/2018'), ('entrata', 25, '21/1/2018'), ('entrata', 25, '27/1/2018'), ('entrata', 39, '22/1/2018'), ('entrata', 39, '2/1/2018'), ('entrata', 39, '29/1/2018'), ('entrata', 39, '5/1/2018'), ('entrata', 39, '1/1/2018'), ('abbonamento', 15, 13.0), ('entrata', 37, '4/2/2018'), ('entrata', 37, '10/2/2018'), ('entrata', 37, '14/2/2018'), ('entrata', 37, '24/2/2018'), ('entrata', 2, '20/2/2018'), ('entrata', 2, '2/2/2018'), ('entrata', 2, '27/2/2018'), ('entrata', 2, '10/2/2018'), ('entrata', 2, '12/2/2018'), ('entrata', 8, '24/2/2018'), ('entrata', 8, '15/2/2018'), ('entrata', 47, '15/2/2018'), ('entrata', 47, '17/2/2018'), ('entrata', 47, '5/2/2018'), ('entrata', 16, '2/2/2018'), ('entrata', 17, '19/2/2018'), ('entrata', 17, '20/2/2018'), ('entrata', 17, '9/2/2018'), ('entrata', 17, '18/2/2018'), ('entrata', 41, '1/2/2018'), ('entrata', 41, '6/2/2018'), ('entrata', 41, '9/2/2018'), ('entrata', 1, '12/2/2018'), ('entrata', 1, '1/2/2018'), ('entrata', 1, '22/2/2018'), ('entrata', 15, '10/2/2018'), ('entrata', 15, '20/2/2018'), ('entrata', 31, '1/2/2018'), ('entrata', 31, '20/2/2018'), ('entrata', 31, '7/2/2018'), ('entrata', 31, '2/2/2018'), ('abbonamento', 20, 14.0)]

##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# 




##########################################################
# DESCRIZIONE DEL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede
# ogni funzione vi spiegherà cosa fare in dettaglio.
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


def leggiDatiIngressiParco(fn):
    #return datiLetti
    pass
    lOut = []
    with open(fn, 'r') as stream:
        stream.readline()
        stream.readline()
        for line in stream:
            tokens = line.strip().split(';')
            idUsr = tokens[0]
            if tokens[1] == 'sing':
                kind = 'entrata'
                for day in tokens[2:]:
                    lOut.append(( kind, int(idUsr), day))
            else:
                kind = 'abbonamento'
                lOut.append(( kind, int(idUsr), float(tokens[2])))
    return lOut



def costoGiornaliero(ds):
    # dizionario per convertire il giorno della settimana in tariffa
    g2t={0:10, 1:8, 2:6, 3:7, 4:11, 5:15, 6:16 } # la chiave 0 corrisponde a lunedi', 1 a martedi', ...
    pass # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    
    mese2giorni={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} # mese:giorni_nel_mese
    elems = ds.split('/')
    gg=int(elems[0])
    mm=int(elems[1])
    aa=int(elems[2])
    gpas = gg
    i=1
    while i<mm: # aggiungo i giorni dei mesi passati
        gpas += mese2giorni[i]
        i+=1
    #print(gpas)
    ggSet = (gpas - 1) %7 # gpas -1: numero di giorni trascorsi dal 1/1/2018 che e' il 1. giorno dell'anno e che e' lunedi'
    return g2t[ggSet]

def ottieniIncassi(ds):
    pass # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    abbonati={}
    singoli={}
    for tu in ds:
        if tu[0]=='abbonamento':
            idUser = tu[1]
            prezzo = tu[2]
            abbonati[idUser] = prezzo
        else:
            idUser=tu[1]
            giorno=tu[2]
            prezzoIngresso = costoGiornaliero(giorno)
            if idUser in singoli:
                singoli[idUser] += prezzoIngresso
            else:
                singoli[idUser] = prezzoIngresso
                
    toret={} # inizio a costruire la struttura dati da restituire
    for idUser in singoli:
        if idUser in abbonati: # se c'e' un abbonamento
            toret[idUser] = (abbonati[idUser], singoli[idUser])
        else:
            toret[idUser] = (singoli[idUser], singoli[idUser])
    return toret



def valutaImpattoAbbonamenti(ds):
    pass # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    dic = ottieniIncassi(ds)
    
    impatto=0
    for idUser in dic:
        (prezzoConAbbonamento, prezzoSingoli) = dic[idUser]
        if (prezzoSingoli-prezzoConAbbonamento) >= prezzoConAbbonamento * 0.10:
            impatto +=  prezzoSingoli - prezzoConAbbonamento
    return impatto
            



##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################




print('Esercizio %s.' % (nomeEsercizio))

print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione leggiDatiIngressiParco: ')
nomeFile='accessiParco.csv'
dp = leggiDatiIngressiParco(nomeFile)
print(dp)

print('2a) Eseguo la funzione costoGiornaliero sul 5/1/2018: ')
cg = costoGiornaliero('5/1/2018')
print(cg)

print('2b) Eseguo la funzione costoGiornaliero sul 20/5/2018: ')
cg = costoGiornaliero('20/5/2018')
print(cg)


print("3) Eseguo la funzione ottieniIncassi: ")
ip = ottieniIncassi(dp)
print(ip)

print("4) Eseguo la funzione valutaImpattoAbbonamenti: ")
imp = valutaImpattoAbbonamenti(dp)
print(imp)

print('Nome e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))


