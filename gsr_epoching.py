import pandas as pd
import numpy as np
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind

bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\GSR\\BADCODE_GSR_DEFAULT\\GSR Epoching.csv")
good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\GSR\\GOODCODE_GSR_DEFAULT\\GSR Epoching.csv")


# usuwanie wybranych uczestników
good_code = good_code[~good_code['Respondent Name'].isin(['Mateusz Rokosa'])]
bad_code = bad_code[~bad_code['Respondent Name'].isin(['Konrad Kazieczko'])]


# usuwanie quality < 100
good_code = good_code[good_code['Quality'] == 100]
bad_code = bad_code[bad_code['Quality'] == 100]


# czyszczenie kolumn
columns_to_save = ['Respondent Name', 'Label', 'Mean']
good_code = good_code[columns_to_save]
bad_code = bad_code[columns_to_save]


# agregacja
good_code = good_code.groupby(['Respondent Name', 'Label'], as_index=False).agg('mean')
bad_code = bad_code.groupby(['Respondent Name', 'Label'], as_index=False).agg('mean')


# agregacja zadań 3.1-3.4
good_code_z3 = good_code[good_code['Label'].isin(['zad3.2', 'zad3.3', 'zad3.4'])].groupby('Respondent Name', as_index=False).agg('mean')
good_code_z3['Label'] = 'zad3'
good_code = good_code[~good_code['Label'].isin(['zad3.1', 'zad3.2', 'zad3.3', 'zad3.4'])].append(good_code_z3, ignore_index=True)

bad_code_z3 = bad_code[bad_code['Label'].isin(['zad3.2', 'zad3.3', 'zad3.4'])].groupby('Respondent Name', as_index=False).agg('mean')
bad_code_z3['Label'] = 'zad3'
bad_code = bad_code[~bad_code['Label'].isin(['zad3.1', 'zad3.2', 'zad3.3', 'zad3.4'])].append(bad_code_z3, ignore_index=True)


# usuwanie dużych wartości
good_code = good_code[good_code['Mean'] < 10]
bad_code = bad_code[bad_code['Mean'] < 10]


# baselinowanie


### Analiza Mean GSR
# print(bad_code.groupby('Label')['Mean'].median())
# print(good_code.groupby('Label')['Mean'].median())
print(bad_code.groupby('Label')['Mean'].mean())
print(good_code.groupby('Label')['Mean'].mean())
# print(bad_code.groupby('Label')['Mean'].std())
# print(good_code.groupby('Label')['Mean'].std())
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad1', 'Mean']))
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad2', 'Mean']))
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad3', 'Mean']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean'], good_code.loc[good_code['Label'] == 'zad1', 'Mean']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean'], good_code.loc[good_code['Label'] == 'zad2', 'Mean']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean'], good_code.loc[good_code['Label'] == 'zad3', 'Mean']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean'], good_code.loc[good_code['Label'] == 'zad1', 'Mean']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean'], good_code.loc[good_code['Label'] == 'zad2', 'Mean']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean'], good_code.loc[good_code['Label'] == 'zad3', 'Mean']))


