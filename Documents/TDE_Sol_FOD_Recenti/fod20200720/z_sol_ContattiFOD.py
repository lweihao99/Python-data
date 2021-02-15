import pandas as pd
import matplotlib.pyplot as plt


# 1.  Caricare il contenuto del file `contattiSettimana7.txt` nel dataframe
# `dfPrimaSettimana` e del file `contattiSettimana7.txt` nel dataframe
# `contattiSettimana8.txt`.
dfPrimaSettimana = pd.read_csv('contattiSettimana7.txt', sep='#', header=1)
dfSecondaSettimana = pd.read_csv('contattiSettimana8.txt', sep='#', header=1)

print(dfPrimaSettimana.head())
print(dfSecondaSettimana.head())

print(dfPrimaSettimana.shape)
print(dfSecondaSettimana.shape)


# 2. Allineare il tempo registrato nel dataframe associato alla seconda
# settimana `dfSecondaSettimana` sapendo che
#  * la settimana 8 è successiva alla 7
#  * una settimana ha 10080 minuti.
dfSecondaSettimana.time += 10080
print(dfSecondaSettimana.head())


# 3. Fondere in un nuovo dataframe `dfCompleto` il contenuto dei dataframe
# `dfPrimaSettimana` e `dfSecondaSettimana` contente tutti i record di entrambe
# le settimane gli uni dopo gli altri.
dfCompleto = pd.concat([dfPrimaSettimana, dfSecondaSettimana])
print(dfCompleto.shape)
# print(dfCompleto.head())


# 4. Inviduare in quale momento ('time') si è verificato il maggior numero di
# contatti e quanti siano stati. Si consiglia di sfruttare le funzioni di
#  pandas `idxmax()` ed `max()`.
dfConteggi = dfCompleto.groupby(by='time').count()
# print(dfConteggi)
quando = dfConteggi.UID1.idxmax()
quanti = dfConteggi.UID1.max()
print(quando, quanti)


# 5. Estrarre gli identificativi unici dei presenti al momento del contatto
# identificato al punto precedente ('time = 15930').
# Si ricorda, se necessario, che è possibile concatenare 2 serie tramite il
# metodo di pandas `s1.append(s2)`.
dfMaxContatto = dfCompleto[dfCompleto.time == quando]
sUID1 = dfMaxContatto.UID1
sUID2 = dfMaxContatto.UID2
sUID = sUID1.append(sUID2).unique()
print(len(sUID), sUID)


# 6. Identificare tuti gli `UID` (identificativi unici) che hanno avuto
#  contatto con l'`UID` `u_472` dopo il minuto 8000
dfDopo = dfCompleto[dfCompleto.time >= 8000]
print(dfDopo)
dfDopoUID1 = dfDopo[dfDopo.UID1 == 'u_472']
sContatti1 = dfDopoUID1.UID2
print(dfDopoUID1)
dfDopoUID2 = dfDopo[dfDopo.UID2 == 'u_472']
sContatti2 = dfDopoUID2.UID1
print(dfDopoUID2)
sContatti = sContatti1.append(sContatti2).unique()
print(sContatti)


# 7.Riprodurre il seguente grafico e salvarlo in un file di tipo pdf.
# Il grafico rappresenta graficamente le informazioni relative al conteggio dei
# contatti nel tempo.
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(dfConteggi.index, dfConteggi, label='', color='#377EB8')
ax.set_title('Andamento del numero di contatti')
ax.set_xlabel('tempo [min]')
ax.set_ylabel('numero contatti')
plt.savefig('dinamicaContatti.svg')
