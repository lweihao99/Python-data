# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'chiamate'

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
# Nel file .zip trovate i seguenti file, oltre a questo script:
#
# - File 1) telefonate.csv
#   Il file contiene informazioni sulle telefonate effettuate in un mese da
#   alcuni clienti di un operatore di telefonia cellulare
#   Un esempio dell'intestazione del file e':
#
#   Cod_Chiamante;Cod_Destinatario;Cod_Cella_Chiamante;Cod_Cella_Destinatario;GGI:HHI:MMI;GGF:HHF:MMF\r\n
#
#   La prima riga contiene l'intestazione delle colonne. Ogni riga riporta le
#   informazioni seguenti.
#   * Cod_Chiamante: un intero che identifica univocamente il
#     cliente che ha effettuato la chiamata
#   * Cod_Destinatario: un intero che identifica univocamente il
#     cliente che ha ricevuto la chiamata
#   * Cod_Cella_Chiamante: un intero che identifica l'area nella
#     quale si trova il cliente che ha effettuato la chiamata
#   * Cod_Cella_Destinatario: un intero che identifica l'area nella
#     quale si trova il cliente che ha ricevuto la chiamata
#   * GGI:HHI:MMI rappresentano rispettivamente il giorno, l'ora
#     e il minuto in cui e' iniziata la chiamata
#   * GGF:HHF:MMF rappresentano rispettivamente il giorno, l'ora
#     e il minuto in cui e' finita la chiamata
#     - sia GGI sia GGF contengono valore interi (compresi tra 1 e 31) che rappresentano il giorno del mese
#     - sia HHI sia HHF contengono valori interi (compresi tra 0 e 23) che rappresentano un'ora del giorno
#     - sia MMI sia MMF contengono valori interi (compresi tra 0 e 59) che rappresentano un minuto di un'ora
#   All'interno del file sono presenti righe che iniziano con il
#   carattere '#', inserite per indicare il malfunzionamento delle celle.
#   Il \r\n rappresentano due caratteri di "a capo".
#   Provate ad aprire il file con un editor di testi.
#   State attenti, se aprirete il file con Excel o con il
#   notepad di windows, alcune informazioni potrebbero essere
#   VISUALIZZATE in MANIERA DISTORTA rispetto al contenuto del file.
#
#
# - File 2) questo script con il codice che dovrete implementare, come descritto nelle righe qua sotto
#
# DESCRIZIONE DEL LAVORO DA SVOLGERE
#
# Implementate le seguenti funzioni, il commento che precede ogni funzione vi
# spieghera' cosa fare in dettaglio.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
#
# - ottieniDatiTelefonate(nomeFile). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati sulle telefonate effettuate.
#   Nota bene: il nome del file da aprire e' passato alla funzione
#   come parametro. La funzione dovra' restituire una lista formata da tuple,
#   dove ogni tupla contiene i seguenti dati (ogni tupla corrisponde ad una telefonata):
#   (Cod_Chiamante, Cod_Destinatario, Cod_Cella_Chiamante, Cod_Cella_Destinatario, Numeo_Minuti_Di_Conversazione ).
#   I minuti di conversazione si calcolano includendo anche il minuto di inizio
#   della conversazione, per esempio una telefonata iniziata alle
#   (GGI;HHI;MMI) 10;14;30 e terminata alle (GGF;HHF;MMF) 10;14;34
#   dura 5 minuti (34-30+1=5).
#   Nella tupla, i dati dovranno essere memorizzati sotto forma di valori interi.
#   Ci sono alcune righe del file che contengono dati sbagliati, nella lista restituita
#   non dovranno essere presenti le tuple corrispondenti alle righe con dati sbagliati.
#   Le righe che rispettano i criteri indicati qua di seguito sono da considerarsi corrette:
#   * Cod_Chiamante e Cod_Destinatario devono essere diversi (non sono ammesse
#     chiamate a se stessi)
#   * GGI, HHI, MMI devono appartenere ai rispettivi insiemi di valori come da
#     specifiche precedenti.
#   * L'inizio della chiamata non puo' essere successivo alla fine della chiamata.
#     - (GGI:HHI:MMI) 10:14:30 , (GGF:HHF:MMF) 10:14:34 # Questa va bene
#     - (GGI:HHI:MMI) 21:10:10 , (GGF:HHF:MMF) 21:10:10 # Questa va bene (la telefonata dura un minuto)
#     - (GGI:HHI:MMI) 30:20:40 , (GGF:HHF:MMF) 30:20:30 # Da eliminare
#   * Telefonate piu' lunghe di 10 ore sono da considerarsi errori
#   Per il calcolo dei minuti di conversazione, si suggerisce di trasformare
#   (data,ora,minuto) in un intero corrispondente al numero di minuti trascorsi
#   dall'inizio del mese.
#   Siete invitati a creare delle funzioni accessorie per svolgere le operazioni
#   che si ripetono piu' volte all'interno del codice.


def check(gg, hh, mm):
    if gg < 1 or gg > 31:
        return False
    if hh < 0 or hh > 23:
        return False
    if mm < 0 or mm > 59:
        return False
    return True  # se arriva qui, i controlli sono andati a buon fine


def tempoTrascorso(gg, hh, mm):
    return mm + hh * 60 + gg * 24 * 60


def ottieniDatiTelefonate(nomeFile):
    # (Cod_Chiamante, Cod_Destinatario, Cod_Cella_Chiamante, Cod_Cella_Destinatario, Numeo_Minuti_Di_Conversazione )
    data = []
    fi = open(nomeFile, 'r')
    fi.readline()  # salto la 1. riga
    for line in fi:
        if line[0]!='#':
            line = line.strip('\r\n')
            line = line.split(';')
            # Cod_Chiamante;Cod_Destinatario;Cod_Cella_Chiamante;Cod_Cella_Destinatario;GGI:HHI:MMI;GGF:HHF:MMF
            chiamante = int(line[0])
            destinatario = int(line[1])
            cellaChiamante = int(line[2])
            cellaDestinatario = int(line[3])
            timeInizio=line[4]
            timeFine=line[5]

            timeInizioLi=timeInizio.split(':')
            timeFineLi=timeFine.split(':')
            
            ggi = int(timeInizioLi[0])
            hhi = int(timeInizioLi[1])
            mmi = int(timeInizioLi[2])
            ggf = int(timeFineLi[0])
            hhf = int(timeFineLi[1])
            mmf = int(timeFineLi[2])
            
            inizio = tempoTrascorso(ggi, hhi, mmi)
            fine = tempoTrascorso(ggf, hhf, mmf)
            delta = fine - inizio
            if chiamante != destinatario and check(ggi, hhi, mmi) and check(ggf, hhf, mmf) and delta >= 0:
                durata = delta + 1  # il 1. minuto va conteggiato
                el = ( chiamante, destinatario, cellaChiamante, cellaDestinatario, durata )
                data.append(el)
    fi.close()
    return data


# - calcolaBollette(datiChiamate). La funzione accetta come parametro
#   in ingresso la struttura dati restituita dalla funzione precedente.
#   La funzione dovra' restituire un dizionario di coppie chiave volore
#   in cui la chiave e' il codice del cliente e il valore e' un float
#   corrispondente all'importo che il cliente deve pagare per le chiamate
#   effettuate nel mese. La tariffazione delle chiamate avviene sulla base
#   dei minuti di conversazione, un cliente paga 0.10 euro (10 centesimi di euro)
#   per ogni minuto di chiamata effettuata. Il cliente che riceve la chiamata
#   non paga niente.
#   Ogni cliente ha un bonus di 20 minuti gratuiti al mese, quindi il cliente
#   paghera' solamente per i minuti eccedenti il bonus.
#   Per esempio se il cliente 1 effettua chiamate per 55 minuti e il cliente 2
#   effettua chiamate per 15 minuti, il dizionario restituito dovra' contenere:
#   {1:3.5, 2:0}. Il cliente 1 ha 35 minuti eccedenti il bonus tariffati a 0.10
#   centesimi l'uno.
#   L'insieme dei clienti contenuti nel dizionario e' formato da quei clienti
#   che appaiono almeno una volta come chiamanti nella struttura dati fornita in
#   ingresso.

def calcolaBollette(datiChiamate):
    # [chiamante,destinatario, cellaChiamante, cellaDestinatario, durata]
    clienti2minuti = {}
    for el in datiChiamate:
        chiamante = el[0]
        durata = el[4]
        if chiamante in clienti2minuti:
            clienti2minuti[chiamante] += durata
        else:
            clienti2minuti[chiamante] = durata
    clienti2tariffa = {}
    for cliente in clienti2minuti:
        minuti = clienti2minuti[cliente]
        if minuti <= 20:
            clienti2tariffa[cliente] = 0
        else:
            clienti2tariffa[cliente] = (minuti - 20) * 0.10
    return clienti2tariffa


# - calcolaCelleCongestionate(datiChiamate).  La funzione accetta come parametro
#   in ingresso la struttura dati creata dalla funzione ottieniDatiTelefonate.
#   La funzione deve identificare le celle (cioe' le aree) che hanno un elevato
#   carico di telefonate.
#   Per far cio', dovete calcolare il numero medio di telefonate effettuate
#   nel mese per cella. Nel calcolo della media, considerate solo le telefonate
#   in partenza da una cella, non le chiamate ricevute.
#   Sono da considerarsi congestionate le celle nelle quali il numero di telefonate
#   effettuate e' maggiore alla media.
#   La funzione dovra' restituire una lista con i codici delle celle congestionate.

def calcolaCelleCongestionate(datiChiamate):
    # (chiamante,destinatario, cellaChiamante, cellaDestinatario, durata)
    celle2chiamate = {}
    for el in datiChiamate:
        cella = el[2]
        if cella in celle2chiamate:
            celle2chiamate[cella] += 1
        else:
            celle2chiamate[cella] = 1

    numChiamate = 0
    numCelle = 0
    for cella in celle2chiamate:
        n = celle2chiamate[cella]
        numChiamate += n
        numCelle += 1
    media = float(numChiamate) / numCelle
    congestionate = []
    for cella in celle2chiamate:
        n = celle2chiamate[cella]
        if n > media:
            congestionate.append(cella)
    return congestionate


##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))
print('Ciao (%s, %s, %s)' % (studenteNome, studenteCognome, studenteMatricola))
print('1) Eseguo la funzione ottieniDatiTelefonate')
fn1 = 'telefonate.csv'
litel = ottieniDatiTelefonate(fn1)
print('Risultato: ')
print(litel)

print('2) Eseguo la funzione calcolaBollette: ')
bollette = calcolaBollette(litel)
print('Risultato: ')
print(bollette)

print('3) Eseguo la funzione calcolaCelleCongestionate: ')
res = calcolaCelleCongestionate(litel)
print('Risultato: ')
print(res)
