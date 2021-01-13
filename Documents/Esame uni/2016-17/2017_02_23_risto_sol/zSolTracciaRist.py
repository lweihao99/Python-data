# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'ristoranti'

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
# - consumazioni.csv
#   Il file contiene informazioni sulle consumazioni fatte in un ristorante.
#   Un esempio del contenuto del file e':
#       Giorno;IdCliente;Prezzo in euro;Alimento/bevanda\r\n
#       1;14;9;Pasta Matriciana\r\n
#       1;14;8;Arrosto di vitello\r\n
#       ...\r\n
#   La prima riga contiene l'intestazione delle colonne. Ogni riga riporta le
#   informazioni seguenti.
#   * Giorno e' il giorno della settimana in cui e' stato servito il prodotto. I
#     giorni possono andare da 1 lunedi' a 7 domenica.
#   * IdCliente e' un numero che identifica univocamente un cliente
#   * Prezzo in euro e' il prezzo speso per la consumazione dell'alimento
#     o della bevanda indicata nella riga.
#   * Alimento/bevanda indica il nome dell'alimento o della bevanda. Il nome dello
#     stesso alimento non cambia nelle diverse righe
#   Ogni riga del file riporta informazioni su un alimento o bevanda acquistato da
#   un cliente.
#   Provate ad aprire il file con un editor di testi .State attenti, se aprite
#   il file con un foglio di calcolo (es. excel), alcune informazioni potrebbero  
#   essere visualizzate in maniera distorta rispetto al contenuto vero e proprio
#   del file.
#   Il \r\n rappresentano due caratteri di "a capo".
#   SUGGERIMENTO: NON aprite il file ne' con il notepad di windows ne' con excel.
#
#
#
#
# DESCRIZIONE DEL LAVORO DA SVOLGERE
#
# Implementate le seguenti funzioni, il commento che precede ogni funzione vi
# spieghera' cosa fare in dettaglio.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
#
# - caricaConsumazioni(fn). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati delle consumazioni effettuate
#   dai clienti nel ristorante.
#   Nota bene: il nome del file da aprire e' passato alla funzione
#   come parametro.
#   La funzione deve restituire una lista di tuple, dove ogni tupla contiene le
#   informazioni presenti in una riga del file. Non deve essere inserita la
#   riga contenente l'intestazione. Dalle stringhe devono essere rimossi
#   eventuali caratteri di a capo.
#   Giorno, identificatore del cliente e prezzo devono essere memorizzati come interi.
#   Pere esempio, applicando la funzione ad un file con il seguente contenuto
#   Giorno;IdCliente;Prezzo in euro;Alimento/bevanda\r\n
#   ...\r\n
#   1;14;9;Pasta al pesto\r\n
#   1;14;8;Arrosto di vitello\r\n
#   ...\r\n
#   la funzione dovrebbe restituire la seguente struttura dati
#   [..., (1,14,9,'Pasta al pesto'), (1,14,8,'Arrosto di vitello'), ...] 
#   Scrivete l'implementazione della funzione qua sotto.

def caricaConsumazioni(fn):
    f=open(fn, 'r')
    li=[]
    f.readline() # salto la prima riga
    for line in f:
        line=line.strip('\n').strip('\r')
        records=line.split(';')
        gg=int(records[0])
        idc=int(records[1])
        prezzo=int(records[2])
        alimento=records[3]
        li.append((gg, idc, prezzo, alimento))
    return li



# - miglioreIncasso(consumazioni). La funzione accetta come parametro
#   in ingresso la struttura dati restituita dalla funzione precedente.
#   La funzione deve individuare il nome dell'alimento/bevanda che ha
#   fatto incassare di piu' al ristorante.
#   La funzione deve restituire una lista formata dal nome
#   dell'alimento/bevanda e dal valore incassato.
#   Un esempio di possibile risultato potrebbe essere:
#   ['Pasta al pesto', 3245]. Nota bene: i valori qua a sinistra sono
#   solo degli esempi, non sono il risultato corretto.
#   Se ci fossero piu' prodotti con lo stesso valore di incasso massimo,
#   sceglietene uno con il criterio che preferite.

def miglioreIncasso(consumazioni):
    al2pr={}
    for el in consumazioni:
        #print(el)
        (gg, idc, prezzo, alimento) = el
        if alimento in al2pr:
            al2pr[alimento]+=prezzo
        else:
            al2pr[alimento]=prezzo
    maxinc=0
    maxalim=0
    for k in al2pr:
        v=al2pr[k]
        if v>maxinc:
            maxinc=v
            maxalim=k
    return [maxalim, maxinc]



# - spesaClientiSuDoppie(consumazioni). La funzione accetta come parametro
#   in ingresso la struttura dati restituita dalla funzione caricaConsumazioni.
#   La funzione deve individuare per ogni cliente il totale delle somme spese
#   considerando solo gli alimenti/bevande che soddisfano il criterio seguente:
#   l'alimento/bevanda deve avere almeno una lettera doppia nel nome. Una lettera
#   doppia sono due lettere identiche consecutive. Per esempio 'Risotto' soddisfa
#   il criterio (doppia t) mentre 'Lasagne' no. Non preoccupatevi delle maiuscole/minuscole.
#   Scrivete un algoritmo in grado di individuare i nomi con lettere doppie, non
#   costruite a mano un elenco di alimenti con le doppie, rischiate sicuramente di
#   dimenticare qualcosa.
#   La funzione deve restituire un dizionario di coppie chiave valore, dove la chiave
#   e' l'idcliente e il valore e' il totale degli incassi calcolato come descritto sopra.
#   Nota: nel caso vi sorgesse il dubbio, nei nomi degli alimenti non ci saranno mai due
#   spazi consecutivi.

def hadoppie(st):
    i=0
    while i<len(st)-1:
        if st[i]==st[i+1]:
            return True
        i+=1
    return False

def spesaClientiSuDoppie(consumazioni):
    cl2sp={}
    for el in consumazioni:
        #print(el)
        (gg, idc, prezzo, alimento) = el
        if hadoppie(alimento):
            if idc in cl2sp:
                cl2sp[idc]+=prezzo
            else:
                cl2sp[idc]=prezzo
    return cl2sp


# - giornoPreferito(consumazioni). La funzione accetta come parametro
#   in ingresso la struttura dati restituita dalla funzione caricaConsumazioni.
#   La funzione deve individuare per ogni cliente il giorno della settimana
#   in cui il cliente si e' recato al ristorante piu' spesso.
#   Se ci fossero piu' giorni a pari merito, sceglietene uno con  con il
#   criterio che preferite.
#   La funzione deve restituire un dizionario di coppie chiave valore, dove la chiave
#   e' l'idcliente e il valore e' l'intero corrispondente al giorno della settimana preferito.

def getMaxDay(li):
    maxday=-1
    maxvalue=-1
    for i in range(len(li)):
        if li[i]>maxvalue:
            maxvalue=li[i]
            maxday=i
    return maxday

def giornoPreferito(consumazioni):
    cl2gg={}
    for el in consumazioni:
        #print(el)
        (gg, idc, prezzo, alimento) = el
        if idc not in cl2gg:
            cl2gg[idc] = [0]*7 # lista di 7 elementi
        cl2gg[idc][gg]+=1
    di={}
    for k in cl2gg:
        li=cl2gg[k]
        di[k]=getMaxDay(li)
    return di
    



##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione. 
##########################################################


print('Esercizio %s.' % (nomeEsercizio))
print('Ciao (%s, %s, %s)' % (studenteNome, studenteCognome, studenteMatricola))
print('1) Eseguo la funzione caricaConsumazioni')
fn = 'consumazioni.csv'
cons = caricaConsumazioni(fn)
print('Risultato: ')
print(cons)

print('2) Eseguo la funzione miglioreIncasso: ')
mi=miglioreIncasso(cons)
print('Risultato: ')
print(mi)

print('3) Eseguo la funzione spesaClientiSuDoppie: ')
scsd = spesaClientiSuDoppie(cons)
print('Risultato: ')
print(scsd)

print('4) Eseguo la funzione giornoPreferito: ')
gp = giornoPreferito(cons)
print('Risultato: ')
print(gp)
