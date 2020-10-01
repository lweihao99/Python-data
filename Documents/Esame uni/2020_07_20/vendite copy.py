# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'venditeImmobili'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituita da una delle funzioni seguenti,
# La (vera) struttura dati caricata dal file sara' più lunga,
# i primi elementi di entrambe possono essere diversi.
# OVVIAMENTE, se non implementerete la funzione di lettura da file,
# quest'ultima sara' considerata non svolta

datiImmobili = [
    ('pubblicazione', '2010_03_01', 71, 'DONN', 150, 1553), ('rimozione', '2010_04_21', 71), ('catasto', '2010_10_19', 7746, 'DONN', 150, 1692), ('pubblicazione', '2010_01_01', 39, 'DHML', 50, 3081), ('pubblicazione', '2010_01_02', 70, 'BOVO', 90, 5848), ('pubblicazione', '2010_01_06', 34, 'BMIG', 300, 6802), ('pubblicazione', '2010_01_06', 49, 'GIMS', 90, 5486), ('pubblicazione', '2010_01_06', 80, 'DTMV', 90, 7133), ('pubblicazione', '2010_01_07', 90, 'ADHJ', 150, 5178), ('pubblicazione', '2010_01_07', 93, 'FLBB', 90, 1507), ('pubblicazione', '2010_01_14', 11, 'ABEF', 150, 8388), ('pubblicazione', '2010_01_15', 79, 'FDDK', 90, 3121), ('pubblicazione', '2010_01_16', 8, 'CBTI', 90, 2276), ('pubblicazione', '2010_01_16', 15, 'EPMF', 100, 6673), ('pubblicazione', '2010_01_18', 68, 'DGOQ', 50, 5544), ('rimozione', '2010_01_19', 70), ('pubblicazione', '2010_01_20', 47, 'DAEP', 100, 7791), ('pubblicazione', '2010_01_24', 0, 'EMHW', 90, 2893), ('pubblicazione', '2010_01_26', 50, 'CLWQ', 120, 9887), ('pubblicazione', '2010_01_29', 53, 'DEER', 200, 8248), ('pubblicazione', '2010_01_30', 33, 'ERWP', 150, 7731), ('pubblicazione', '2010_01_31', 1, 'CAON', 90, 5178), ('pubblicazione', '2010_01_31', 89, 'CHOU', 120, 3954), ('pubblicazione', '2010_02_01', 14, 'CBIP', 120, 4273), ('pubblicazione', '2010_02_03', 19, 'CFOR', 120, 8813), ('pubblicazione', '2010_02_04', 23, 'CCVE', 200, 4197), ('pubblicazione', '2010_02_05', 84, 'APXC', 150, 3379), ('pubblicazione', '2010_02_06', 66, 'FMNC', 150, 6840), ('rimozione', '2010_02_06', 49), ('pubblicazione', '2010_02_07', 92, 'DUHY', 200, 5891), ('pubblicazione', '2010_02_08', 85, 'BAJQ', 50, 6940), ('pubblicazione', '2010_02_09', 44, 'EBCK', 300, 7654), ('pubblicazione', '2010_02_12', 35, 'CJST', 300, 7486), ('pubblicazione', '2010_02_14', 16, 'CRSB', 50, 9426), ('pubblicazione', '2010_02_14', 18, 'BDVE', 180, 1987), ('pubblicazione', '2010_02_15', 31, 'DLRR', 50, 1018), ('rimozione', '2010_02_15', 85), ('pubblicazione', '2010_02_16', 24, 'DQAK', 120, 3762), ('pubblicazione', '2010_02_16', 36, 'GCRW', 100, 8180), ('pubblicazione', '2010_02_16', 57, 'DGEB', 300, 8790), ('rimozione', '2010_02_16', 79), ('pubblicazione', '2010_02_19', 42, 'BYWW', 50, 8420), ('pubblicazione', '2010_02_19', 94, 'DXCD', 90, 4657), ('pubblicazione', '2010_02_20', 17, 'AUTF', 100, 9368), ('pubblicazione', '2010_02_20', 29, 'FUKE', 90, 4916), ('pubblicazione', '2010_02_20', 62, 'AGYM', 200, 1119), ('rimozione', '2010_02_24', 92), ('pubblicazione', '2010_02_25', 51, 'CATY', 120, 4464), ('pubblicazione', '2010_02_26', 41, 'ATEO', 50, 3121), ('pubblicazione', '2010_02_28', 73, 'FGVO', 50, 9208), ('rimozione', '2010_02_28', 15), ('rimozione', '2010_02_28', 23), ('rimozione', '2010_03_03', 0), ('pubblicazione', '2010_03_04', 13, 'EDNK', 120, 4718), ('rimozione', '2010_03_04', 50), ('pubblicazione', '2010_03_06', 74, 'BCXD', 150, 7722), ('pubblicazione', '2010_03_08', 10, 'FLTK', 180, 7009), ('catasto', '2010_03_09', 7642, 'EPMF', 100, 6873), ('pubblicazione', '2010_03_09', 81, 'AFXS', 90, 1158), ('rimozione', '2010_03_09', 31), ('catasto', '2010_03_12', 5492, 'CCVE', 200, 4700), ('rimozione', '2010_03_12', 29), ('pubblicazione', '2010_03_13', 46, 'BMVT', 50, 7604), ('rimozione', '2010_03_16', 68), ('rimozione', '2010_03_17', 84), ('pubblicazione', '2010_03_18', 9, 'CRUD', 200, 1543), ('pubblicazione', '2010_03_21', 45, 'CNHD', 120, 4810), ('pubblicazione', '2010_03_21', 87, 'FTCA', 300, 8632), ('pubblicazione', '2010_03_22', 95, 'DPAV', 150, 9222), ('rimozione', '2010_03_23', 16), ('rimozione', '2010_03_23', 73), ('catasto', '2010_03_24', 838, 'BOVO', 90, 6666), ('pubblicazione', '2010_03_24', 38, 'EVAW', 100, 6826), ('pubblicazione', '2010_03_24', 40, 'GJUN', 50, 8880), ('rimozione', '2010_03_24', 8), ('pubblicazione', '2010_03_26', 58, 'GHUO', 100, 7802), ('pubblicazione', '2010_03_29', 4, 'CFUJ', 100, 9542), ('pubblicazione', '2010_03_30', 6, 'ANXT', 100, 5275), ('pubblicazione', '2010_04_01', 76, 'AMUX', 100, 2185), ('pubblicazione', '2010_04_01', 99, 'BPKQ', 100, 2066), ('pubblicazione', '2010_04_02', 61, 'CEPI', 180, 8963), ('rimozione', '2010_04_02', 89), ('pubblicazione', '2010_04_03', 98, 'FLBM', 150, 8626), ('pubblicazione', '2010_04_04', 88, 'BWGJ', 50, 5651), ('pubblicazione', '2010_04_05', 56, 'AHOT', 100, 8615), ('rimozione', '2010_04_06', 4), ('pubblicazione', '2010_04_09', 75, 'CWKC', 200, 4896), ('rimozione', '2010_04_09', 6), ('rimozione', '2010_04_17', 18), ('catasto', '2010_04_20', 8994, 'EMHW', 90, 2979), ('pubblicazione', '2010_04_21', 72, 'BMRJ', 100, 7798), ('catasto', '2010_04_22', 6532, 'GIMS', 90, 5979), ('pubblicazione', '2010_04_22', 59, 'DKMA', 120, 2477), ('pubblicazione', '2010_04_22', 96, 'APTG', 50, 7880), ('rimozione', '2010_04_22', 38), ('rimozione', '2010_04_23', 13), ('rimozione', '2010_04_24', 75), ('rimozione', '2010_04_25', 39), ('pubblicazione', '2010_04_28', 43, 'BYRU', 90, 2739), ('pubblicazione', '2010_04_28', 78, 'EMDB', 120, 5255), ('rimozione', '2010_05_01', 35), ('catasto', '2010_05_04', 4232, 'BAJQ', 50, 7287), ('rimozione', '2010_05_05', 10), ('pubblicazione', '2010_05_06', 5, 'FQIN', 180, 1462), ('pubblicazione', '2010_05_09', 86, 'EHNK', 150, 3079), ('pubblicazione', '2010_05_10', 48, 'BGOI', 100, 8695), ('rimozione', '2010_05_10', 56), ('pubblicazione', '2010_05_11', 37, 'DTIK', 150, 4361), ('pubblicazione', '2010_05_11', 54, 'FJQD', 50, 3592), ('rimozione', '2010_05_11', 72), ('rimozione', '2010_05_11', 94), ('pubblicazione', '2010_05_13', 3, 'FYCK', 180, 2792), ('pubblicazione', '2010_05_13', 28, 'ECWD', 150, 4976), ('pubblicazione', '2010_05_13', 67, 'DVHM', 90, 4778), ('rimozione', '2010_05_14', 47), ('pubblicazione', '2010_05_16', 32, 'EUAL', 100, 8900), ('rimozione', '2010_05_17', 74), ('rimozione', '2010_05_18', 78), ('rimozione', '2010_05_19', 5), ('rimozione', '2010_05_19', 76), ('pubblicazione', '2010_05_20', 60, 'DQOX', 150, 1802), ('pubblicazione', '2010_05_21', 82, 'CWNL', 120, 2128), ('rimozione', '2010_05_22', 32), ('rimozione', '2010_05_24', 45), ('rimozione', '2010_05_27', 58), ('catasto', '2010_05_31', 1126, 'FQIN', 180, 1330), ('rimozione', '2010_05_31', 60), ('rimozione', '2010_06_02', 44), ('rimozione', '2010_06_04', 57), ('pubblicazione', '2010_06_05', 91, 'CCGS', 180, 9960), ('catasto', '2010_06_07', 4847, 'DGEB', 300, 9229), ('catasto', '2010_06_08', 2860, 'AHOT', 100, 9734), ('pubblicazione', '2010_06_08', 65, 'DWUJ', 180, 6782), ('rimozione', '2010_06_09', 87), ('catasto', '2010_06_10', 6692, 'CFUJ', 100, 10019), ('catasto', '2010_06_11', 7175, 'GHUO', 100, 8894), ('pubblicazione', '2010_06_11', 69, 'APDM', 150, 5955), ('pubblicazione', '2010_06_15', 2, 'BDRN', 300, 3135), ('pubblicazione', '2010_06_18', 77, 'EQCV', 100, 6462), ('pubblicazione', '2010_06_19', 12, 'CJEA', 200, 4133), ('pubblicazione', '2010_06_20', 7, 'BOBC', 150, 2945), ('catasto', '2010_06_22', 7917, 'ANXT', 100, 5380), ('rimozione', '2010_06_22', 46), ('pubblicazione', '2010_06_24', 52, 'CBCS', 100, 4202), ('rimozione', '2010_06_27',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       43), ('rimozione', '2010_06_27', 62), ('pubblicazione', '2010_06_30', 26, 'BQXQ', 150, 2496), ('pubblicazione', '2010_06_30', 63, 'CVIM', 180, 7546), ('pubblicazione', '2010_06_30', 64, 'CNME', 100, 1006), ('rimozione', '2010_07_01', 80), ('rimozione', '2010_07_02', 41), ('catasto', '2010_07_03', 522, 'CWKC', 200, 4700), ('catasto', '2010_07_04', 2190, 'DUHY', 200, 6126), ('rimozione', '2010_07_04', 1), ('rimozione', '2010_07_04', 99), ('pubblicazione', '2010_07_06', 20, 'FWBY', 90, 3415), ('catasto', '2010_07_08', 3469, 'FTCA', 300, 8373), ('rimozione', '2010_07_09', 63), ('rimozione', '2010_07_10', 17), ('catasto', '2010_07_11', 6005, 'EBCK', 300, 8266), ('pubblicazione', '2010_07_11', 27, 'APYR', 300, 7702), ('rimozione', '2010_07_14', 61), ('rimozione', '2010_07_14', 65), ('rimozione', '2010_07_15', 53), ('rimozione', '2010_07_15', 66), ('catasto', '2010_07_16', 3104, 'CJST', 300, 7935), ('rimozione', '2010_07_17', 54), ('rimozione', '2010_07_18', 7), ('catasto', '2010_07_19', 6911, 'BCXD', 150, 7027), ('rimozione', '2010_07_20', 51), ('rimozione', '2010_07_21', 82), ('catasto', '2010_07_24', 5630, 'BDVE', 180, 2126), ('pubblicazione', '2010_07_24', 21, 'DAXP', 50, 8101), ('rimozione', '2010_07_24', 9), ('rimozione', '2010_07_25', 81), ('catasto', '2010_07_27', 3552, 'BYRU', 90, 2739), ('rimozione', '2010_07_27', 77), ('rimozione', '2010_07_29', 40), ('rimozione', '2010_07_29', 69), ('catasto', '2010_07_30', 2613, 'GJUN', 50, 8702), ('rimozione', '2010_07_30', 34), ('catasto', '2010_07_31', 9580, 'CWNL', 120, 2128), ('catasto', '2010_08_01', 1965, 'FDDK', 90, 2996), ('rimozione', '2010_08_07', 96), ('catasto', '2010_08_10', 915, 'EQCV', 100, 6203), ('catasto', '2010_08_12', 4120, 'EMDB', 120, 5360), ('rimozione', '2010_08_14', 26), ('rimozione', '2010_08_15', 3), ('rimozione', '2010_08_17', 28), ('catasto', '2010_08_18', 9712, 'CATY', 120, 5356), ('rimozione', '2010_08_18', 95), ('catasto', '2010_08_23', 9768, 'BMIG', 300, 6461), ('pubblicazione', '2010_08_23', 97, 'CGVD', 180, 8182), ('catasto', '2010_08_24', 1222, 'CLWQ', 120, 10480), ('catasto', '2010_08_25', 3160, 'EUAL', 100, 9879), ('catasto', '2010_08_25', 3454, 'BOBC', 150, 3445), ('rimozione', '2010_08_25', 33), ('rimozione', '2010_08_25', 93), ('rimozione', '2010_08_26', 64), ('rimozione', '2010_08_28', 48), ('rimozione', '2010_08_28', 52), ('catasto', '2010_09_01', 4815, 'APXC', 150, 3379), ('catasto', '2010_09_02', 2559, 'CVIM', 180, 8526), ('rimozione', '2010_09_02', 19), ('catasto', '2010_09_04', 602, 'BMVT', 50, 7223), ('catasto', '2010_09_08', 1340, 'DGOQ', 50, 5433), ('pubblicazione', '2010_09_08', 22, 'EUXJ', 120, 1343), ('pubblicazione', '2010_09_17', 30, 'EXMU', 120, 3919), ('rimozione', '2010_09_17', 2), ('rimozione', '2010_09_17', 27), ('rimozione', '2010_09_17', 91), ('catasto', '2010_09_19', 7879, 'APYR', 300, 8241), ('catasto', '2010_09_20', 6435, 'CCGS', 180, 10258), ('catasto', '2010_09_21', 8519, 'AFXS', 90, 1250), ('pubblicazione', '2010_09_21', 83, 'CFXG', 180, 5566), ('rimozione', '2010_09_21', 98), ('catasto', '2010_09_22', 4506, 'CFOR', 120, 10046), ('pubblicazione', '2010_09_22', 25, 'EHJH', 180, 9138), ('rimozione', '2010_09_22', 59), ('rimozione', '2010_09_24', 24), ('catasto', '2010_09_26', 5333, 'BQXQ', 150, 2995), ('rimozione', '2010_09_30', 42), ('catasto', '2010_10_02', 2464, 'CEPI', 180, 9142), ('pubblicazione', '2010_10_03', 55, 'DYXS', 50, 3287), ('rimozione', '2010_10_04', 14), ('catasto', '2010_10_05', 8881, 'CBCS', 100, 3907), ('catasto', '2010_10_07', 3853, 'DLRR', 50, 1201), ('catasto', '2010_10_07', 4183, 'FLBB', 90, 1537), ('catasto', '2010_10_07', 5344, 'CBTI', 90, 2708), ('catasto', '2010_10_08', 5091, 'BGOI', 100, 9912), ('catasto', '2010_10_08', 8163, 'DPAV', 150, 8484), ('rimozione', '2010_10_13', 86), ('catasto', '2010_10_19', 3313, 'DTMV', 90, 7204), ('catasto', '2010_10_19', 5379, 'CAON', 90, 5022), ('rimozione', '2010_10_19', 22), ('catasto', '2010_10_23', 9086, 'FUKE', 90, 5063), ('rimozione', '2010_10_23', 36), ('catasto', '2010_10_24', 4264, 'ATEO', 50, 2902), ('catasto', '2010_10_25', 1281, 'EDNK', 120, 4906), ('catasto', '2010_10_25', 9330, 'FGVO', 50, 8471), ('catasto', '2010_10_26', 1360, 'CBIP', 120, 5042), ('catasto', '2010_10_26', 8237, 'DQOX', 150, 1856), ('catasto', '2010_10_27', 3221, 'BMRJ', 100, 7875), ('catasto', '2010_10_27', 9004, 'EHNK', 150, 3356), ('catasto', '2010_10_29', 6638, 'FJQD', 50, 3448), ('catasto', '2010_10_30', 162, 'ECWD', 150, 5075), ('catasto', '2010_10_30', 503, 'DEER', 200, 8990), ('catasto', '2010_10_30', 4715, 'BYWW', 50, 7662), ('catasto', '2010_10_31', 7399, 'AUTF', 100, 11054), ('rimozione', '2010_11_01', 25), ('catasto', '2010_11_04', 7403, 'CNME', 100, 1046), ('rimozione', '2010_11_05', 30), ('catasto', '2010_11_08', 8387, 'DAEP', 100, 7089), ('rimozione', '2010_11_10', 11), ('rimozione', '2010_11_11', 90), ('catasto', '2010_11_13', 5703, 'EHJH', 180, 9046), ('catasto', '2010_11_14', 4345, 'APTG', 50, 9377), ('catasto', '2010_11_17', 8646, 'APDM', 150, 6967), ('rimozione', '2010_11_18', 20), ('catasto', '2010_11_19', 4305, 'BPKQ', 100, 1880), ('catasto', '2010_11_19', 7200, 'CNHD', 120, 5291), ('catasto', '2010_11_20', 5304, 'FLTK', 180, 8340), ('catasto', '2010_11_22', 735, 'DQAK', 120, 3385), ('catasto', '2010_11_22', 3534, 'DHML', 50, 3573), ('catasto', '2010_11_25', 1470, 'CHOU', 120, 3637), ('rimozione', '2010_11_25', 88), ('catasto', '2010_11_26', 7612, 'DKMA', 120, 2526), ('catasto', '2010_11_27', 1350, 'FMNC', 150, 6498), ('catasto', '2010_11_27', 8633, 'FWBY', 90, 3961), ('rimozione', '2010_11_28', 21), ('catasto', '2010_11_29', 9604, 'DXCD', 90, 5541), ('rimozione', '2010_11_30', 83), ('rimozione', '2010_11_30', 97), ('catasto', '2010_12_02', 476, 'EXMU', 120, 3879), ('catasto', '2010_12_03', 2126, 'DWUJ', 180, 6781), ('catasto', '2010_12_03', 7518, 'CRUD', 200, 1774), ('catasto', '2010_12_03', 8682, 'AMUX', 100, 2490), ('rimozione', '2010_12_06', 67), ('catasto', '2010_12_07', 3320, 'CFXG', 180, 6567), ('catasto', '2010_12_07', 7909, 'EUXJ', 120, 1262), ('catasto', '2010_12_07', 9859, 'DVHM', 90, 5160), ('catasto', '2010_12_08', 2213, 'ABEF', 150, 9981), ('catasto', '2010_12_10', 7606, 'CRSB', 50, 9143), ('catasto', '2010_12_11', 4438, 'ERWP', 150, 9199), ('catasto', '2010_12_12', 7330, 'EVAW', 100, 8191), ('catasto', '2010_12_16', 5975, 'AGYM', 200, 1051), ('catasto', '2010_12_17', 5529, 'FLBM', 150, 10351), ('catasto', '2010_12_18', 5562, 'BDRN', 300, 3730), ('rimozione', '2010_12_18', 55), ('catasto', '2010_12_19', 9404, 'DAXP', 50, 8911), ('catasto', '2010_12_21', 9292, 'GCRW', 100, 8180), ('rimozione', '2010_12_21', 12), ('rimozione', '2010_12_21', 37), ('catasto', '2010_12_23', 1373, 'DYXS', 50, 3122), ('catasto', '2010_12_25', 3035, 'BWGJ', 50, 6724), ('catasto', '2010_12_25', 7318, 'DTIK', 150, 4230), ('catasto', '2010_12_26', 5200, 'CJEA', 200, 4628), ('catasto', '2010_12_28', 1377, 'CGVD', 180, 9163), ('catasto', '2010_12_28', 2447, 'ADHJ', 150, 5695), ('catasto', '2010_12_29', 3202, 'FYCK', 180, 2540)
]


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritto qua di seguito.
#
# - File 1) 'immobili.csv'
#   Il file memorizza le informazioni su annunci immobiliari
#   (nello specifico, vendita di abitazioni) pubblicate su un sito web e
#   sui dati inseriti nel catasto una volta completata la vendita.
#   Il catasto è un ente della pubblica amministrazione che si occupa
#   di memorizzare informazioni sui proprietari delle abitazioni.
#   Un esempio del contenuto del file e' il seguente.
#   In ogni riga del file possono essere memorizzati i dati
#   di una fra le seguenti tipologie di operazione:
#   - (pubblicazione) di un annuncio di vendita
#   - (rimozione) di un annuncio, perché è stato trovato un acquirente
#   - (catasto) inserimento dei dati del nuovo proprietario dell'abitazione nel catasto
#   Le informazioni presenti in una riga variano a seconda del tipo di
#   operazione memorizzata (pubblicazione, rimozione, catasto).
#   Nell'esempio qua sotto non considerate il simbolo di # e gli spazi iniziali.
#   Gli a capo presenti nel file (\r\n) sono stati omessi per semplicita'.
#   Le prime tre righe descrivono la struttura dati delle diverse tipologie di operazioni.
#
#   Data;tipoOperazione(pubblicazione);idAnnuncio;idAbitazione;M2;prezzoM2Proposto
#   Data;tipoOperazione(rimozione);idAnnuncio
#   Data;tipoOperazione(catasto);idProprietario;idAbitazione;M2;prezzoM2Vendita
#   2010_06_12;pubblicazione;1438;DONN;100;9961
#   2010_06_27;rimozione;1438
#   2010_09_05;catasto;1032;DONN;100;9263
#   2010_01_01;pubblicazione;61;BDXB;200;9229
#   2010_01_01;pubblicazione;136;AUKJ;300;7528
#   2010_01_01;pubblicazione;599;CYFT;180;7646
#   ...
#   In ogni record (record e' un sinonimo di 'riga')
#   può essere memorizzata un'operazione (pubblicazione, rimozione, catasto),
#   maggiori dettagli qua sotto.
#   - pubblicazione. Una riga con tale operazione, contiene le seguenti informazioni:
#        * Data. La data in cui è stato pubblicato l'annuncio.
#                La data è espressa nel formato anno_mese_giorno.
#        * tipoOperazione. La stringa "pubblicazione" contrassegna i record
#                con i dati della pubblicazione di un annuncio di vendita
#        * idAnnuncio. Un numero intero che identifica univocamente
#                l'annuncio di vendita dell'abitazione
#        * idAbitazione. Una stringa di caratteri utilizzata dal catasto per
#                identificare univocamente l'abitazione posta in vendita.
#        * M2. L'estensione in metri quadrati dell'abitazione
#                messa in vendita
#        * prezzoM2Proposto. Il prezzo di vendita al metro quadrato proposto
#                nell'annuncio.
#   - rimozione. Una riga con tale operazione, contiene le seguenti informazioni:
#        * Data. La data in cui l'annuncio è stato rimosso dal sito web.
#                Un annuncio viene tolto una volta effettuata la vendita,
#                assumete che tutte le abitazioni presenti nel dataset vengano vendute.
#        * tipoOperazione. La stringa "rimozione" contrassegna i record
#                con le informazioni sulla rimozione di un annuncio di vendita
#        * idAnnuncio. Analogo al dato presente nel record
#                "pubblicazione"
#   - catasto. Una riga con tale operazione, contiene le seguenti informazioni:
#        * Data. La data in cui le informazioni della vendita sono state comunicate
#                all'ufficio del catasto.
#        * tipoOperazione. La stringa "catasto" contrassegna i record
#                con le informazioni sulla vendita comunicate al catasto
#        * idProprietario. Un numero intero che identifica univocamente
#                il nuovo proprietario
#        * idAbitazione. Analogo al dato presente in un record
#                "pubblicazione"
#        * M2. Analogo al dato presente nel record
#                "pubblicazione"
#        * prezzoM2Vendita. Il prezzo al metro quadrato a cui è stata effettivamente
#                venduta l'abitazione. Può differire dal prezzo di vendita proposto nell'annuncio.
#
#   Nel file, ogni annuncio pubblicitario si conclude con una vendita e con l'inserimento dei dati
#   del nuovo proprietario nel catasto. Quindi per ogni "pubblicazione" esiste sempre un corrispondente
#   record "rimozione" e "catasto". Alcune note sul contenuto del file
#   - i record delle diverse operazioni sono mischiati tra loro
#   - nel file, un record pubblicazione precede sempre il corrispondente record rimozione,
#   - nel file, un record rimozione precede sempre il corrispondente record catasto
#   - i tre record relativi ad una casa (pubblicazione, rimozione, catasto),
#     non sono necessariamente vicini tra loro
#   * NOTA BENE: cercate di aprire il file .csv
#     - con un editor di testo diverso da notepad
#     - senza usare excel (o programmi similari)

##########################################################
# INTRODUZIONE AL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede
# ogni funzione vi spiegherà in dettaglio che cosa fare.
# Controllate nel corpo principale del programma (in fondo
# allo script), come vengono invocate le funzioni che
# implementerete.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
# Se volete, potete implementare funzioni aggiuntive
# rispetto a quelle gia' presenti qua sotto.


##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome = 'Liu'  # inserisci qua il tuo cognome
nome = 'Weihao'  # inserisci qua il tuo nome


# - La funzione seguente accetta come parametro in ingresso
#   il nome del file .csv contenente i dati descritti in precedenza.
#   La funzione deve leggere il contenuto del file e
#   restituire una lista di tuple, come nell'esempio seguente.
#        [
#          ('pubblicazione', data, idAnnuncio, idAbitazione, M2, prezzoM2Proposto),
#          ('rimozione', data, idAnnuncio),
#          ('catasto', data, idProprietario, idAbitazione, M2; prezzoM2Vendita),
#          ...
#        ]
#   dove ogni tupla contiene le informazioni presenti in un record del file.
#   Per esempio, la funzione applicata ad un file con il contenuto seguente
#      Data;tipoOperazione(pubblicazione);idAnnuncio;idAbitazione;M2;prezzoM2Proposto
#      Data;tipoOperazione(rimozione);idAnnuncio
#      Data;tipoOperazione(catasto);idProprietario;idAbitazione;M2;prezzoM2Vendita
#      2010_06_12;pubblicazione;1438;DONN;100;9961
#      2010_06_27;rimozione;1438
#      2010_09_05;catasto;1032;DONN;100;9263
#      ...
#   dovrebbe restituire una struttura dati come la seguente
#   [ ...,
#     ('pubblicazione', '2010_06_12', 1438, 'DONN', 100, 9961)
#     ('rimozione', '2010_06_27', 1438),
#     ('catasto', '2010_09_05', 1032, 'DONN', 100, 9263),
#     ...
#   ]
#   In ogni tupla,
#   - i valori di metri quadrati, prezzo al metro quadrato, idAnnuncio e idProprietario
#     devono essere di tipo intero.
#   - i valori di idAbitazione e data devono essere di tipo stringa.
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
#   se in via provvisoria volete lavorare sulle funzioni successive senza
#   implementare l'attuale, potete utilizzare la struttura dati dichiarata
#   all'inizio di questo script (basta togliere il commento dalla prima riga di codice).
def caricaDatiAbitazioni(fn):
    #        [
    #          ('pubblicazione', data, idAnnuncio, idAbitazione, M2, prezzoM2Proposto),
    #          ('rimozione', data, idAnnuncio),
    #          ('catasto', data, idProprietario, idAbitazione, M2; prezzoM2Vendita),
    #          ...
    #        ]
    file = open(fn, 'r')
    for i in range(3):
        file.readline()
    li = []
    for line in file:
        line = line.strip('\n').strip('\r')
        content = line.split(';')
        tipo_operazione = content[1]
        if tipo_operazione == 'pubblicazione':
            data = content[0]
            id_annuncio = int(content[2])
            id_abitazione = content[3]
            m2 = int(content[4])
            prezzo_m2 = int(content[5])
            li.append((tipo_operazione, str(data), id_annuncio,
                       id_abitazione, m2, prezzo_m2))

        if tipo_operazione == 'rimozione':
            data = content[0]
            id_annuncio = int(content[2])
            li.append((tipo_operazione, str(data), id_annuncio))

        if tipo_operazione == 'catasto':
            data = content[0]
            id_proprietario = int(content[2])
            id_abitazione = content[3]
            m2 = int(content[4])
            prezzo_m2 = int(content[5])
            li.append((tipo_operazione, str(data), id_proprietario,
                       id_abitazione, m2, prezzo_m2))

    return li


# - La funzione calcolaDurataAnnuncio accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiAbitazioni().
#   La funzione seguente deve restituire un dizionario come nell'esempio seguente
#        {
#           id_Annuncio1:giorni_trascorsi1, id_annuncio2:giorni_trascorsi2, ...
#        }
#   Dove ad ogni id_annuncio deve essere associato il numero di giorni trascorsi
#   tra la pubblicazione e la rimozione dell'annuncio.
#   IL giorno di pubblicazione e il giorno di rimozione vanno considerati nel conteggio come giorni interi.
#   Per esempio se l'annuncio è stato pubblicato il 28/giu/2020 ed è stato rimosso il
#   10/lug/2020, i giorni trascorsi sono 13: 3 giorni a giugno (dal 28 compreso al 30 giugno)
#   e 10 giorni a luglio (considerando anche l'ultimo giorno)
#   Per vostra semplicità:
#   - Il file contiene solo date nell'anno 2010. Il 2010 non è stato un anno bisestile.
#   - Nel file, per ogni record "pubblicazione" c'è un corrispondente record "rimozione" e "catasto".
#   - Nel file, un record "rimozione" si trova sempre dopo il corrispondente record "pubblicazione",
#     in maniera analoga accade tra "catasto" e "rimozione".
#   Per il computo dei giorni trascorsi si chiede di trasformare le date nel
#   numero di giorni trascorsi dall'1 gen 2010, sfruttando il seguente dizionario.
# Struttura dati che vi puo' essere utile
dizGiorniMese = {'gennaio': 31, 'febbraio': 28, 'marzo': 31, 'aprile': 30,
                 'maggio': 31, 'giugno': 30, 'luglio': 31, 'agosto': 31,
                 'settembre': 30, 'ottobre': 31, 'novembre': 31, 'dicembre': 31}

# se volete definire delle funzioni accessorie potete farlo qua sotto

# Funzione da implementare


def giorno_data(fn):
    data = fn
    content = data.split('_')
    mm = int(content[1])
    gg = int(content[2])
    li = [0] * 12
    temp = 0
    i = 0
    for mese in dizGiorniMese:
        temp += dizGiorniMese[mese]
        li[i] = temp
        i += 1

    giorni_tot = li[mm-1] + gg
    return giorni_tot


def calcolaDurataAnnuncio(ds):
    # Implementa il codice della funzione qua sotto. La riga con il pass puo' essere cancellata.
    di_a = {}
    di_b = {}
    final_di = {}
    for tu in ds:
        tipo_operazione = tu[0]
        if tipo_operazione == 'pubblicazione':
            data = tu[1]
            id_annuncio = tu[2]
            di_a[id_annuncio] = giorno_data(data)

        if tipo_operazione == 'rimozione':
            data = tu[1]
            id_annuncio = tu[2]
            di_b[id_annuncio] = giorno_data(data)

    for idAnnuncio in di_a:
        final_di[idAnnuncio] = di_b[idAnnuncio] - di_a[idAnnuncio]

    return final_di


# - La funzione seguente accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiAbitazioni().
#   La funzione seguente deve restituire un dizionario come nell'esempio qua sotto
#        {
#         '0_100':prezzo_medio1_metro_quadrato,
#         '101_200':prezzo_medio2_metro_quadrato,
#         '201_e_superiori':prezzo_medio3_metro_quadrato,
#         ...,
#        }
#   Nella prima coppia chiave valore (che appare qua sopra), come valore ci deve essere
#   il prezzo medio al metro quadrato con cui sono state vendute tutte le abitazioni
#   da 0 a 100 metri quadrati (estremi compresi).
#   Nella seconda coppia chiave valore va calcolato il prezzo medio al metro quadrato
#   delle abitazioni con estensione compresa tra 101 e 200 metri quadrati (estremi compresi)
#   Nella terza coppia va calcolato il prezzo medio al metro quadrato delle abitazioni
#   con metratura maggiore o uguale a 201 metri quadrati.
#   I prezzi medi al metro quadrato devono essere di tipo float.
#   Nota bene: i prezzi delle categorie non e' detto che vengano fuori in ordine crescente o decrescente


def prezziCategorieAbitazioni(ds):
    #        {
    #         '0_100':prezzo_medio1_metro_quadrato,
    #         '101_200':prezzo_medio2_metro_quadrato,
    #         '201_e_superiori':prezzo_medio3_metro_quadrato,
    #         ...,
    #        }
    cat_a = '0_100'
    cat_b = '101_200'
    cat_c = '201_e_superiore'
    di_num = {cat_a: 0, cat_b: 0, cat_c: 0}
    di_prezzo = {cat_a: 0, cat_b: 0, cat_c: 0}
    di_out = {}

    for tu in ds:
        tipo_operazione = tu[0]
        if tipo_operazione == 'catasto':
            m2 = tu[4]
            if 0 <= m2 <= 100:
                prezzo_m2 = tu[5]
                di_num[cat_a] += m2
                di_prezzo[cat_a] += m2 * prezzo_m2

            if 101 <= m2 <= 200:
                prezzo_m2 = tu[5]
                di_num[cat_b] += m2
                di_prezzo[cat_b] += m2 * prezzo_m2

            if m2 > 200:
                prezzo_m2 = tu[5]
                di_num[cat_c] += m2
                di_prezzo[cat_c] += m2*prezzo_m2

    for key in di_prezzo:
        di_out[key] = di_prezzo[key] / di_num[key]

    return di_out

    # - La funzione seguente accetta come parametro in ingresso la struttura dati
    #   restituita dalla funzione caricaDatiAbitazioni().
    #   La funzione seguente deve individuare e restituire un valore intero corrispondente
    #   all'idProprietario della persona che ha acquistato più immobili.
    #   Se ci fossero piu' persone a pari merito,
    #   sceglietene una come meglio preferite.


def individuaAcquirente(ds):
    # Implementa il codice della funzione qua sotto. La riga con il pass puo' essere cancellata.
    di = {}
    for tu in ds:
        tipo_operazione = tu[0]
        if tipo_operazione == 'catasto':
            id_proprietario = tu[2]
            if id_proprietario not in di:
                di[id_proprietario] = 1
            else:
                di[id_proprietario] += 1

    mobili_aquistati = 0
    idProprietario = 0
    for key in di:
        if di[key] > mobili_aquistati:
            mobili_aquistati = di[key]
            idProprietario = key

    return (idProprietario, mobili_aquistati)


##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################

print('Esercizio %s.' % (nomeEsercizio))
print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione caricaDatiAbitazioni: ')
fnv = 'Esame-uni/Documents/Esame uni/2020_07_20/immobili.csv'
dpr = caricaDatiAbitazioni(fnv)
print(dpr)

print('2) Eseguo la funzione calcolaDurataAnnuncio: ')
ca = calcolaDurataAnnuncio(dpr)
print(ca)

print('3) Eseguo la funzione prezziCategorieAbitazioni: ')
numpr = prezziCategorieAbitazioni(dpr)
print(numpr)

print("4) Eseguo la funzione individuaAcquirente")
cf = individuaAcquirente(dpr)
print(cf)

print('Nome file e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
