import pandas as pd
import matplotlib.pyplot as plt

# 1. Unire i 5 file in un unico dataframe
lFiles = []
for i in range(0, 5):
    lFiles.append('pubmedCoV' + str(i) + '.csv')
print(lFiles)

dizDFs = {}  # si può fare anche con una lista
for fileName in lFiles:
    dfTmp = pd.read_csv(fileName, sep='\t', dtype={'PMID': 'str'})
    dizDFs[fileName] = dfTmp
dfCoV = pd.concat(dizDFs)
dfCoV = dfCoV.reset_index(drop=True)

print(dfCoV.head())
print(dfCoV.shape)
print(dfCoV.dtypes)
# PMID        object
# title       object
# date        object
# location    object
# doi         object

# 2. Aggiungere una colonna 'year' che contenga l'anno estratto dal campo 'date'
dfCoV['year'] = dfCoV['date'].str[:4]
print(dfCoV['year'])

# 3. Calcolare il numero medio di pubblicazioni per anno
print('numero medio di pubblicazioni per anno')
dfCoVCountYear = dfCoV.groupby(by='year')['PMID'].count()
print(dfCoVCountYear.mean())

# 4. Costruire un dataframe che contenga le sole pubblicazioni stilate in Italia
# 'Italy'
mask = (dfCoV['location'] == 'Italy')
dfCovItaly = dfCoV[mask]
print(dfCovItaly)

# 5. Identificare l'anno con più pubblicazioni
maxPubs = dfCoVCountYear.max()
print(dfCoVCountYear[dfCoVCountYear == maxPubs])

# 6. Riprodurre il seguente grafico
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(dfCoVCountYear, 'o-')
ax.set_title('Pubblicazioni per anno')
plt.savefig('distribPubAnno.svg')
