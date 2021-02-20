##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e dei
# file dati, descritti qua di seguito
#
# - File 1) 'ParcoVeicoliCircolantiLombardia2018.csv'
#   Il file memorizza i dati raccolti del parco veicoli viaggianti in Lombardia.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
# PROG,USO,DESTINAZIONE,PORTATA,FLAG_ANN_MASSA_RIMORC,CILINDRATA,ALIMENTAZIONE,MASSA_RIMORCHIABILE,NUMERO_POSTI,TIPO_ALIMENTAZIONE_IMPIANTO,KW,DT_PRIMA_IMMATRICOLAZIONE,NUMERO_ASSI,COD_SIGLA_EURO,EMISSIONI_CO2,PESO_COMPLESSIVO,COD_ISTAT_COMUNE,COD_ISTAT_PROVINCIA
# 4607724,4,J,1000,A, , ,,, ,,1989,1,EURO0,0,1300,029,017
# 710077,0,A,0,,01570,B,,5,,0,,0,,,0,133,013
# 3292399,0,M,139,A,"600,00",B,0,2,,57,2000,2,EURO1,0,440,073,017
# 14536586,0,A,405,P,"1242,00",B,800,4,,51,2015,2,EURO6,1150,1345,216,016
# 7627294,0,M,125,A,01064,B,,2,,55,2006,2,EURO2,0,470,012,108
# 7375619,0,A,485,P,01242,B,900,4,,48,2006,2,EURO4,1400,1575,144,017
# 1792720,0,A,434,P,01968,G,1400,5,,103,2004,2,EURO4,1490,1910,029,017
# 3475439,0,A,475,P,01870,G,1300,5,,72,2000,2,EURO2,1570,1840,027,108
# 8812536,0,A,398,P,01124,B,920,5,,44.1,2007,2,EURO4,1400,1483,143,013
# ...
#   La prima riga contiene l'intestazione del file.
#   Nel file, per ogni veicolo/riga ci sono 18 colonne di cui segue l'indice,
#   il nome ed una breve descrizione:
#    0, PROG: numero Progressivo associato al veicolo
#    1, USO: Uso del veicolo
#    2, DESTINAZIONE: Tipologia del veicolo.
#    3, PORTATA: La portata del veicolo in Kg.
#    4, FLAG_ANN_MASSA_RIMORC: Flag indicante se il veicolo può rimorchiare o meno.
#    5, CILINDRATA: Numero della cilindrata del veicolo.
#    6, ALIMENTAZIONE: Tipo dell'alimentazione del veicolo.
#    7, MASSA_RIMORCHIABILE: La massa massima rimorchiabile in Kg.
#    8, NUMERO_POSTI: Numero di posti possibile del veicolo.
#    9, TIPO_ALIMENTAZIONE_IMPIANTO: Impianto di alimentazione se installato successivamente.
#   10, KW: Potenza Kilowatt del veicolo.
#   11, DT_PRIMA_IMMATRICOLAZIONE: Anno dell'immatricolazione del veicolo.
#   12, NUMERO_ASSI: Numero degli assi del veicolo.
#   13, COD_SIGLA_EURO: Classificazione euro del veicolo.
#   14, EMISSIONI_CO2: EMISSIONI_CO2 in gr/Km.
#   15, PESO_COMPLESSIVO: Peso complessivo del veicolo senza la portata in Kg.
#   16, COD_ISTAT_COMUNE: Codice Istat del comune d'appartenenza del veicolo lombardo.
#   17, COD_ISTAT_PROVINCIA: Codice Istat della provincia d'appartenenza del veicolo lombardo.
#
# - File 2) 'Elenco-comuni-italiani.csv'
#   Il file contiene le informazioni dettagliate per la classificazione ISTAT dei comuni d'italia.


import pandas as pd
import matplotlib.pyplot as plt


fileComuni = 'Documents/TDE_Sol_FOD_Recenti/fod20200131/Elenco-comuni-italiani.csv'
fileVeicoli = 'Documents/TDE_Sol_FOD_Recenti/fod20200131/ParcoVeicoliCircolantiLombardia2018.csv'

# 1. Caricare il contenuto del file Elenco-comuni-italiani.csv nel
# dataframe dfComuni, assicurandosi che la colonna 'Codice_Comune_formato_alfanumerico'
# sia di tipo stringa
dfComuni = pd.read_csv(fileComuni, sep=';', dtype={
                       'Codice_Comune_formato_alfanumerico': 'str'})
print(dfComuni)

# 2. Caricare il contenuto del file ParcoVeicoliCircolantiLombardia2018.csv nel
# dataframe dfVeicoli, assicurandosi che la colonna 'COD_ISTAT_PROVINCIA'
# sia di tipo stringa
dfVeicoli = pd.read_csv(fileVeicoli, dtype={'COD_ISTAT_PROVINCIA': 'str'})
print(dfVeicoli)
print(dfVeicoli.dtypes)

# 3.Aggiungere al dataframe dfVeicoli la colonna Codice_Comune_formato_alfanumerico
# composta dalla concatenazione dei valori contenuti nelle colonne
# COD_ISTAT_PROVINCIA e COD_ISTAT_COMUNE.
# Codice_Comune_formato_alfanumerico = COD_ISTAT_PROVINCIA + COD_ISTAT_COMUNE
dfVeicoli['Codice_Comune_formato_alfanumerico'] = \
    dfVeicoli.COD_ISTAT_PROVINCIA + dfVeicoli.COD_ISTAT_COMUNE

# 4.Fondere il contenuto dei due dataframe utilizzando i valori contenuti nella
# colonna Codice_Comune_formato_alfanumerico
# merge是用来融合数据的方法,
# 属性: on = 指定数据对齐合并的列,
#       how = 数据融合的方法 不指定的话默认使用inner也就是保留2个数据中一样的部分,outer保留所有信息,
#       right left分别保留右边 和 左边表的对应信息

dfMerged = pd.merge(dfVeicoli, dfComuni,
                    on='Codice_Comune_formato_alfanumerico',
                    how='inner')  # 这里就是要对齐dfVeicoli 以及 dfComuni,里的对应列Codice_comuni_formato_alfanumeri,并且取其共有的数据进行合并(inner)
print(dfMerged)
print(dfMerged.columns)  # 打印列表

# 5. Costruire il dataframe dfMergedMi contenente solo le osservazioni la cui
# denominazione è Milano
dfMergedMi = dfMerged[dfMerged.Denominazione_in_italiano == 'Milano']
print("______", dfMergedMi.shape)  # shape 只打印(行数,列数)

# 6.Costruire il dataframe dfMiEuro che contenga le osservazioni del dataframe
# dfMergedMi contente il conteggio delle osservazioni stratificate per
# 'COD_SIGLA_EURO'

dfMiEuro = dfMergedMi.groupby(
    by='COD_SIGLA_EURO').count()  # 以COD_SIGLA_EURO进行分组,并计数
print("=====", dfMiEuro.PROG)  # 这里取dfMiEuro 里的 prog列


# 7.Riprodurre il seguente grafico e salvarlo in un file di tipo pdf
y = range(len(dfMiEuro.PROG))
fig = plt.figure()  # 设置图片大小,可以通过figsize设置大小,以及dpi
ax = fig.add_subplot(111)  # 同subplot用来设置子图,比如subplot(2,2,1)将话不分为两行两列,并对1话不进行绘制
ax.barh(y, dfMiEuro.PROG, label='sigla euro',
        color='#377EB8')  # 同bar用来绘制柱状图,barh是用来绘制横向条形图,所以x对应Y,y对应x

ax.set_yticklabels(dfMiEuro.index)  # y轴信息
ax.set_yticks(y)  # y轴刻度
ax.set_title('Distribuzione su classe Euro')
# plt.savefig('distribEuroMI.png') # 对图片进行保存
plt.show()
