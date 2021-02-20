import pandas as pd
import matplotlib.pyplot as plt

# 1. Unire i 5 file in un unico dataframe
lFiles = []  # 设一个空列表用来存放csv文件从1倒5
for i in range(0, 5):
    lFiles.append(
        'Documents/TDE_Sol_FOD_Recenti/fod20200220/pubmedCoV' + str(i) + '.csv')
print(lFiles)

dizDFs = {}  # si può fare anche con una lista
for fileName in lFiles:  # 遍历列表里的文件名
    # filename是遍历出来的csv文件名(1-5),分隔方式使\t也就是tab,文件里带有'PMID'格式为str
    dfTmp = pd.read_csv(fileName, sep='\t', dtype={'PMID': 'str'})
    dizDFs[fileName] = dfTmp  # 字典里的key使csv文件名,每个文件名的value是文件里的内容
# concat是用来合并不同表格的指令,默认axis=0也就是纵向合并,axis=-1横向合并,可以定义keys来建立层次化索引
dfCoV = pd.concat(dizDFs)
dfCoV = dfCoV.reset_index(drop=True)  # reset_index用来还原索引,从新变为默认的整形索引
# set_index用来设置单索引,复合索引,也就是原先一列或多列元素转化为索引

print(dfCoV.head())  # head(n)用来显示前n行数据,不指定n的话就是显示所有数据
print(dfCoV.shape)  # 输出对象的轴纬度 与ndarray一致,比如shape[0]返回行数,shape[1]返回列数
print(dfCoV.dtypes)  # 返回数据类型
# PMID        object
# title       object
# date        object
# location    object
# doi         object

# 2. Aggiungere una colonna 'year' che contenga l'anno estratto dal campo 'date'
dfCoV['year'] = dfCoV['date'].str[:4]  # 开始的4个字符是年数
print(dfCoV['year'])

# 3. Calcolare il numero medio di pubblicazioni per anno
print('numero medio di pubblicazioni per anno')
# groupby是对元素进行分组并对PMID进行索引并对数量进行统计,这里是以年数来进行分组,比如2020的就分在一起
dfCoVCountYear = dfCoV.groupby(by='year')['PMID'].count()
print(dfCoVCountYear.mean())  # mean()函数返回所求轴的平均值 默认axis=none

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
