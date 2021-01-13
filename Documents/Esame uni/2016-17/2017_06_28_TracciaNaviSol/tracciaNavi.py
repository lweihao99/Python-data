# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'navi'

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
# - File 1) caricoscarico.csv
#   Una nave  viaggia da un porto ad un altro, ogni volta che approda
#   in un porto carica acqua e cibo. Le informazioni sulle provviste
#   caricate nei porti e sul cibo consumato giornalmente dall'equipaggio
#   sono contenute nel file caricoscarico.csv. Ogni riga del file puo'
#   contenere
#   (1) le informazioni su cibo e acqua caricate in un porto
#       con la seguente struttura
#       gg/mm/aa*porto*kg_cibo_caricato*litri_acqua_caricata\r\n
#   (2) i dati su quanto consumato giornalmente dall'equipaggio
#       con la seguente struttura
#       nome_persona_equipaggio:data:kg_cibo_consumato:litri_acqua_bevuta\r\n
#   Nel file .csv le righe sono tra loro mischiate. Ogni riga (escluse le prime due
#   righe del file che contengono le intestazioni) può ospitare solo
#   una e una sola delle due strutture dati appena introdotte. Potete usare il separatore
#   dei campi per capire che tipo di struttura dati ospita una riga.
#   Le prime due righe contengono l'intestazione del file.
#   I pesi sono espressi in kilogrammi, i liquidi sono misurati in litri.
#   I \r\n rappresentano due caratteri di "a capo".
#   Il file inizia con il caricamento di cibo e acqua nel porto di partenza e
#   termina con il caricamento di 0,0 kg di cibo e 0.0 litri di acqua nel porto
#   di fine viaggio.
#   Provate ad aprire il file con un editor di testi.
#   State attenti, se aprirete il file con Excel o con il 
#   notepad di windows, alcune informazioni potrebbero essere 
#   VISUALIZZATE in MANIERA DISTORTA rispetto al contenuto del file.
#

# DESCRIZIONE DEL LAVORO DA SVOLGERE
#
# Implementate le seguenti funzioni, il commento che precede ogni funzione vi
# spieghera' cosa fare in dettaglio.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
#
# - caricaDatiProvviste(nomeFile). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati descritto in precedenza.
#   La funzione dovra' restituire una lista formata da tuple,
#   dove ogni tupla contiene i dati di una riga del file, come nell'esempio
#   seguente (l'esempio si estende su piu' righe):
#   [  (tipo_tupla, giorno, mese, anno, porto, kg_cibo_caricato, litri_acqua_caricata),
#      (tipo_tupla, giorno, mese, anno, nome_persona_equipaggio, kg_cibo_consumato, litri_acqua_bevuta),
#      (tipo_tupla, giorno, mese, anno, nome_persona_equipaggio, kg_cibo_consumato, litri_acqua_bevuta),
#      ...
#   ]
#   Dove tipo_tupla assume il valore intero 1 se la tupla contiene dati sul cibo e acqua
#   caricati in porto, mentre assume il valore intero 2 se la tupla contiene dati su 
#   cibo e acqua consumati dall'equipaggio.
#   Nelle tuple,
#   giorno, mese e anno devono assumere valori interi,
#   mentre kg_cibo_caricato, litri_acqua_caricata, kg_cibo_consumato e litri_acqua_bevuta
#   devono assumere valori float.
#   Se volete potete implementare delle funzioni aggiuntive. Potete
#   utilizzare lo spazio qua sotto

def caricaDatiProvviste(nomeFile):
    pass # Questa istruzione puo' essere eliminata. Ricordatevi di chiudere il file prima di restituire il risultato



    
# - calcolaCostiProvviste(...). La funzione accetta come parametro
#   in ingresso la struttura dati restituita dalla funzione precedente.
#   La funzione deve calcolare e restituire il costo totale pagato per
#   il cibo e l'acqua caricata nei porti, tenendo conto che:
#   Nei porti di 'VENEZIA','ANCONA' e 'MESSINA'  si applicano le seguenti tarffe:
#   * Costo cibo: 10 euro al kg
#   * Costo acqua: 1 euro al kg
#   Nei porti di 'DANZICA','RIGA' e 'TALLIN' si applicano le seguenti tarffe:
#   * Costo cibo: 15 euro al kg
#   * Costo acqua: 0.5 euro al kg
#   In tutti gli altri porti si applicano le seguenti tariffe:
#   * Costo cibo: 12 euro al kg
#   * Costo acqua: 0.7 euro al kg
# La funzione deve restituire un valore float contenente il costo totale che la
# barca ha pagato per comprare acqua e cibo in tutti i porti in cui e' entrata.
def calcolaCostiProvviste(dati):
    pass # Questa istruzione puo' essere eliminata.

                
                

# - calcolaSprechi(...).  La funzione accetta come parametro
#   in ingresso la struttura dati restituita dalla funzione caricaDatiProvviste.
#   In ogni porto, la nave scarica il cibo e l'acqua avanzati dal carico
#   precedente, prima di procedere a caricare il nuovo cibo e la nuova acqua.
#   Se gli acquisti fossero svolti in maniera attenta, la quantita' acquistata
#   dovrebbe essere pari alla quantita' consumata aumentata di un 20% come
#   margine di sicurezza (la navigazione tra un porto e l'altro potrebbe subire
#   dei giorni di ritardo, incrementando il numero dei pasti e quindi dei consumi
#   effettuati dall'equipaggio).
#   Viene considerato spreco la differenza tra la quantita' caricata in un porto
#   e il 120% della quantita' consumata nel viaggio fino al porto successivo (Il
#   120% e' la quantita' consumata aumentata del 20%).
#   Si ricorda che nel file .csv le righe sui consumi seguono sempre la riga del
#   corrispondente rifornimento in porto. I rifornimenti avanzati vengono sempre
#   scaricati appena prima di caricare i nuovi rifornimenti.
#   La funzione deve calcolare gli sprechi compiuti dalla nave durante il viaggio
#   e restituire una lista come la seguente:
#   [kg_sprecati, litri_sprecati]
#   Si sottolinea che il calcolo degli sprechi deve essere fatto porto per porto,
#   e' sbagliato calcolare gli sprechi in un'unica soluzione alla fine del viaggio.
#   Si ricorda che la struttura dati passata come parametro in ingresso alla funzione
#   inizia con il caricamento di cibo e acqua nel porto di partenza e
#   termina con l'arrivo nel porto di fine viaggio (nel porto di fine viaggio non vengono
#   caricati acqua e cibo, per questo e' indicato un caricamento di 0.0 kg di cibo e di
#   0.0 litri di acqua).
#   In caso di dubbi date un'occhiata all'ultima riga del file .csv
def calcolaSprechi(dati):
    pass # Questa istruzione puo' essere eliminata.



# - calcolaConsumoPerMarinaio(...).  La funzione accetta come parametro
#   in ingresso la struttura dati restituita dalla funzione caricaDatiProvviste.
#   La funzione deve restituire un dizionario di coppie chiave valore, dove la
#   chiave e' il nome di un marinaio e il valore e' una lista che contiene
#   rispettivamente i kg di cibo e i litri d'acqua consumati dal marinaio.
#   Un esempio di output restituito e':
#   {'Marco':[10.5, 140.75], 'Aurora':[16.5, 177.5], ...} # N.B.: i valori qua
#   sopra sinistra non corrispondono ai risultati reali.
def calcolaConsumoPerMarinaio(dati):
    pass # Questa istruzione puo' essere eliminata.
            


##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione. 
##########################################################


print('Esercizio %s.' % (nomeEsercizio))
print('Ciao (%s, %s, %s)' % (studenteNome, studenteCognome, studenteMatricola))

print('1) Eseguo la funzione caricaDatiProvviste')
fn = 'caricoscarico.csv'
sd = caricaDatiProvviste(fn)
print('Risultato: ')
print(sd)

print('2) Eseguo la funzione calcolaCostiProvviste: ')
importo=calcolaCostiProvviste(sd)
print('Risultato: ')
print(importo)

print('3) Eseguo la funzione calcolaSprechi: ')
sprechi = calcolaSprechi(sd)
print('Risultato: ')
print(sprechi)

print('4) Eseguo la funzione : calcolaConsumoPerMarinaio')
consumi = calcolaConsumoPerMarinaio(sd)
print('Risultato: ')
print(consumi)

