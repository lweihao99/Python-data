# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'pubMed'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituita da una delle funzioni seguenti,
# La (vera) struttura dati caricata dal file sara' più lunga,
# i primi elementi di entrambe possono essere diversi.
# OVVIAMENTE, se non implementerete la funzione di lettura da file,
# quest'ultima sara' considerata non svolta

dLavori = {'32061199': {'location': 'China', 'date': '2020 Feb 16', 'title': '[Conventional respiratory support therapy for Severe Acute Respiratory Infections(SARI): Clinical indications and nosocomial infection prevention and control].', 'doi': '10.3760/cma.j.issn.1001-0939.2020.0015'},
           '32061198': {'location': 'China', 'date': '2020 Feb 16', 'title': '[Inhibitors of RAS Might Be a Good Choice for the Therapy of COVID-19 Pneumonia].', 'doi': '10.3760/cma.j.issn.1001-0939.2020.0014'},
           '32061066': {'location': 'China', 'date': '2020 Feb 15', 'title': '[Clinical features of 2019 novel coronavirus pneumonia in the early stage from afever clinic in Beijing].', 'doi': '10.3760/cma.j.issn.1001-0939.2020.0013'},
           '32060933': {'location': 'England', 'date': '2020 Feb 14', 'title': '2019_nCoV: Rapid classification of betacoronaviruses and identification oftraditional Chinese medicine as potential origin of zoonotic coronaviruses.', 'doi': '10.1111/lam.13285'},
           '32060789': {'location': 'China', 'date': '2020 Feb 14', 'title': 'The First Disease X is Caused by a Highly Transmissible Acute RespiratorySyndrome Coronavirus.', 'doi': '10.1007/s12250-020-00206-5'},
           '32060619': {'location': 'Germany', 'date': '2020 Feb 14', 'title': 'Imaging features of 2019 novel coronavirus pneumonia.', 'doi': '10.1007/s00259-020-04720-2'},
           '32060015': {'location': 'England', 'date': '2020 Feb 14', 'title': 'Coronavirus: home testing pilot launched in London to cut hospital visits andambulance use.', 'doi': '10.1136/bmj.m621'},
           '32059047': {'location': 'United States', 'date': '2020 Feb 14', 'title': 'A realistic two-strain model for MERS-CoV infection uncovers the high risk forepidemic propagation.', 'doi': '10.1371/journal.pntd.0008065'},
           '32058570': {'location': 'United States', 'date': '2020 Feb 14', 'title': 'Novel Coronavirus Infection in Hospitalized Infants Under 1 Year of Age in China.', 'doi': '10.1001/jama.2020.2131'},
           '32058086': {'location': 'England', 'date': '2020 Feb 11', 'title': 'Novel coronavirus: how the things are in Wuhan.', 'doi': '10.1016/j.cmi.2020.02.005'},
           '32057788': {'location': 'England', 'date': '2020 Feb 11', 'title': 'Novel coronavirus, poor quarantine, and the risk of pandemic.', 'doi': '10.1016/j.jhin.2020.02.002'},
           '32057769': {'location': 'Netherlands', 'date': '2020 Feb 10', 'title': 'The spike glycoprotein of the new coronavirus 2019-nCoV contains a furin-likecleavage site absent in CoV of the same clade.', 'doi': '10.1016/j.antiviral.2020.104742'},
           '32057575': {'location': 'Netherlands', 'date': '2020 Feb 11', 'title': 'Recombinant infectious bronchitis coronavirus H120 with the spike protein S1 geneof the nephropathogenic IBYZ strain remains attenuated but induces protectiveimmunity.', 'doi': '10.1016/j.vaccine.2020.01.001'},
           '32057299': {'location': 'United States', 'date': '2020 Feb 10', 'title': 'The first 2019 novel coronavirus case in Nepal.', 'doi': '10.1016/S1473-3099(20)30067-0'},
           '32057212': {'location': 'China', 'date': '2020 Feb 14', 'title': '[Recommendations for general surgery clinical practice in novel coronaviruspneumonia situation].', 'doi': '10.3760/cma.j.issn.0529-5815.2020.0001'},
           '32057211': {'location': 'China', 'date': '2020 Feb 14', 'title': '[An update on the epidemiological characteristics of novel coronaviruspneumoniaCOVID-19].', 'doi': '10.3760/cma.j.issn.0254-6450.2020.02.002'},
           '32057210': {'location': 'China', 'date': '2020 Feb 14', 'title': '[The prevention and control of a new coronavirus infection in department ofstomatology].', 'doi': '10.3760/cma.j.issn.1002-0098.2020.0001'},
           '32057209': {'location': 'China', 'date': '2020 Feb 14', 'title': '[Pharmacotherapeutics for the New Coronavirus Pneumonia].', 'doi': '10.3760/cma.j.issn.1001-0939.2020.0012'},
           '32056407': {'location': 'Korea (South)', 'date': '2020 Feb 17', 'title': 'Case of the Index Patient Who Caused Tertiary Transmission of COVID-19 Infectionin Korea: the Application of Lopinavir/Ritonavir for the Treatment of COVID-19Infected Pneumonia Monitored by Quantitative RT-PCR.', 'doi': '10.3346/jkms.2020.35.e79'},
           '32056397': {'location': 'Korea (South)', 'date': '2020 Feb 11', 'title': 'Novel Coronavirus Pneumonia Outbreak in 2019: Computed Tomographic Findings inTwo Cases.', 'doi': '10.3348/kjr.2020.0078'},
           '32056396': {'location': 'Korea (South)', 'date': '2020 Feb 11', 'title': 'Pneumonia Associated with 2019 Novel Coronavirus: Can Computed TomographicFindings Help Predict the Prognosis of the Disease?', 'doi': '10.3348/kjr.2020.0096'},
           '32056249': {'location': 'United States', 'date': '2020 Feb 13', 'title': 'Overlapping and discrete aspects of the pathology and pathogenesis of theemerging human pathogenic coronaviruses SARS-CoV, MERS-CoV, and 2019-nCoV.', 'doi': '10.1002/jmv.25709'},
           '32056235': {'location': 'United States', 'date': '2020 Feb 13', 'title': 'Does SARS-CoV-2 has a longer incubation period than SARS and MERS?', 'doi': '10.1002/jmv.25708'},
           '32056143': {'location': 'Germany', 'date': '2020 Feb 13', 'title': 'Non-influenza respiratory viruses in adult patients admitted with influenza-likeillness: a 3-year prospective multicenter study.', 'doi': '10.1007/s15010-019-01388-1'},
           '32055945': {'location': 'Germany', 'date': '2020 Feb 13', 'title': 'Initial CT findings and temporal changes in patients with the novel coronaviruspneumonia (2019-nCoV): a study of 63 patients in Wuhan, China.', 'doi': '10.1007/s00330-020-06731-x'},
           '32050635:': {'location': 'Switzerland', 'date': '2020 Feb 10', 'title': 'Potential Maternal and Infant Outcomes from (Wuhan) Coronavirus 2019-nCoVInfecting Pregnant Women: Lessons from SARS, MERS, and Other Human CoronavirusInfections.', 'doi': '10.3390/v12020194'},
           # attenzione, qua il doi non e' conforme
           '32053470': {'location': 'United States', 'date': '2020 Feb 13', 'title': 'Time Course of Lung Changes On Chest CT During Recovery From 2019 NovelCoronavirus (COVID-19) Pneumonia.', 'doi': '20.1148/radiol.2020200370'}
           }


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritto qua di seguito.
#
# - File 'pubmedCoronavirus.txt'
#   Il file memorizza le informazioni sulle pubblicazioni presenti nel database
#   PubMed che hanno come argomento gli studi scientifici sui coronavirus.
#   Si ricorda che i coronavirus sono una famiglia di diversi virus (tra cui l'influenza).
#   Un esempio del contenuto del file e' il seguente. Nell'esempio qua sotto non considerate
#   il simbolo # e gli spazi iniziali.
#   Gli a capo presenti nel file (\r\n) sono stati omessi per semplicita'.
#
# PMID- 32061199
# DP  - 2020 Feb 16
# TI  - [Conventional respiratory support therapy for Severe Acute Respiratory Infections
#       (SARI): Clinical indications and nosocomial infection prevention and control].
# PL  - China
# AID - 10.3760/cma.j.issn.1001-0939.2020.0015 [doi]
#
# PMID- 32061198
# DP  - 2020 Feb 16
# TI  - [Inhibitors of RAS Might Be a Good Choice for the Therapy of COVID-19 Pneumonia].
# PL  - China
# AID - 10.3760/cma.j.issn.1001-0939.2020.0014 [doi]
#
#   I dati di una pubblicazione sono composti dal PMID (un numero che
#   identifica univocamente la pubblicazione all'interno del dataset),
#   la data di pubblicazione, il titolo, il luogo di pubblicazione ed
#   il suo identificativo digitale (doi).
#
#   Le informazioni associate a ciascuna pubblicazione sono suddivise su più
#   righe, le righe hanno un'intestazione che ne dichiara il tipo,
#   ogni informazione occupa una singola riga, ad eccezione dei titoli
#   che possono estendersi su più righe come indicato qua sotto.
#   IMPORTANTE: I dati di una pubblicazione INIZIANO SEMPRE con il PMID,
#   e TERMINANO SEMPRE con una riga vuota. Quindi, la riga vuota funge
#   da separatore tra due pubblicazioni.
#       * `PMID` (PubMed ID) identificativo unico nel database PubMed
#       * `TI`  (TItolo) titolo della pubblicazione. Se il titolo occupa più righe, le righe
#              aggiuntive non hanno intestazione e sono indentate a destra.
#              Le [] dove presenti, fanno parte integrante del titolo.
#       * `DP` (Date of Publication) la data di pubblicazione
#       * `PL` (Location) il luogo di pubblicazione
#       * `AID` (Alternative IDentifier). Identificatore (alternativo al PMID)
#          che può essere usato per recuperare la pubblicazione in altri database.
#          In una singola pubblicazione ci possono essere diversi AID
#          (quindi possono esserci diverse righe che iniziano con AID).
#          Tra i diversi AID è molto importante il DOI (riconoscibile dalla
#          presenza della stringa '[doi]').
#          Il DOI (digital object identifier) è utile per recuperare la
#          pubblicazione dal Web. Non tutte le pubblicazioni hanno il DOI,
#          tuttavia se presente, lo trovate una volta solo per ogni pubblicazione.
#
#    Si suggerisce caldamente di ispezionare il file .txt

##########################################################
# INTRODUZIONE AL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede
# ogni funzione vi spiegherà in dettaglio che cosa fare.
# Controllate nel corpo principale del programma (in fondo
# allo script), come vengono invocate le funzioni che
# implementerete.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
# Se volete, potete implementare funzioni aggiuntive
# rispetto a quelle gia' presenti qua sotto.


##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome = 'Sostituiscimi con il cognome'  # inserisci qua il tuo cognome
nome = 'Sostituiscimi con il nome'  # inserisci qua il tuo nome


# - La funzione seguente accetta come parametro in ingresso
#   il nome del file .txt contenente i dati descritti in precedenza.
#   La funzione deve leggere il contenuto del file e
#   restituire un dizionario di dizionari, come nell'esempio seguente:
#   {   'PMID_1': {'location': nazione_1, 'date': data_1, 'title': titolo_1, 'doi': doi_1},
#       'PMID_2': {'location': nazione_2, 'date': data_2, 'title': titolo_2, 'doi': doi_2},
#           ...
#       'PMID_n': {'location': nazione_n, 'date': data_n, 'title': titolo_n, 'doi': doi_n}
#   }
#
#   Ad esempio i dati della seguente pubblicazione ...
#
# PMID- 32061199
# DP  - 2020 Feb 16
# TI  - [Conventional respiratory support therapy for Severe Acute Respiratory Infections
#     (SARI): Clinical indications and nosocomial infection prevention and control].
# PL  - China
# AID - 10.3760/cma.j.issn.1001-0939.2020.0015 [doi]
#
# ... produrranno la coppia chiave valore che segue:
#
#   '32061199': {'location': 'China', 'date': '2020 Feb 16',
#                'title': '[Conventional respiratory support therapy for Severe Acute Respiratory Infections(SARI): Clinical indications and nosocomial infection prevention and control].',
#                'doi': '10.3760/cma.j.issn.1001-0939.2020.0015'}
#
# Tutti gli elementi del dizionario devono essere di tipo stringa.
# Dal valore associato a 'doi' deve essere rimossa la stringa ' [doi]'.
# Tra i vari AID disponibili, (si ricorda che una pubblicazione può avere diversi AID)
# dovete utilizzare solamente il DOI. Se il DOI non è disponibile,
# nel dizionario (di cui sopra) associate la stringa vuota alla chiave 'doi'.
# Si ricorda che nel file, i dati di una singola pubblicazione
# - iniziano sempre con il PMID
# - terminano con una riga vuota
# l'ordine di tutti gli altri elementi tra il PMID e la riga vuota può variare.
# Si suggerisce caldamente di ispezionare il file .txt
#
# NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
# se in via provvisoria volete far lavorare le funzioni successive senza
# implementare l'attuale, potete utilizzare la struttura dati dichiarata
# all'inizio di questo script (basta togliere il commento dalla prima riga di codice).
def caricaDatiPubblicazioni_v2(fn):
    # return dLavori # se non riuscite ad implementare la funzione, potete usare temporaneamente questa
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    fd = open(fn, 'r')
    fd.readline()  # salto la prima riga
    pmid = ''
    di = {}
    largeDict = {}
    for line in fd:
        line = line.strip('\n').strip('\r')
        tipoRiga = line[:5]
        parteRimanente = line[6:]
        if len(line) > 0:  # gli \n e \r sono gia' stati tolti
            # siamo nel caso di una riga diversa da quella vuota
            if tipoRiga == 'PMID-':
                # Imposto i valori per una nuova pubblicazione, dato che il pmid e' il primo tra tutti i dati
                pmid = parteRimanente.strip(' ')
                di = {'location': '', 'date': '', 'title': '', 'doi': ''}
            elif tipoRiga == 'DP  -':
                di['date'] = parteRimanente.strip(' ')
            elif tipoRiga == 'TI  -':
                di['title'] = parteRimanente.strip(' ')
            elif tipoRiga == '     ':  # sono le righe con il continuo del titolo
                # lo spazio serve per non appiccicare l'ultima parola della riga precedente con la prima parola della riga attuale
                di['title'] = di['title'] + ' ' + parteRimanente.strip(' ')
            elif tipoRiga == 'PL  -':
                di['location'] = parteRimanente.strip(' ')
            elif tipoRiga == 'AID -':
                aid = parteRimanente.strip(' ')
                if '[doi]' in aid:
                    di['doi'] = aid.strip(' [doi]')
        else:
            # se siamo qua vuol dire che siamo arrivati alla riga vuota che chiude i dati di una pubblicazione
            # inserisco nel dizionario piu' grande il dizionario con i dati della singola pubblicazione
            largeDict[pmid] = di
    fd.close()
    return largeDict

# Un'altra possibile implementazione


def caricaDatiPubblicazioni(fn):
    # return dLavori # se non riuscite ad implementare la funzione, potete usare temporaneamente questa
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    lKinds = ['PMID', 'PL  ', 'DP  ', 'TI  ', 'AID ', '    ']
    dict2ret = {}  # Il dizionario che dovra' essere restituito
    with open(fn, 'r') as streamIn:
        dPub = {'PMID': '', 'location': '', 'date': '', 'title': '', 'doi': ''}
        PMID = 'fake'
        for riga in streamIn:  # 逐行读取内容,每行内容为字符串
            # print(riga)
            kind = riga[:4]  # 读取0-3 的字符,字符串切片
            content = riga[5:]  # 从第5个字符开始读取倒
            if kind in lKinds:  # tipo di interesse o righe con tipo '    -'
                if kind == 'PMID':
                    # Inserisco i dati della vecchia pubblicazione.
                    dict2ret[PMID] = dPub
                    # se sono all'inizio verra' inserito 'fake' come PMID (che sara' poi rimosso alla fine,
                    # altrimenti sara' utilizzato il PMID letto in precedenza
                    PMID = content.strip()  # Setto il nuovo PMID
                    # print(PMID)
                    dPub = {'location': '', 'date': '', 'title': '', 'doi': ''}
                elif kind == 'TI  ':
                    dPub['title'] += content.strip()
                elif kind == '    ':
                    dPub['title'] += content.strip()
                elif kind == 'PL  ':
                    dPub['location'] = content.strip()
                elif kind == 'DP  ':
                    dPub['date'] = content.strip()
                elif kind == 'AID ' and '[doi]' in content:
                    # 不把最后几个字符包含进去,也就是['doi']给去掉
                    dPub['doi'] = content[:-len('[doi]') - 1].strip()
        streamIn.close()
    if PMID not in dict2ret:
        # In questo modo inserisco l'ultima pubblicazione
        dict2ret[PMID] = dPub

    # elimino i dati fake inseriti inizialmente
    del dict2ret['fake']

    return(dict2ret)

# Funzione accessoria utilizzata dalla funzione successiva


def checkDOI(sDOI):  # cancellami
    if sDOI[:3] == '10.':
        return sDOI
    else:
        return ''

# - La funzione controllaDOI accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiPubbicazioni().
#   La funzione deve restituire una struttura dati identica a quella ricevuta in ingresso in cui
#   tutti i doi non conformi (maggiori dettagli fra poco) sono sostituiti da una stringa vuota.
#   Un doi è da considerarsi conforme se inizia esattamente per '10.', altrimenti è da
#   considerarsi non conforme.


def controllaDOI(dPubbl):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    for pub in dPubbl:
        # print(dPubbl[pub]['doi'])
        dPubbl[pub]['doi'] = checkDOI(dPubbl[pub]['doi'])
    return dPubbl

# - La funzione annoPubblicazioni accetta come parametro in ingresso la struttura dati
#   restituita dalla funzione caricaDatiPubblicazioni().
#   La funzione deve restituire un dizionario contenente il numero di
#   pubblicazioni presenti stratificate per anno.
#   Il dizionario restituito deve avere la seguente struttura:
#   { anno_1: nPubblicazioniAnno1, anno_2: nPubblicazioniAnno2, ...}
#   dove sia le chiavi anno_i che e i valori dei conteggi associati devono
#   essere valori interi.


def annoPubblicazioni(diz):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    dCounts = {}
    for pub in diz:
        date = diz[pub]['date']
        year = int(date[:4])
        if year not in dCounts:
            dCounts[year] = 1
        else:
            dCounts[year] += 1
    return dCounts


# - La funzione contaParole accetta come parametri in ingresso
#   * la struttura dati restituita dalla funzione caricaDatiPubblicazioni() ed
#   * una stringa identificativa di una pubblicazione (vale a dire, un PMID).
#   La funzione deve restituire, dopo aver rimosso i simboli di punteggiatura,
#   il numero di parole presenti nel titolo associato alla pubblicazione
#   identificata dalla stringa PMID passato come secondo parametro.
#   Come simboli di punteggiatura, orientativamente considerate
#   .,:;?!-—()[]'“”...
#   (l'ultimo elemento sono i 3 punti di sospensione), i due segni meno consecutivi
#   sono in realtà due tipi diversi di meno. Se qualcuno dei simboli di cui sopra
#   vi da problemi nell'editor di testo, ignoratelo.
#   Si ricorda che, su una variabile di tipo stringa, è possibile richiamare
#   il metodo replace con la notazione punto per sostituire una sottostringa con
#   un'altra, come nell'esempio seguente
#   st='ciao ciao'
#   st2 = st.replace('o', 'u')) # 'ciau ciau'

# Funzione accessoria
def togliPunteggiatura(sIn):
    lPunctMarks = ['.', ',', ':', ';', '?', '!', '-', '—', '(', ')',
                   '[', ']', '...', "'", '“', '”']
    sOut = sIn
    for p in lPunctMarks:
        sOut = sOut.replace(p, '')
    return sOut


def contaParole(diz, ID):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    titolo = diz[ID]['title']
    titoloNoPunt = togliPunteggiatura(titolo)
    # print(titolo)
    # print(titoloNoPunt)
    # riduco eventuali spazi doppi a spazi singoli
    titoloNoPunt = titoloNoPunt.replace('  ', ' ')
    print(titoloNoPunt.strip().split(' '))
    return(len(titoloNoPunt.strip().split(' ')))


##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################

print('Esercizio %s.' % (nomeEsercizio))
print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione caricaDatiPubblicazioni: ')
fnv = 'Esame-uni/Documents/Esame uni/2020_02_20/pubmedCoronavirus.txt'
dc = caricaDatiPubblicazioni(fnv)
if type(dc) == type({}):
    print('Saranno visualizzate solo i valori associati alle prime 20 chiavi')
    lKeys = list(dc.keys())
    for el in lKeys[0:20]:
        print(dc[el])
else:
    print(dc)

print('2) Eseguo la funzione controllaDOI: ')
dc2 = controllaDOI(dc)
if type(dc2) == type({}) and '32053470' in dc2:
    print('doi:', dc2['32053470']['doi'])
else:
    print(dc2)

print("3) Eseguo la funzione annoPubblicazioni")
aP = annoPubblicazioni(dc)
print(aP)

print("4) Eseguo la funzione contaParole")
print(contaParole(dc, '32050635'))

print('Nome file e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
