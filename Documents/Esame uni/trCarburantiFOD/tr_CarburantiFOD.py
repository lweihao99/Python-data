import pandas as pd

# 1.  Caricare il contenuto del file `anagrafica.csv` nel dataframe
# `dfAnagrafica` e del file `prezzi.csv` nel dataframe `dfPrezzi`.
file = 'Documents/Esame uni/trCarburantiFOD/anagrafica.csv'
dfAnagrafica = pd.read_csv(file, sep=';')
file2 = 'Documents/Esame uni/trCarburantiFOD/prezzi.csv'
dfPrezzi = pd.read_csv(file2, sep=';')
print(dfAnagrafica)
print(dfPrezzi)


# 2. Costruire, a partire dal dataframe 'dfAnagrafica' un nuovo dataframe
# `dfAnagraficaMB` che contenga tutti e soli i record associati alla Provincia
# di Monza Brianza (`MB`), e se ne esegua il conteggio.
dfAnagraficaMB = dfAnagrafica[dfAnagrafica.Provincia == 'MB']
count = dfAnagraficaMB['Provincia'].count()

print(dfAnagraficaMB)
print('conteggio = ', count)


# 3. Fondere in un nuovo dataframe `dfCompleto` il contenuto dei dataframe
# `dfAnagraficaMB` e `dfPrezzi` contente tutti e soli i record presenti in
# entrambi i dataframe.
dfCompleto = pd.merge(dfAnagraficaMB, dfPrezzi, how='inner')
print(dfCompleto)

# 4. A partire dal dataframe `dfCompleto`, costruire un nuovo dataFrame `dfLite`
# che includa le sole colonne `['idImpianto', 'giorno', 'Bandiera',
# 'descCarburante', 'prezzo']` e i cui record siano associati al solo servizio
# self-service (usare variabile 'isSelf').
# Verificare, inoltre, la presenza delle sole colonne indicate.


# 5. A partire dal dataframe `dflite` costruire quattro nuovi dataframe che
# contengano la media giornaliera del prezzo dei due carburanti, `Gasolio` e
# `Benzina`, erogati dai distributori liberi (variabile `Bandiera` pari a
# `Pompe Bianche`) o dai restanti distributori.


# 6.Riprodurre il seguente grafico e salvarlo in un file di tipo pdf.
# Il grafico rappresenta graficamente le informazioni relative ai valori
# dei prezzi del carburante per *Bianche Gasolio*, *Bianche Benzina*,
# *Altre Gasolio* e *Altre Benzina*.
