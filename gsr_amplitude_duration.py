import pandas as pd
import numpy as np
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind

bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\GSR\\BADCODE_GSR_DEFAULT\\Peaks pr respondent.csv")
good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\GSR\\GOODCODE_GSR_DEFAULT\\Peaks pr respondent.csv")


# usuwanie wybranych uczestników
good_code = good_code[~good_code['Respondent Name'].isin(['Mateusz Rokosa'])]
bad_code = bad_code[~bad_code['Respondent Name'].isin(['Konrad Kazieczko'])]


# obliczanie Peak Duration
good_code['Peak Duration'] = good_code['Offset Time'] - good_code['Onset Time']
bad_code['Peak Duration'] = bad_code['Offset Time'] - bad_code['Onset Time']


# czyszczenie kolumn
columns_to_save = ['Respondent Name', 'Stimulus Name', 'Amplitude', 'Peak Duration']
good_code = good_code[columns_to_save]
bad_code = bad_code[columns_to_save]


# agregacja
good_code = good_code.groupby(['Respondent Name', 'Stimulus Name'], as_index=False).agg('mean')
bad_code = bad_code.groupby(['Respondent Name', 'Stimulus Name'], as_index=False).agg('mean')


# agregacja zadań 3.1-3.4
good_code_z3 = good_code[good_code['Stimulus Name'].isin(['zad3.2', 'zad3.3', 'zad3.4'])].groupby('Respondent Name', as_index=False).agg('mean')
good_code_z3['Stimulus Name'] = 'zad3'
good_code = good_code[~good_code['Stimulus Name'].isin(['zad3.1', 'zad3.2', 'zad3.3', 'zad3.4'])].append(good_code_z3, ignore_index=True)

bad_code_z3 = bad_code[bad_code['Stimulus Name'].isin(['zad3.2', 'zad3.3', 'zad3.4'])].groupby('Respondent Name', as_index=False).agg('mean')
bad_code_z3['Stimulus Name'] = 'zad3'
bad_code = bad_code[~bad_code['Stimulus Name'].isin(['zad3.1', 'zad3.2', 'zad3.3', 'zad3.4'])].append(bad_code_z3, ignore_index=True)

print(bad_code)

### Analiza Peak Duration
# print(bad_code.groupby('Stimulus Name')['Peak Duration'].median())
# print(good_code.groupby('Stimulus Name')['Peak Duration'].median())
print(bad_code.groupby('Stimulus Name')['Peak Duration'].mean())
print(good_code.groupby('Stimulus Name')['Peak Duration'].mean())
# print(bad_code.groupby('Stimulus Name')['Peak Duration'].std())
# print(good_code.groupby('Stimulus Name')['Peak Duration'].std())
print(shapiro(bad_code.loc[bad_code['Stimulus Name'] == 'zad1', 'Peak Duration']))
print(shapiro(good_code.loc[good_code['Stimulus Name'] == 'zad1', 'Peak Duration']))
print(shapiro(bad_code.loc[bad_code['Stimulus Name'] == 'zad2', 'Peak Duration']))
print(shapiro(good_code.loc[good_code['Stimulus Name'] == 'zad2', 'Peak Duration']))
print(shapiro(bad_code.loc[bad_code['Stimulus Name'] == 'zad3', 'Peak Duration']))
print(shapiro(good_code.loc[good_code['Stimulus Name'] == 'zad3', 'Peak Duration']))
print(mannwhitneyu(bad_code.loc[bad_code['Stimulus Name'] == 'zad1', 'Peak Duration'], good_code.loc[good_code['Stimulus Name'] == 'zad1', 'Peak Duration']))
print(mannwhitneyu(bad_code.loc[bad_code['Stimulus Name'] == 'zad2', 'Peak Duration'], good_code.loc[good_code['Stimulus Name'] == 'zad2', 'Peak Duration']))
print(mannwhitneyu(bad_code.loc[bad_code['Stimulus Name'] == 'zad3', 'Peak Duration'], good_code.loc[good_code['Stimulus Name'] == 'zad3', 'Peak Duration']))
print(ttest_ind(bad_code.loc[bad_code['Stimulus Name'] == 'zad1', 'Peak Duration'], good_code.loc[good_code['Stimulus Name'] == 'zad1', 'Peak Duration']))
print(ttest_ind(bad_code.loc[bad_code['Stimulus Name'] == 'zad2', 'Peak Duration'], good_code.loc[good_code['Stimulus Name'] == 'zad2', 'Peak Duration']))
print(ttest_ind(bad_code.loc[bad_code['Stimulus Name'] == 'zad3', 'Peak Duration'], good_code.loc[good_code['Stimulus Name'] == 'zad3', 'Peak Duration']))


### Analiza Peak Duration
# print(bad_code.groupby('Stimulus Name')['Amplitude'].median())
# print(good_code.groupby('Stimulus Name')['Amplitude'].median())
# print(bad_code.groupby('Stimulus Name')['Amplitude'].mean())
# print(good_code.groupby('Stimulus Name')['Amplitude'].mean())
# print(bad_code.groupby('Stimulus Name')['Amplitude'].std())
# print(good_code.groupby('Stimulus Name')['Amplitude'].std())
# print(shapiro(bad_code.loc[bad_code['Stimulus Name'] == 'zad1', 'Amplitude']))
# print(shapiro(good_code.loc[good_code['Stimulus Name'] == 'zad1', 'Amplitude']))
# print(shapiro(bad_code.loc[bad_code['Stimulus Name'] == 'zad2', 'Amplitude']))
# print(shapiro(good_code.loc[good_code['Stimulus Name'] == 'zad2', 'Amplitude']))
# print(shapiro(bad_code.loc[bad_code['Stimulus Name'] == 'zad3', 'Amplitude']))
# print(shapiro(good_code.loc[good_code['Stimulus Name'] == 'zad3', 'Amplitude']))
# print(mannwhitneyu(bad_code.loc[bad_code['Stimulus Name'] == 'zad1', 'Amplitude'], good_code.loc[good_code['Stimulus Name'] == 'zad1', 'Amplitude']))
# print(mannwhitneyu(bad_code.loc[bad_code['Stimulus Name'] == 'zad2', 'Amplitude'], good_code.loc[good_code['Stimulus Name'] == 'zad2', 'Amplitude']))
# print(mannwhitneyu(bad_code.loc[bad_code['Stimulus Name'] == 'zad3', 'Amplitude'], good_code.loc[good_code['Stimulus Name'] == 'zad3', 'Amplitude']))
# print(ttest_ind(bad_code.loc[bad_code['Stimulus Name'] == 'zad1', 'Amplitude'], good_code.loc[good_code['Stimulus Name'] == 'zad1', 'Amplitude']))
# print(ttest_ind(bad_code.loc[bad_code['Stimulus Name'] == 'zad2', 'Amplitude'], good_code.loc[good_code['Stimulus Name'] == 'zad2', 'Amplitude']))
# print(ttest_ind(bad_code.loc[bad_code['Stimulus Name'] == 'zad3', 'Amplitude'], good_code.loc[good_code['Stimulus Name'] == 'zad3', 'Amplitude']))