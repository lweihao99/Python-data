# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'verificaPassword'

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
# - listaUtentiMese.txt
#   Il file contiene le informazioni relative agli accreditamenti degli utenti
#   del mese per la gestione di un servizio web.
#   Di cisacun utente vengono registrate le informazioni relative all'indirizzo
#   mail, al momento in cui e' avvenuta la registrazione ed alla password
#   assegnata automaticamente dal sistema.
#   Ogni riga del file (una per utente) contiene le informazioni sopracitate,
#   separate da ';' e con la seguente codifica:
#       - idUtente costituito dall'inidirizzo mail cosi' composto:
#           nome.cognome@dominio.it
#       - tempoRegistrazione con codifica giorno:ora:minuto
#       - passwd rappresentata da una stringa di caratteri Ascii
#
# - asciiCodes.txt
#   Il file contiene le informazioni per la codifica dei caratteri nello
#   standard ascii.
#   Ciascuna riga contiene i seguenti campi:
#   - stringa descrizione
#   - valore intero di codifica del carattere corrispondente
#   - carattere associato al valore intero
#   - descrizione estesa del carattere
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
# - caricaUtenti(filename). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati descritto in precedenza.
#   La funzione dovra' restituire una lista di tuple, una tupla
#   corrisponde ai dati di una riga del file (quindi ai dati di un utente),
#   come nell'esempio seguente:
#   [('idUtente1', 'time1', 'pwd1'), ... ,('idUtenteN', 'timeN', 'pwdN')]
#   dove tutti gli elementi di una tupla sono stringhe. Si ricorda che idUtente
#   e' nome.cognome@dominio.it

def caricaUtenti(filename):
    pass  # Questa istruzione puo' essere eliminata. Ricordatevi di chiudere il file prima di restituire il risultato


# - loadAscii(filename). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati descritto in precedenza.
#   La funzione dovra' restituire due dizionari, uno per passare
#   da carattere a numero (codifica in ascii del carattere) ed uno
#   per passare da numero a carattere (decodifica del carattere).
#   Nei due dizionari dovranno essere presenti solo i codici che vanno dal
#   numero 33, che corrisponde a '!' al codice 126, che corrisponde a '~'.
#   I due dizionari avranno struttura:
#       - {int: '', ..., int: ''} per la decodifica
#       - {'': int, ..., '':int } per la codifica

def loadAscii(filename):
    pass  # Questa istruzione puo' essere eliminata. Ricordatevi di chiudere il file prima di restituire il risultato



# - verificaPassword(lUtenti, filename). La funzione accetta solo due
#   parametri in ingresso: la lista restituita dalla funzione caricaUtenti()
#   ed il nome del file da passare alla funzione loadAscii().
#   La funzione dovra' restituire un lista di tuple, una per ogni utente e
#   strutturata secondo lo schema ('idUtente', risposta), dove:
#       - idUtente è l'identificativo contenuto nella lista in ingresso
#       - risposta è un valore booleano
#   Il valore che assume la variabile risposta corrispondera' a vero se
#   se la password associata e' corretta e falso altrimenti.
#   Per determinare se la password e' corretta e' necessario estrarre
#   nome, cognome e dominio (.it escluso) dall'identificativo dell'utente, unirli in
#   un'unica stringa ed estarre solo i caratteri di posizione
#   pari (posizione 0 compresa), per formare la stringa S1.
#   Esempio da armidio.tronconi@onomastici.it viene prima estratto
#   'armidiotronconionomastici' e da questa si considerano solo le posizioni pari. 
#   Per i passaggi successivi e' necessario determinare il valore corrispondente alla
#   somma degli interi in gg:hh:mm che formano tempoRegistrazione, cioe' gg+hh+mm.   
#   Ai valori ottenuti convertendo ciascun carattere ASCII della stringa S1 in intero,
#   deve essere sommato il valore ottenuto da tempoRegistrazione.
#   Di ogni numero risultante occorre calcolare il resto della sua divisione intera per 93.
#   Nota bene: questa operazione deve essere svolta per ciascun carattere di S1.
#   Infine, ai valori cosi' ottenuti occorre aggiungere 33 e convertire il numero
#   nel corrispondente carattere della codifica ASCII.
#   Ad esempio, per l'utente armidio.tronconi@onomastici.it iscrittosi
#   il 26 alle 6 e 8 la password corretta è MYP[^Z[UZY_UU

def verificaPassword(lUts, filename):
    pass  # Questa istruzione puo' essere eliminata. Ricordatevi di chiudere il file prima di restituire il risultato

##########################################################
# Fine della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################

print('Esercizio %s.' % (nomeEsercizio))
print('Ciao (%s, %s, %s)' % (studenteNome, studenteCognome, studenteMatricola))
print('Eseguo la funzione caricaUtenti')
fn1 = 'listaUtentiMese.txt'
lUtentiMese = caricaUtenti(fn1)
print 'caricaUscite\n', lUtentiMese
fn2 = 'asciiCodes.txt'
#fromAscii, toAscii = loadAscii(fn2)
#print('Risultato funzione loadAscii: ')
#print(fromAscii)
#print(toAscii)
lUtVerifica = verificaPassword(lUtentiMese, fn2)
print('Risultato funzione verificaPassword: ')
print(lUtVerifica)

               

