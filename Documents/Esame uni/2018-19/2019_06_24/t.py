def caricaDatiAppartamenti(fn):
    # return datiAppartamenti # se non riuscite ad implementare la funzione, potete usare temporaneamente qs dati
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    file = open(fn, 'r')
    li = []
    for i in file:
        i = i.strip('\n').strip('\r')
        temp = i.split(';')
        # print(temp)
        for item in temp:
            new_temp = item.split('=')
            print(new_temp)
            # print(item)


caricaDatiAppartamenti(
    'Esame-uni/Documents/Esame uni/2018-19/2019_06_24/appartamenti.csv')
