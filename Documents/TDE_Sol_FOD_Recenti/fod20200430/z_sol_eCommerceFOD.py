import pandas as pd
import matplotlib.pyplot as plt

# 1. Caricare il file dei carrelli virtuali
dfEComm = pd.read_csv('cartFOD.csv', sep=';')

print(dfEComm.head(15))
print(dfEComm.shape)

# 2. Caricare il file con la descrizione dei prodotti
dfProdotti = pd.read_csv('itemsFOD.tsv', sep='\t')
print(dfProdotti.head(15))
print(dfProdotti.shape)


# 3.Fondere il contenuto dei due dataframe utilizzando i valori contenuti nella
# colonna ID. Il dataframe ottenuto deve contenere solo i valori presenti in
# entrambi i dataframe di partenza.
dfMerged = pd.merge(dfEComm, dfProdotti,
                    right_on='ID', left_on='ID_PRODUCT',
                    how='inner')
print(dfMerged)
print(dfMerged.columns)
print(dfMerged.head(15))

# 4. Verificare che il dataframe contenga solo righe associate a operazioni di
# 'ADD' e 'DROP' e non di 'CHECKOUT'
print(dfMerged.OPERATION.unique())
print(dfMerged[dfMerged.OPERATION == 'CHECKOUT'].TIME.count())  # alternativa

# 5. Calcolare l'incasso complessivo comprensivo di tutti gli acquisti
#   effettuati.
mask = dfMerged.OPERATION == 'DROP'
dfMerged.loc[mask, 'QUANTITY'] *= -1
dfMerged['singoloAcquisto'] = dfMerged.QUANTITY * dfMerged.UNIT_SALE_PRICE
grandTotal = dfMerged.singoloAcquisto.sum()
print('grandTotal', grandTotal)

# 6. Calcolare la spesa media effettuata dai clienti (media del totale
# acquistato da ciascun cliente)
spesaCliente = dfMerged.groupby(by='CUSTOMER').singoloAcquisto.sum()
print(spesaCliente)
spesaMedia = spesaCliente.mean()
print('spesaMedia', spesaMedia)


# 7. Riprodurre il seguente grafico e salvarlo in un file di tipo pdf
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dfMerged.UNIT_SALE_PRICE, dfMerged.QUANTITY.abs(),
           label='item', color='#377EB8')
# ax.set_yticklabels(dfMiEuro.index)
# ax.set_yticks(y)
ax.set_xlabel('Prezzo vendita singolo oggetto')
ax.set_ylabel('Quantità acquistatata')
ax.set_title('Correlazione Prezzo / quantità')
plt.savefig('corrPriceQuantity.svg')
