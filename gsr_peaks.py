import pandas as pd
import numpy as np
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind

bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\GSR\\BADCODE_GSR_DEFAULT\\GSR Summary Scores.csv")
good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\GSR\\GOODCODE_GSR_DEFAULT\\GSR Summary Scores.csv")


# usuwanie wybranych uczestników
good_code = good_code[~good_code['Respondent Name'].isin(['Mateusz Rokosa'])]
bad_code = bad_code[~bad_code['Respondent Name'].isin(['Konrad Kazieczko'])]


# czyszczenie kolumn
columns_to_save = ['Respondent Name', 'Label', 'Peak Count', 'Peaks Per Minute']
good_code = good_code[columns_to_save]
bad_code = bad_code[columns_to_save]


# agregacja zadań 3.1-3.4
good_code_z3 = good_code[good_code['Label'].isin(['zad3.2', 'zad3.3', 'zad3.4'])].groupby('Respondent Name', as_index=False).agg('mean')
good_code_z3['Label'] = 'zad3'
good_code = good_code[~good_code['Label'].isin(['zad3.1', 'zad3.2', 'zad3.3', 'zad3.4'])].append(good_code_z3, ignore_index=True)

bad_code_z3 = bad_code[bad_code['Label'].isin(['zad3.2', 'zad3.3', 'zad3.4'])].groupby('Respondent Name', as_index=False).agg('mean')
bad_code_z3['Label'] = 'zad3'
bad_code = bad_code[~bad_code['Label'].isin(['zad3.1', 'zad3.2', 'zad3.3', 'zad3.4'])].append(bad_code_z3, ignore_index=True)


### Analiza Peak Count
# print(bad_code.groupby('Label')['Peak Count'].median())
# print(good_code.groupby('Label')['Peak Count'].median())
# print(bad_code.groupby('Label')['Peak Count'].mean())
# print(good_code.groupby('Label')['Peak Count'].mean())
# print(bad_code.groupby('Label')['Peak Count'].std())
# print(good_code.groupby('Label')['Peak Count'].std())
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Peak Count']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad1', 'Peak Count']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Peak Count']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad2', 'Peak Count']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3', 'Peak Count']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad3', 'Peak Count']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Peak Count'], good_code.loc[good_code['Label'] == 'zad1', 'Peak Count']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Peak Count'], good_code.loc[good_code['Label'] == 'zad2', 'Peak Count']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3', 'Peak Count'], good_code.loc[good_code['Label'] == 'zad3', 'Peak Count']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad1', 'Peak Count'], good_code.loc[good_code['Label'] == 'zad1', 'Peak Count']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad2', 'Peak Count'], good_code.loc[good_code['Label'] == 'zad2', 'Peak Count']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad3', 'Peak Count'], good_code.loc[good_code['Label'] == 'zad3', 'Peak Count']))


### Analiza Peaks Per Minute
# print(bad_code.groupby('Label')['Peaks Per Minute'].median())
# print(good_code.groupby('Label')['Peaks Per Minute'].median())
print(bad_code.groupby('Label')['Peaks Per Minute'].mean())
print(good_code.groupby('Label')['Peaks Per Minute'].mean())
# print(bad_code.groupby('Label')['Peaks Per Minute'].std())
# print(good_code.groupby('Label')['Peaks Per Minute'].std())
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Peaks Per Minute']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad1', 'Peaks Per Minute']))
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Peaks Per Minute']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad2', 'Peaks Per Minute']))
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3', 'Peaks Per Minute']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad3', 'Peaks Per Minute']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Peaks Per Minute'], good_code.loc[good_code['Label'] == 'zad1', 'Peaks Per Minute']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Peaks Per Minute'], good_code.loc[good_code['Label'] == 'zad2', 'Peaks Per Minute']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3', 'Peaks Per Minute'], good_code.loc[good_code['Label'] == 'zad3', 'Peaks Per Minute']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad1', 'Peaks Per Minute'], good_code.loc[good_code['Label'] == 'zad1', 'Peaks Per Minute']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad2', 'Peaks Per Minute'], good_code.loc[good_code['Label'] == 'zad2', 'Peaks Per Minute']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad3', 'Peaks Per Minute'], good_code.loc[good_code['Label'] == 'zad3', 'Peaks Per Minute']))