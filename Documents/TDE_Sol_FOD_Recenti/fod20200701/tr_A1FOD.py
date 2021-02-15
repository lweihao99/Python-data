
# 1.  Caricare il contenuto del file `viaggi.csv` nel dataframe `dfViaggi`,
# del.file `autostradaA1.tsv` nel dataframe `dfCaselli` e quello del
# del.file `costoKm.txt` nel dataframe `dfCosti`.


# 2. Calcolare il tempo di viaggio, differenza tra tempo di uscita e tempo
#   di ingresso e immagazzinarlo nella colonna `deltaT`.


# 3. Fondere in un nuovo dataframe `dfCompleto` il contenuto dei dataframe
# `dfViaggi` e `dfCaselli` ed aggiungervi una nuova colonna`deltaKm`
# contenente il valore in kilometri della distanza percorsa durante ciascun
# viaggio.
# Si consiglia di sfruttare l'associazione tra i codici dei caselli di
# ingresso e uscita `cIN` e `cOut` ed i valori per `CodiceCasello` nel
# dataframe `dfCaselli`per identificare il kilometro `#ProgressivaKm` a cui è
# situato ciascun casello.


# 4. Calcolare ed immagazzinare in una nuova colonna `pedaggio` del dataframe
# `dfCompleto` il pedaggio associato a ciascun viaggio. Il costo di ciascun
# viaggio si ottiene moltiplicando la lunghezza del viaggio `deltaKm` per il
# costo a chilometro associato alla categoria del veicolo `categoria`.
# Le informazioni sui costi al chilometro sono immagazzinate nel dataframe
# 'dfCosti'.


# 5.Individuare i veicoli che hanno tenuto una velocità media superiore ai
# 130 km/h.
# La velocità media si può ottenere dal rapporto tra la distanza percorsa in
# chilometri moltiplicata per il fattore di conversion 3600 e divisa per il
# tempo del viaggio (espresso in secondi) `deltaT`.


# 6. Costruire una nuova serie `sIncassoCategoria` che contenga l'incasso
# totale per ciascuna delle categorie di veicolo.


# 7.Riprodurre il seguente grafico e salvarlo in un file di tipo pdf.
# Il grafico rappresenta graficamente le informazioni relative alla serie
# `sIncassoCategoria`
