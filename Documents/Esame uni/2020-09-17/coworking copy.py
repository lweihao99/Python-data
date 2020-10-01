# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe
import re
from re import template
nomeEsercizio = 'coWorking'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituita da una delle funzioni seguenti.
# La (vera) struttura dati caricata dal file sara' diversa:
# può essere più lunga, i primi elementi possono differire come valori.

datiCoworking = [[0, '04/01/2018', 34, 59, 166, 155, 58, 72, 154, 168, 236, 214, 180, 127, 112, 201, 54, 49, 16, 148, 68, 185, 106, 140, 116, 70, 2, 48, 66, 133, 209, 77], [1, '04/01/2018', 14, 38], [2, '04/01/2018', 13, 177], [3, '04/01/2018', 212, 8, 71], [4, '04/01/2018', 12, 228], [5, '04/01/2018', 6, 95, 97, 219], [6, '04/01/2018', 165, 205, 11, 56, 118], [7, '04/01/2018', 167, 60, 10, 80, 105], [8, '04/01/2018', 235, 3, 182], [9, '04/01/2018', 1, 42, 84], [0, '08/01/2018', 4, 123, 90, 85, 231, 215, 98, 103, 193, 199, 27, 74, 73, 64, 165, 36, 86, 135, 134, 40, 142, 234, 33, 53, 63, 92, 163, 207, 56, 118], [1, '08/01/2018', 3, 182], [2, '08/01/2018', 1, 82, 230], [3, '08/01/2018', 144, 7, 148, 161, 214], [4, '08/01/2018', 58, 75, 83, 19, 146], [5, '08/01/2018', 151, 0, 141, 206, 157], [6, '08/01/2018', 106, 5, 101], [7, '08/01/2018', 108, 12, 187], [8, '08/01/2018', 6, 30], [9, '08/01/2018', 116, 159, 2, 44], [0, '11/01/2018', 165, 222, 83, 170, 174, 45, 33, 213, 19, 58, 7, 205, 90, 207, 238, 177, 11, 160, 59, 55, 50, 76, 179, 71, 73, 60, 48, 188, 0, 62], [1, '11/01/2018', 182, 20, 3, 89], [2, '11/01/2018', 228, 93, 108, 12, 65], [3, '11/01/2018', 31, 6, 95, 176], [4, '11/01/2018', 70, 9, 68, 145], [5, '11/01/2018', 117, 2, 229, 237], [6, '11/01/2018', 18, 21], [7, '11/01/2018', 5, 101, 106], [8, '11/01/2018', 4, 34, 128], [9, '11/01/2018', 152, 16, 67], [0, '13/01/2018', 231, 127, 88, 109, 116, 35, 185, 184, 103, 71, 173, 18, 139, 182, 92, 36, 230, 110, 40, 112, 131, 86, 170, 221, 100, 145, 198, 45, 74, 20], [1, '13/01/2018', 5, 69], [2, '13/01/2018', 43, 164, 153, 6, 61], [3, '13/01/2018', 13, 177], [4, '13/01/2018', 11, 238], [5, '13/01/2018', 7, 107, 174], [6, '13/01/2018', 15, 193, 199, 178], [7, '13/01/2018', 10, 73, 80], [8, '13/01/2018', 19, 83], [9, '13/01/2018', 0, 150, 66, 48, 129], [0, '14/01/2018', 141, 215, 25, 110, 0, 212, 14, 205, 99, 58, 159, 103, 96, 210, 29, 233, 129, 188, 48, 78, 137, 186, 117, 57, 84, 124, 123, 74, 152, 55], [1, '14/01/2018', 24, 220, 3, 143], [2, '14/01/2018', 196, 228, 187, 12, 108], [3, '14/01/2018', 5, 132, 101], [4, '14/01/2018', 6, 115, 31, 164], [5, '14/01/2018', 18, 92, 221, 231], [6, '14/01/2018', 73, 10, 197], [7, '14/01/2018', 13, 177], [8, '14/01/2018', 4, 185], [9, '14/01/2018', 218, 179, 189, 7, 144], [0, '15/01/2018', 206, 44, 142, 7, 67, 70, 131, 55, 111, 162, 155, 49, 16, 86, 174, 35, 30, 164, 129, 88, 130, 140, 37, 33, 159, 97, 211, 150, 14, 152], [1, '15/01/2018', 10, 105, 207, 80, 64], [2, '15/01/2018', 81, 54, 69, 5, 203], [3, '15/01/2018', 32, 238, 11, 213], [4, '15/01/2018', 19, 57], [5, '15/01/2018', 147, 1, 42, 230], [6, '15/01/2018', 8, 200, 188, 225, 172], [7, '15/01/2018', 13, 177], [8, '15/01/2018', 227, 184, 24, 3, 220], [9, '15/01/2018', 178, 15, 199, 137, 193], [0, '16/01/2018', 174, 96, 109, 214, 229, 116, 49, 28, 157, 48, 39, 113, 195, 164, 127, 178, 52, 119, 65, 91, 176, 63, 199, 31, 165, 45, 115, 13, 187, 25], [1, '16/01/2018', 67, 16, 47], [2, '16/01/2018', 5, 81], [3, '16/01/2018', 9, 68], [4, '16/01/2018', 8, 71], [5, '16/01/2018', 4, 51], [6, '16/01/2018', 3, 182], [7, '16/01/2018', 126, 18, 36, 92], [8, '16/01/2018', 10, 167], [9, '16/01/2018', 1, 230, 139], [0, '17/01/2018', 110, 93, 108, 151, 216, 90, 55, 162, 56, 41, 102, 190, 142, 177, 228, 67, 157, 128, 212, 155, 38, 23, 32, 213, 203, 51, 238, 159, 0, 74], [1, '17/01/2018', 15, 137], [2, '17/01/2018', 17, 49, 98], [3, '17/01/2018', 6, 79, 219, 113], [4, '17/01/2018', 197, 10, 207, 105], [5, '17/01/2018', 158, 3, 184, 143], [6, '17/01/2018', 201, 19, 83, 136], [7, '17/01/2018', 189, 7, 107, 174], [8, '17/01/2018', 147, 84, 42, 1, 82], [9, '17/01/2018', 18, 22, 92, 77], [0, '18/01/2018', 235, 126, 192, 121, 23, 149, 157, 132, 20, 61, 179, 165, 106, 127, 141, 221, 97, 140, 9, 72, 86, 115, 144, 227, 200, 166, 92, 160, 162, 218], [1, '18/01/2018', 19, 57, 62, 96, 59], [2, '18/01/2018', 93, 12, 26, 228], [3, '18/01/2018', 14, 239, 39], [4, '18/01/2018', 73, 10, 197, 94], [5, '18/01/2018', 209, 215, 16, 41], [6, '18/01/2018', 13, 177], [7, '18/01/2018', 2, 229], [8, '18/01/2018', 1, 139], [9, '18/01/2018', 15, 222, 199], [0, '20/01/2018', 61, 101, 176, 88, 130, 81, 155, 179, 15, 131, 151, 217, 42, 144, 124, 21, 72, 224, 134, 163, 67, 206, 114, 5, 107, 231, 106, 40, 48, 178], [1, '20/01/2018', 86, 216, 9, 145], [2, '20/01/2018', 59, 91, 19, 186], [3, '20/01/2018', 93, 12, 187, 228, 196], [4, '20/01/2018', 11, 32, 90], [5, '20/01/2018', 10, 207], [6, '20/01/2018', 200, 225, 170, 8, 29], [7, '20/01/2018', 3, 125, 227, 235, 24], [8, '20/01/2018', 13, 177],
                 [9, '20/01/2018', 2, 175], [0, '24/01/2018', 158, 146, 234, 54, 235, 106, 74, 185, 3, 25, 84, 105, 49, 34, 69, 154, 104, 220, 224, 172, 201, 33, 39, 136, 4, 132, 51, 228, 80, 93], [1, '24/01/2018', 180, 7, 161], [2, '24/01/2018', 9, 233], [3, '24/01/2018', 206, 111, 0, 141], [4, '24/01/2018', 31, 6, 95, 61], [5, '24/01/2018', 16, 138], [6, '24/01/2018', 13, 177], [7, '24/01/2018', 18, 163, 21, 92, 22], [8, '24/01/2018', 229, 2, 109, 116, 208], [9, '24/01/2018', 11, 213, 204, 32], [0, '28/01/2018', 202, 205, 4, 184, 152, 178, 192, 32, 110, 194, 230, 84, 165, 227, 185, 167, 203, 234, 16, 88, 134, 140, 69, 81, 131, 17, 231, 236, 104, 158], [1, '28/01/2018', 175, 159, 2, 195, 109], [2, '28/01/2018', 33, 14, 169, 38, 223], [3, '28/01/2018', 6, 97, 43], [4, '28/01/2018', 55, 151, 0, 130, 157], [5, '28/01/2018', 65, 12, 108, 93], [6, '28/01/2018', 8, 50], [7, '28/01/2018', 13, 177], [8, '28/01/2018', 62, 75, 19, 58], [9, '28/01/2018', 7, 148, 122, 133, 218], [0, '30/01/2018', 77, 236, 93, 98, 31, 3, 121, 224, 27, 206, 102, 119, 48, 81, 157, 108, 22, 88, 232, 209, 237, 185, 225, 172, 203, 100, 17, 106, 159, 150], [1, '30/01/2018', 15, 99, 137], [2, '30/01/2018', 19, 83], [3, '30/01/2018', 9, 68, 140], [4, '30/01/2018', 1, 230], [5, '30/01/2018', 73, 60, 10, 104], [6, '30/01/2018', 7, 226], [7, '30/01/2018', 13, 177], [8, '30/01/2018', 124, 103, 14, 239], [9, '30/01/2018', 32, 11, 213], [0, '02/02/2018', 59, 41, 96, 201, 130, 68, 203, 205, 237, 165, 132, 146, 208, 187, 227, 111, 82, 81, 12, 1, 168, 129, 154, 3, 158, 90, 196, 53, 186, 159], [1, '02/02/2018', 4, 166], [2, '02/02/2018', 14, 169], [3, '02/02/2018', 7, 107], [4, '02/02/2018', 126, 131, 18, 236, 72], [5, '02/02/2018', 6, 97], [6, '02/02/2018', 212, 8, 190, 181, 172], [7, '02/02/2018', 13, 177], [8, '02/02/2018', 15, 28, 123, 63, 178], [9, '02/02/2018', 17, 46, 173], [0, '03/02/2018', 123, 37, 46, 65, 191, 229, 124, 216, 140, 161, 146, 70, 49, 187, 117, 19, 226, 195, 33, 13, 91, 186, 178, 139, 223, 101, 239, 99, 173, 132], [1, '03/02/2018', 66, 0, 206, 119], [2, '03/02/2018', 4, 40], [3, '03/02/2018', 16, 171], [4, '03/02/2018', 32, 11, 90, 192, 23], [5, '03/02/2018', 10, 207], [6, '03/02/2018', 8, 190, 172], [7, '03/02/2018', 18, 131, 21, 126, 36], [8, '03/02/2018', 6, 79, 61], [9, '03/02/2018', 227, 89, 3, 220, 143], [0, '04/02/2018', 11, 91, 186, 162, 71, 23, 75, 127, 57, 199, 29, 129, 48, 88, 181, 4, 209, 62, 124, 67, 152, 201, 238, 144, 168, 225, 99, 217, 55, 50], [1, '04/02/2018', 10, 73], [2, '04/02/2018', 149, 6, 95, 211], [3, '04/02/2018', 108, 12, 228, 93], [4, '04/02/2018', 81, 5, 54], [5, '04/02/2018', 2, 37], [6, '04/02/2018', 9, 70, 35], [7, '04/02/2018', 42, 147, 1, 230], [8, '04/02/2018', 3, 125], [9, '04/02/2018', 13, 177], [0, '05/02/2018', 48, 41, 220, 177, 216, 198, 167, 234, 196, 169, 171, 67, 180, 50, 45, 7, 60, 107, 174, 64, 35, 17, 98, 127, 215, 0, 148, 33, 89, 152], [1, '05/02/2018', 82, 1, 139], [2, '05/02/2018', 2, 44], [3, '05/02/2018', 19, 76], [4, '05/02/2018', 213, 238, 204, 11, 192], [5, '05/02/2018', 4, 88, 185], [6, '05/02/2018', 61, 6, 149], [7, '05/02/2018', 203, 81, 5, 106, 132], [8, '05/02/2018', 15, 137], [9, '05/02/2018', 221, 236, 36, 18, 21], [0, '06/02/2018', 159, 6, 94, 30, 35, 59, 84, 57, 212, 58, 177, 195, 63, 61, 42, 149, 237, 199, 14, 140, 158, 83, 53, 223, 103, 229, 139, 232, 188, 8], [1, '06/02/2018', 12, 228], [2, '06/02/2018', 18, 236], [3, '06/02/2018', 51, 185, 4, 128, 134], [4, '06/02/2018', 17, 49, 46], [5, '06/02/2018', 5, 132], [6, '06/02/2018', 226, 179, 161, 7, 122], [7, '06/02/2018', 55, 0, 157], [8, '06/02/2018', 56, 11, 165], [9, '06/02/2018', 155, 16, 215, 138], [0, '07/02/2018', 41, 99, 9, 169, 182, 105, 23, 124, 164, 60, 149, 210, 54, 16, 14, 81, 94, 215, 69, 104, 88, 110, 3, 4, 219, 28, 78, 138, 86, 115], [1, '07/02/2018', 0, 66, 157], [2, '07/02/2018', 1, 230, 84, 147], [3, '07/02/2018', 57, 19, 91, 58], [4, '07/02/2018', 214, 174, 226, 7, 107], [5, '07/02/2018', 18, 131, 236, 221, 77], [6, '07/02/2018', 12, 26, 93, 108], [7, '07/02/2018', 2, 37], [8, '07/02/2018', 17, 45, 217], [9, '07/02/2018', 8, 212, 181, 188, 170], [0, '08/02/2018', 82, 149, 22, 126, 164, 158, 147, 86, 5, 71, 20, 196, 236, 110, 61, 176, 36, 183, 34, 221, 182, 89, 35, 65, 224, 8, 51, 184, 69, 132], [1, '08/02/2018', 19, 201], [2, '08/02/2018', 14, 39], [3, '08/02/2018', 155, 78, 47, 16, 27], [4, '08/02/2018', 63, 15, 99, 194], [5, '08/02/2018', 204, 192, 11, 56], [6, '08/02/2018', 0, 130, 150], [7, '08/02/2018', 2, 112], [8, '08/02/2018', 10, 80, 167], [9, '08/02/2018', 161, 7, 179]]


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritto qua di seguito.
#
# - File 1) 'copreno.csv'
#   Il file memorizza le informazioni sulle prenotazioni di spazi in un
#   coworking (un edificio che mette a disposizione stanze che possono
#   essere affittate su base giornaliera da lavoratori o team di lavoratori).
#   Un esempio del contenuto del file e' il seguente.
#   In ogni riga del file sono memorizzati un numero variabile di dati.
#   Nell'esempio qua sotto non considerate il simbolo di # e gli spazi iniziali.
#   Gli a capo presenti nel file (\r\n) sono stati omessi per semplicita'.
#   La prima riga descrive la struttura delle righe successive.
#
#   id_utente1;id_utente2;...;id_utenteN;giorno;id_stanza
#   34;59;166;155;58;72;154;168;236;68;185;106;140;116;70;2;48;66;133;209;77;04/01/2018;0
#   14;38;04/01/2018;1
#   13;177;04/01/2018;2
#   212;8;71;04/01/2018;3
#   12;228;04/01/2018;4
#   ...
#   In ogni record (record e' un sinonimo di 'riga')
#   sono memorizzate le informazioni sugli utenti del coworking
#   che hanno affittato una stanza. Le informazioni sono:
#   - id_stanza. E' l'ULTIMA informazione della riga. La stanza 0
#     e' l'open space e contiene tante postazioni di lavoro singole.
#     Le stanze piccole (id_stanza >= 1) invece sono stanze
#     da 5 posti che vengono affittate dai componenti
#     di un team (gruppo) di lavoro.
#     Un lavoratore affitta un posto nell'open space (id_stanza 0) quando
#     vuole svolgere una giornata di lavoro in autonomia. Quando
#     invece un gruppo di persone vuole svolgere una riunione,
#     allora affittano una stanza piccola (id_stanza >= 1).
#   - giorno. E' la PENULTIMA informazione della riga. Indica il giorno in
#     cui è stato affittata la stanza o una postazione nell'open space.
#   - id_utente1. E' la prima informazione della riga. Si tratta
#     dell'identificatore dell'utente che ha affittato
#     una postazione in una stanza e in un giorno ben precisi.
#   - id_utente2, ..., id_utenteN. In maniera analoga all'elemento precedente,
#     ogni id_utente successivo al primo indica un id_utente che ha prenotato
#     una postazione nella stanza. Se l'utente ha prenotato un posto in
#     una stanza piccola (id_stanza >= 1), allora tutti gli utenti che hanno
#     prenotato la stessa stanza nello stesso giorno fanno parte
#     dello stesso team di lavoro.
#     L'open space (id_stanza 0) e' l'unica stanza che nello
#     stesso giorno puo' essere prenotata da membri di team diversi.
#
#   Alcune note sul contenuto del file
#   - i record hanno un numero di elementi variabili
#   - Ogni utente (identificato univocamente da un id_utente) fa parte
#     di uno e un solo team.
#   - Ogni team ha uno e un solo team leader.
#     I team leader sono riconoscbili perche' hanno un
#     id_utente<20. Tutti gli utenti con id_utente<20 sono team leader.
#   - In una riunione organizzata in una stanza piccola (id_stanza >= 1) ...
#     * ... e' sempre presente il team leader del gruppo di lavoro.
#     * ... non sono necessariamente presenti tutti i membri del team.
#       Nel giorno della riunione i membri che non partecipano alla riunione
#       possono essere nell'open space o possono anche essere
#       assenti dal coworking.
#     * ... non devono essere riempiti tutti i posti disponibili.
#   - Se in un giorno un team non ha riunioni, il team leader
#     può essere nell'open space oppure può non essere presente nel coworking.
#
#   ***NOTA BENE***: cercate di aprire il file .csv:
#     - con un editor di testo diverso da notepad
#     - senza usare excel (o programmi similari)

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

cognome = 'Liu'  # inserisci qua il tuo cognome
nome = 'Weihao'  # inserisci qua il tuo nome


# - La funzione seguente accetta come parametro in ingresso
#   il nome del file .csv contenente i dati descritti in precedenza.
#   La funzione deve leggere il contenuto del file e
#   restituire una lista di liste, come nell'esempio seguente.
#        [
#          ['id_stanza1', data, id_utenteX, id_utenteY, ... id_utenteN],
#          ['id_stanza2', data, id_utenteH, id_utenteK, ... id_utenteW],
#          ...
#        ]
#   dove ogni lista interna contiene le informazioni presenti in un record del file.
#   Per esempio, la funzione applicata ad un file con il contenuto seguente
#      id_utente1;id_utente2;...;id_utenteN;giorno;id_stanza
#      34;59;166;155;58;72;154;168;236;214;180;04/01/2018;0
#      14;38;04/01/2018;1
#      ...
#   deve restituire una struttura dati come la seguente
#   [
#     [0, '04/01/2018', 34, 59, 166, 155, 58, 72, 154, 168, 236, 214, 180],
#     [1, 04/01/2018', 14, 38, 04],
#     ...
#   ]
#   In ogni lista interna, tutti i valori devono essere di tipo intero, ad eccezione
#   della data che deve essere di tipo stringa.
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
#   se in via provvisoria volete lavorare sulle funzioni successive senza
#   implementare l'attuale, potete utilizzare la struttura dati dichiarata
#   all'inizio di questo script (basta togliere il commento dalla prima riga di codice).
#   In quest'ultimo caso tuttavia la funzione sara' considerata non svolta.


def caricaDatiCoworking(fn):
    # return datiCoworking # se non riuscite ad implementare la funzione, potete usare temporaneamente questa struttura dati
    # Implementa il codice della funzione qua sotto. La riga con il pass puo' essere cancellata.
    file = open(fn, 'r')
    file.readline()
    li = []
    for line in file:
        line = line.strip('\n').strip('\r')
        item = line.split(';')
        id_stanza = int(item[-1])
        data = item[-2]
        temp_li = [id_stanza, data]
        for i in item[:-2]:
            temp_li.append(int(i))
        li.append(temp_li)
    return li

    # - La funzione costiUtilizzo accetta come parametri in ingresso la struttura dati
    #   restituita dalla funzione caricaDatiCoworking().
    #   La funzione seguente deve restituire un dizionario come nell'esempio seguente
    #        {
    #           id_Utente1:costo1, id_Utente2:costo2, ...
    #        }
    #   Dove ad ogni utente è associato il prezzo (costo) che l'utente deve corrispondere
    #   per l'affitto delle postazioni di lavoro, le cui prenotazioni sono contenute
    #   nella struttura dati ricevuta in ingresso.
    #   Il costo va calcolato nel modo seguente:
    #   - una giornata nell'open space costa 2 euro (a persona) id_stanza = 0
    #   - l'affitto di una sala piccola costa 60 euro a giornata e ==> id_stanza > 0
    #     la cifra va divisa in parti uguali tra tutte le persone che
    #     usufruiscono in tal giorno della stanza.
    #   - Nella struttura dati restituita, per ogni utente va indicata
    #     la somma dei costi dovuti per l'uso dell'open space e delle stanze piccole.
    #   Il tipo di costo1, costo2, ... può essere int o float, a vostra scelta.


def costiUtilizzo(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    di = {}
    for li in ds:
        id_stanza = li[0]
        count = 0
        for idCliente in li[2:]:
            if idCliente not in di:
                di[idCliente] = 0
            if id_stanza == 0:
                di[idCliente] += 2
            else:
                num_persone = len(li)-2
                di[idCliente] += 60/num_persone
    return di


# - La funzione seguente accetta come parametro in ingresso la struttura dati
#   restituita dalla funzione caricaDatiCoworking().
#   La funzione seguente deve restituire una struttura dati come la seguente:
#        {
#           id_macro_gruppo0:numero_utilizzi_stanze_piccole0,
#           id_macro_gruppo1:numero_utilizzi_stanze_piccole1,
#           id_macro_gruppo2:numero_utilizzi_stanze_piccole2,
#           ...
#           id_macro_gruppoN:numero_utilizzi_stanze_piccoleN,
#        }
#   Un macrogruppo è un insieme di persone. Data una persona,
#   è possibile individuare il macrogruppo di appartenenza
#   calcolando il resto della divisione intera tra l'id_utente e 20.
#   Quindi i valori di id_macro_gruppo sono i possibili resti della
#   divisione intera per 20, vale a dire i numeri da 0 a 19.
#   Con numero_utilizzi_stanze_piccole si intende il numero di volte che gli
#   utenti del macrogruppo hanno utilizzato una stanza piccola.
#   Ogni volta che una persona del macrogruppo prende posto in una stanza
#   piccola per un giorno, il numero di utilizzi associato al macrogruppo
#   deve essere incrementato di un'unità.
#   Se una stanza piccola è utilizzata da più persone, per ogni persona
#   deve essere conteggiato l'utilizzo della stanza nel macrogruppo di appartenenza.
def macroGruppi(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    di = {}
    for li in ds:
        id_stanza = li[0]
        for idCliente in li[2:]:
            id_macro = idCliente % 20
            if id_macro not in di and id_stanza > 0:
                di[id_macro] = 1
            if id_stanza > 0 and id_macro in di:
                di[id_macro] += 1
    return di


# - La funzione seguente accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiCoworking().
#   La funzione seguente deve restituire un dizionario come nell'esempio qua sotto
#        {
#         id_utente_team_leader1:[id_utente_membro1, id_utente_membro2, ... id_utente_membroN],
#         id_utente_team_leader2:[id_utente_membroX, id_utente_membroY, ... ],
#         ...,
#        }
#   La chiave di ogni coppia deve essere un utente team leader. Nella lista associata
#   alla chiave devono essere presenti gli id_utente di tutti i membri del team.
#   Nella lista, un membro deve essere presente una sola volta,
#   il team leader non deve essere presente nella lista.
#   Si ricorda che:
#   - Ogni utente può fare parte di uno e un solo team.
#   - Ogni team ha uno e un solo team leader
#     (tutte e solo le persone con id_utente<20 sono team leader).
#   - In una riunione organizzata in una stanza piccola (id_stanza >= 1),
#     * e' sempre presente il team leader
#     * non sono necessariamente presenti tutti i membri del team
#   - Nell'open space sono presenti persone di team diversi
def composizioneTeam(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    di = {}
    for li in ds:
        id_stanza = li[0]
        if id_stanza > 0:
            team_leader = 0
            id_membro = []
            for idCliente in li[2:]:
                if idCliente < 20:
                    team_leader = idCliente
                else:
                    id_membro.append(idCliente)

            if team_leader not in di:
                di[team_leader] = id_membro
            else:
                for ele in id_membro:
                    if ele not in di[team_leader]:
                        di[team_leader].append(ele)
    return di


##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################

print('Esercizio %s.' % (nomeEsercizio))
print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione caricaDatiCoworking: ')
fnv = 'Esame-uni/Documents/Esame uni/2020-09-17/copreno.csv'
dcw = caricaDatiCoworking(fnv)
print(dcw)

print('2) Eseguo la funzione costiUtilizzo: ')
f2d = costiUtilizzo(dcw)
print(f2d)

print('3) Eseguo la funzione macroGruppi: ')
f3d = macroGruppi(dcw)
print(f3d)

print("4) Eseguo la funzione composizioneTeam")
f4d = composizioneTeam(dcw)
print(f4d)

print('Nome file e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
