import pandas as pd
import matplotlib as plot

# 1. Caricare il contenuto del file Elenco-comuni-italiani.csv nel
# dataframe dfComuni, assicurandosi che le colonne siano caricate
# con tipo stringa
file = pd.read_csv(
    'Elenco-comuni-italiani.csv', sep=';'
)

dfComuni = pd.DataFrame(file)


print(dfComuni)

# 2. Caricare il contenuto del file trafficoAereo2017.csv nel
# dataframe dfTrafficoAereo2017.
file2 = pd.read_csv('trafficoAereo2017.csv', sep=';')
dfTrafficoAereo2017 = pd.DataFrame(file2)
print(dfTrafficoAereo2017)

# 3. Verificare che il valore associato al numero di passeggeri Internazionali e Nazionali di Linea e Charter
# di ciascuno scalo sia pari alla somma dei valori associati al numero di passeggeri di voli Internazionali e Nazionali di Linea
# e dei valori associati al numero di passeggeri di voli Internazionali e Nazionali Charter


# 4. Costruire un nuovo dataframe che contenga solo le righe associate agli aeroporti
# per i quali il numero di passeggeri di voli internazionali è maggiore di quello dei
# voli nazionali sia di Linea che Charter. Il datframe deve contenere le sole colonne
# 'ComuneRif', 'NomeAeroporto', 'Pass_I_LeC' e 'Pass_N_LeC'.
newData = pd.DataFrame({'ComuneRif': dfTrafficoAereo2017['ComuneRif'],
                        'NomeAeroporto': dfTrafficoAereo2017['NomeAeroporto'],
                        'Pass_I_LeC': dfTrafficoAereo2017['Pass_I_LeC'],
                        'Pass_N_LeC': dfTrafficoAereo2017['Pass_N_LeC']})

print(newData)

# 5.Fondere il contenuto dei dataframe dfTrafficoAereo2017 e dfComuni utilizzando i valori contenuti nelle
# colonne ComuneRif e Denominazione_in_italiano. Il nuovo dataframe si deve chiamare dfTraAereo.\
di = {'ComuneRif': dfTrafficoAereo2017['ComuneRif'],
      'Denominazione_in_italiano': dfComuni['Denominazione_in_italiano']}
dfTraAereo = pd.DataFrame(di)
print(dfTraAereo)

# 6. Sfruttando il dataframe dfTrAereo, individuare quale sia la regione i cui scali hanno
# globalmente ospitato il maggior numero di passeggeri di voli Internazionali e Nazionali,
# sia di Linea che Charter, ed indicare quale sia questo valore.


# 7.Riprodurre il seguente grafico e salvarlo in un file di tipo pdf
# Il grafico ha per dimensioni le variabili Ton_I_LeC, .Pass_I_LeC e Ton_N_LeC, .Pass_N_LeC
x1 = dfTrafficoAereo2017['Ton_I_LeC']
y1 = dfTrafficoAereo2017['Pass_I_LeC']

x2 = dfTrafficoAereo2017['Ton_N_LeC']
y2 = dfTrafficoAereo2017['Pass_N_LeC']
# fare il grafico

plot.show()
