# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'ecommerce'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituita da una delle funzioni seguenti,
# La vera struttura dati caricata dal file sara' più lunga,
# i primi elementi delle due strutture dati non e' detto che coincidano.

datiCommercio = {
    'vendite': [
        ('0', '0', 7, 245), ('1', '1', 7, 80), ('5', '3', 4, 200), ('5', '8', 5, 204), ('4', '7', 4, 141), ('0', '6', 5, 240), ('0', '4', 6, 245), ('7',
                                                                                                                                                    '4', 5, 16), ('8', '0', 6, 54), ('3', '9', 1, 24), ('0', '7', 1, 234), ('5', '1', 4, 168), ('9', '5', 6, 227), ('6', '7', 4, 258), ('1', '0', 9, 67)
    ],
    'clienti': [
        ('0', 'Roberto', 'Bianchi'), ('1', 'Sofia', 'Conti'), ('2', 'Sofia', 'Colombo'), ('3', 'Giovanna', 'Salieri'), ('4', 'Sara', 'Lombardi'), ('5',
                                                                                                                                                   'Nicola', 'Bianchi'), ('6', 'Paolo', 'Salieri'), ('7', 'Giovanna', 'Rossi'), ('8', 'Lucia', 'Salieri'), ('9', 'Anna', 'Rossi')
    ],
    'prodotti': [
        ('0', 'friggitrice', '0'), ('1', 'aspirapolvere', '3'), ('2', 'fornello', '3'), ('3', 'frullatore', '6'), ('4', 'frullatore',
                                                                                                                   '1'), ('5', 'tostapane', '0'), ('6', 'tostapane', '9'), ('7', 'ferro_da_stiro', '9'), ('8', 'tostapane', '1'), ('9', 'frullatore', '2')
    ]
}


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritto qua di seguito
#
# - File 1) 'vendite.csv'
#   Il file memorizza le informazioni sui prodotti, sui clienti e sulle vendite
#   di un sito di commercio on-line.
#   Nel file sono presenti TRE DIVERSE TIPOLOGIE di righe,
#   il tipo riga è riconoscibile dalla prima parola presente
#   nella riga, come negli esempi qua sotto. I valori sono separati da ;
#   Le prime tre righe del file sono le intestazioni, che spiegano come
#   sono strutturate le informazioni nelle righe del file.
#   Le tipologie di righe si susseguono con un ordine casuale.
#   Nell'esempio qua sotto non considerate il simbolo di # e
#   gli spazi iniziali. Gli a capo (\r\n) sono stati omessi per semplicita'.
#   Record e' un sinonimo di 'riga'.
#
#        tipo_record;id_prodotto;descrizione;id_categoria
#        tipo_record; id_cliente;nome;cognome
#        tipo_record;id_prodotto;id_cliente;qt;prezzo_unitario
#        ...
#        prodotto;0;friggitrice;0
#        cliente;0;Roberto;Bianchi
#        vendita;0;0;7;245
#        prodotto;1;aspirapolvere;3
#        cliente;1;Sofia;Conti
#        vendita;1;1;7;80
#        cliente;2;Sofia;Colombo
#        prodotto;2;fornello;3
#        vendita;37;18;5;278
#        vendita;17;3;9;49
#        prodotto;3;frullatore;6
#        cliente;3;Giovanna;Salieri
#        ...
#
#  Nel file sono presenti TRE DIVERSE TIPOLOGIE di righe, rispettivamente righe con
#     * Riga 'prodotto'. Questa riga contiene le informazioni su un
#       prodotto messo in vendita, la riga ospita le seguenti informazioni:
#         - tipo_record. C'è sempre la stringa 'prodotto' in questo tipo di riga
#         - id_prodotto. Un valore numerico che identifica univocamente il prodotto
#         - descrizione. La descrizione del prodotto
#         - id_categoria. Un valore numerico che identifica la categoria di appartenenza del prodotto.
#     * Riga 'cliente'. Questa riga contiene le informazioni sui
#       clienti che hanno effettuato acquisti, la riga ospita le seguenti informazioni:
#         - tipo_record. C'è sempre la stringa 'cliente' in questo tipo di riga
#         - id_cliente. Un valore numerico che identifica univocamente il cliente
#         - nome. Il nome del cliente
#         - cognome. Il cognome del cliente
#     * Riga 'vendita'. Questa riga contiene le informazioni sugli
#       acquisti effettuati dai clienti, la riga ospita le seguenti informazioni:
#         - tipo_record. C'è sempre la stringa 'vendita' in questo tipo di riga
#         - id_prodotto. Un valore numerico che identifica il prodotto venduto
#         - id_cliente. Un valore numerico che identifica il cliente che ha effettuato l'acquisto
#         - qt. La Quantita' di prodotti acquistata
#         - prezzo_unitario. Il prezzo di un singolo prodotto. Se il cliente ha acquistato piu'
#           di un prodotto, il prezzo totale dell'acquisto e' dato dal prezzo_unitario moltiplicato
#           per la quantita' venduta. Lo stesso bene puo' assumere prezzi diversi nelle diverse
#           righe di vendita.

#  Nota bene: una riga di vendita puo' contenere informazioni su clienti o su prodotti
#  i cui dati saranno presentati in righe successive.
#  Per ogni cliente e prodotto nominati nel file c'è sicuramente una riga corrispondente
#  di tipo (rispettivamente) 'cliente' o 'prodotto'. Tuttavia,
#  queste righe possono non essere vicine tra loro.


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

cognome = 'Liu'  # inserisci qua il tuo cognome
nome = 'WeiHao'  # inserisci qua il tuo nome


# - La funzione seguente accetta come parametro in ingresso
#   il nome del file .csv contenente i dati descritti in precedenza.
#   La funzione deve restituire un dizionario di liste, come nell'esempio seguente.
#        {
#          'prodotti': [ (id_prodotto1,descrizione1,id_categoria1), ... (id_prodottoN,descrizioneN,id_categoriaN) ],
#          'clienti': [ (id_cliente1,nome1,cognome1), ... (id_clienteN, nomeN, cognomeN) ],
#          'vendite': [ (id_prodotto1,id_cliente1,qt1,prezzo_unitario1), ..., (id_prodottoN,id_clienteN,qtN,prezzo_unitarioN) ]
#        }
#   dove ogni valore associato ad una chiave e' una lista di informazioni,
#   rispettivamente sui prodotti, sui clienti e sulle vendite.
#   In 'vendite', QT e PREZZO_UNITARIO devono essere di TIPO INTERO.
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
#   se in via provvisoria volete far lavorare le funzioni successive senza
#   implementare l'attuale, potete utilizzare la struttura dati dichiarata
#   all'inizio di questo script.
#   Tale struttura dati e' una versione piu' corta ma simile a quella
#   che dovrebbe restituire la vostra implementazione.
#   OVVIAMENTE, se userete la struttura dati gia' presente,
#   l'esercizio sara' considerato non svolto
def caricaDatiVendite(fn):
    # return datiCommercio # se non riuscite ad implementare la funzione, potete usare temporaneamente qs dati
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    file = open(fn, 'r')
    file.readline()
    list_prodotto = []
    list_clienti = []
    list_vendite = []
    for line in file:
        line = line.strip('\n').strip('\r')
        record = line.split(';')  # 是个列表
        if record[0] == 'prodotto':
            id_prodotto = record[1]
            descrizione = record[2]
            id_categoria = record[3]
            list_prodotto.append((id_prodotto, descrizione, id_categoria))
        if record[0] == 'cliente':
            id_cliente = record[1]
            name = record[2]
            surname = record[3]
            list_clienti.append((id_cliente, name, surname))
        if record[0] == 'vendita':
            id_prodotto, id_cliente, qt, prezzo_uni = record[1:5]
            list_vendite.append(
                (id_prodotto, id_cliente, int(qt), int(prezzo_uni)))

    dati_vendite = {'prodotto': list_prodotto,
                    'clienti': list_clienti, 'vendite': list_vendite}
    return dati_vendite

    # - La funzione seguente accetta come parametro in ingresso la struttura dati
    #   restituita dalla funzione caricaDatiVendite().
    #   La funzione seguente deve restituire un dizionario come nell'esempio seguente
    #        {
    #         id_cliente1:totale_acquisti1,
    #         id_cliente2:totale_acquisti2,
    #         ...,
    #         id_clienteN:totale_acquistiN
    #        }
    #   Ogni coppia riporta informazioni sul totale degli acquisti effettuato da un cliente.
    #   id_cliente riporta l'identificatore del cliente, totale_acquisti riporta il prezzo
    #   totale speso dal cliente per acquisti.
    #   Alcune precisazioni che vi possono essere utili:
    #   - Se in un acquisto il cliente 99 ha comprato 10 oggetti dal prezzo di 5 euro l'uno,
    #     e in un secondo acquisto ha comprato 2 oggetti dal prezzo di 100 euro l'uno,
    #     supponendo che si tratti delle uniche spese del cliente 99,
    #     la spesa totale del cliente 99 e': (10x5 + 100x2)=250.
    #   - Se un cliente non ha effettuato spese, non deve apparire nel dizionario restituito.


def totaliClienti(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    list_clienti = ds['vendite']
    dati_clienti = {}
    for i in list_clienti:
        id_prodotto, id_cliente, qt, prezzo_uni = i
        if id_cliente not in dati_clienti:
            dati_clienti[id_cliente] = 0
        dati_clienti[id_cliente] += qt * prezzo_uni
    return dati_clienti

    # - La funzione seguente accetta come parametro in ingresso la struttura dati
    #   restituita dalla funzione caricaDatiVendite().
    #   La funzione seguente deve restituire una lista come nell'esempio seguente
    #
    #        [totale_acquisti_categoria0, totale_acquisti_categoria1, ..., totale_acquisti_categoriaN]
    #
    #   Ogni valore della lista deve riportare il totale delle vendite per una specifica categoria.
    #   L'elemento di posizione=0 deve corrispondere al totale delle vendite dei prodotti con id_categoria=0,
    #   l'elemento di posizione=1 deve corrispondere al totale delle vendite dei prodotti con id_categoria=1, ...
    #   L'id_categoria di un prodotto e' un'informazione presente nella struttura dati ricevuta
    #   in ingresso, nella parte relativa ai prodotti.
    #   Alcune precisazioni che vi possono essere utili:
    #   - Nel calcolo dei prezzi occorre tenere in considerazione le quantita' vendute,
    #     si vedano le indicazioni date per l'esercizio precedente.
    #   - l'id_categoria massimo deve essere ricavato dalla struttura dati
    #     ricevuta in ingresso da questa funzione
    #   - se per un id_categoria non ci fossero vendite, inserire 0 nella lista


def totaliCategorie(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    list_categoria = []
    liCat = ds['prodotto']
    temp_dict = {}
    max_cat = 0
    for i in liCat:
        (id_prodotto, descrizione, id_categoria) = i
        id_prodotto = int(id_prodotto)
        id_categoria = int(id_categoria)
        temp_dict[id_prodotto] = id_categoria
        if id_categoria > max_cat:
            max_cat = id_categoria

    # (max_cat +1) 用来确保可以把所有数据存储倒列表里,不然的话只有一个元素那就是0
    totCat = [0] * (max_cat + 1)
    liVendite = ds['vendite']
    for i in liVendite:
        (id_prodotto, id_cliente, qt, prezzo_uni) = i
        prezzo_totale = int(qt) * int(prezzo_uni)
        id_categoria = temp_dict[int(id_prodotto)]
        totCat[id_categoria] += prezzo_totale
    return totCat


# - La funzione seguente accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiVendite() # In alcune versione del file la funzione appena citata e' stata erroneamente scritta come sommarioAppartamenti().
#   La funzione deve restituire un'unica tupla come la seguente
#
#       (id_cliente, id_prodotto, spesa_del_cliente_per_il_prodotto)
#
#   contenente la combinazione di id_cliente e id_prodotto che ha fatto incassare di piu' all'azienda.
#   Se ci fossero piu' combinazioni a pari merito, ne deve essere scelta una, con un criterio a vostra scelta.
#
def combinazioneMassima(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    combMax = {}
    list_vendite = ds['vendite']
    for i in list_vendite:
        (id_prodotto, id_cliente, qt, prezzo_uni) = i
        key = str(id_cliente)+'_'+str(id_prodotto)
        if key not in combMax:
            combMax[key] = 0
        combMax[key] += int(qt) * int(prezzo_uni)

    max_key = None
    for key in combMax:  # for 循环字典的话,临时变量是key值
        if max_key == None or combMax[key] > combMax[max_key]:  # 判断时不时最大的值
            max_key = key

    id_cliente = max_key.split('_')[0]  # split方法返回的是一个列表
    id_prodtto = max_key.split('_')[1]
    combinazioneMax = (id_cliente, id_prodotto, combMax[max_key])
    return combinazioneMax


##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################
print('Esercizio %s.' % (nomeEsercizio))
print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione caricaDatiVendite: ')
fnv = 'Esame-uni/Documents/Esame uni/2018-19/2019_07_11/vendite.csv'
dv = caricaDatiVendite(fnv)
print(dv)

print('2) Eseguo la funzione totaliClienti: ')
tcli = totaliClienti(dv)
print(tcli)

print("3) Eseguo la funzione totaliCategorie: ")
tcat = totaliCategorie(dv)
print(tcat)

print("4) Eseguo la funzione combinazioneMassima: ")
cm = combinazioneMassima(dv)
print(cm)

print('Nome file e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
