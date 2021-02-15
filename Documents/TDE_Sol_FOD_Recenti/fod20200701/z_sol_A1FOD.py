import pandas as pd
import matplotlib.pyplot as plt

# 1.  Caricare il contenuto del file `viaggi.csv` nel dataframe `dfViaggi`,
# del.file `autostradaA1.tsv` nel dataframe `dfCaselli` e quello del
# del.file `costoKm.txt` nel dataframe `dfCosti`.
dfViaggi = pd.read_csv('viaggi.csv', sep=':')
print(dfViaggi)
# dfViaggi.to_csv('tmpViaggi.csv')
dfCaselli = pd.read_csv('autostradaA1.tsv', sep='\t', header=1)
# print(dfCaselli.CodiceCasello.value_counts())
dfCosti = pd.read_csv('costoKm.txt', header=2)
print(dfCosti)

# 2. Calcolare il tempo di viaggio, differenza tra tempo di uscita e tempo
#   di ingresso e immagazzinarlo nella colonna `deltaT`.

dfViaggi['deltaT'] = dfViaggi['tOut'] - dfViaggi['tIn']
print(dfViaggi)


# 3. Fondere in un nuovo dataframe `dfCompleto` il contenuto dei dataframe
# `dfViaggi` e `dfCaselli` ed aggiungervi una nuova colonna`deltaKm`
# contenente il valore in kilometri della distanza percorsa durante ciascun
# viaggio.
# Si consiglia di sfruttare l'associazione tra i codici dei caselli di
# ingresso e uscita `cIN` e `cOut` ed i valori per `CodiceCasello` nel
# dataframe `dfCaselli`per identificare il kilometro `#ProgressivaKm` a cui è
# situato ciascun casello.

dfCompleto = pd.merge(dfViaggi, dfCaselli, left_on='cIn',
                      right_on='CodiceCasello', how='left')
dfCompleto.drop(columns=['NomeCasello', 'CodiceCasello'], inplace=True)
dfCompleto['kmIn'] = dfCompleto['#ProgressivaKm']
dfCompleto.drop(columns=['#ProgressivaKm'], inplace=True)
dfCompleto = pd.merge(dfCompleto, dfCaselli,
                      left_on='cOut', right_on='CodiceCasello')
dfCompleto['kmOut'] = dfCompleto['#ProgressivaKm']
dfCompleto.drop(columns=['NomeCasello', 'CodiceCasello',
                         '#ProgressivaKm'], inplace=True)
dfCompleto['deltaKm'] = (dfCompleto['kmIn'] - dfCompleto['kmOut']).abs()
print(dfCompleto)

# 4. Calcolare ed immagazzinare in una nuova colonna `pedaggio` del dataframe
# `dfCompleto` il pedaggio associato a ciascun viaggio. Il costo di ciascun
# viaggio si ottiene moltiplicando la lunghezza del viaggio `deltaKm` per il
# costo a chilometro associato alla categoria del veicolo `categoria`.
# Le informazioni sui costi al chilometro sono immagazzinate nel dataframe
# 'dfCosti'.

dfCompleto = pd.merge(dfCompleto, dfCosti,
                      left_on='categoria', right_on='#ClasseVeicolo')
dfCompleto.drop(columns=['#ClasseVeicolo'], inplace=True)
dfCompleto['pedaggio'] = dfCompleto['deltaKm'] * dfCompleto['euro/km']
print(dfCompleto)

# 5.Individuare i veicoli che hanno tenuto una velocità media superiore ai
# 130 km/h.
# La velocità media si può ottenere dal rapporto tra la distanza percorsa in
# chilometri moltiplicata per il fattore di conversion 3600 e divisa per il
# tempo del viaggio (espresso in secondi) `deltaT`.
dfCompleto['velMedia'] = (dfCompleto['deltaKm'] *
                          3600.0) / dfCompleto['deltaT']

dfIrregolari = dfCompleto[dfCompleto.velMedia > 130.0]
print(dfIrregolari)

# 6. Costruire una nuova serie `sIncassoCategoria` che contenga l'incasso
# totale per ciascuna delle categorie di veicolo.
dfViaggiCategoria = dfCompleto.groupby(by='categoria')
sIncassoCategoria = dfViaggiCategoria.pedaggio.sum()
print(sIncassoCategoria)

# 7.Riprodurre il seguente grafico e salvarlo in un file di tipo pdf.
# Il grafico rappresenta graficamente le informazioni relative alla serie
# `sIncassoCategoria`
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(sIncassoCategoria.index, sIncassoCategoria, label='', color='#377EB8')
ax.set_title('Incasso per categoria [Euro]')
plt.savefig('incassoCategoria.svg')
