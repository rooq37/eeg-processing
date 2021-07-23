import pandas as pd
import numpy as np
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind

bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\BADCODE_EEG_BETAS_WELCH_2\\FrontalAsymmetry_metrics.csv")
good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\GOODCODE_EEG_BETAS_WELCH_2\\FrontalAsymmetry_metrics.csv")


# usuwanie wybranych uczestników
good_code = good_code[~good_code['Respondent Name'].isin(['Mateusz Rokosa'])]
bad_code = bad_code[~bad_code['Respondent Name'].isin(['Konrad Kazieczko'])]


# czyszczenie kolumn
columns_to_save = ['Respondent Name', 'Label', 'Mean Frontal Asymmetry Alpha']
good_code = good_code[columns_to_save]
bad_code = bad_code[columns_to_save]


# agregacja zadań 3.1-3.4
good_code_z3 = good_code[good_code['Label'].isin(['zad3.2', 'zad3.3', 'zad3.4'])].groupby('Respondent Name', as_index=False).agg('mean')
good_code_z3['Label'] = 'zad3'
good_code = good_code[~good_code['Label'].isin(['zad3.1', 'zad3.2', 'zad3.3', 'zad3.4'])].append(good_code_z3, ignore_index=True)

bad_code_z3 = bad_code[bad_code['Label'].isin(['zad3.2', 'zad3.3', 'zad3.4'])].groupby('Respondent Name', as_index=False).agg('mean')
bad_code_z3['Label'] = 'zad3'
bad_code = bad_code[~bad_code['Label'].isin(['zad3.1', 'zad3.2', 'zad3.3', 'zad3.4'])].append(bad_code_z3, ignore_index=True)


# FAA
# print(bad_code.groupby('Label')['Mean Frontal Asymmetry Alpha'].median())
# print(good_code.groupby('Label')['Mean Frontal Asymmetry Alpha'].median())
print(bad_code.groupby('Label')['Mean Frontal Asymmetry Alpha'].mean())
print(good_code.groupby('Label')['Mean Frontal Asymmetry Alpha'].mean())
# print(bad_code.groupby('Label')['Mean Frontal Asymmetry Alpha'].std())
# print(good_code.groupby('Label')['Mean Frontal Asymmetry Alpha'].std())
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Frontal Asymmetry Alpha']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad1', 'Mean Frontal Asymmetry Alpha']))
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Frontal Asymmetry Alpha']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad2', 'Mean Frontal Asymmetry Alpha']))
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Frontal Asymmetry Alpha']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad3', 'Mean Frontal Asymmetry Alpha']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Frontal Asymmetry Alpha'], good_code.loc[good_code['Label'] == 'zad1', 'Mean Frontal Asymmetry Alpha']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Frontal Asymmetry Alpha'], good_code.loc[good_code['Label'] == 'zad2', 'Mean Frontal Asymmetry Alpha']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Frontal Asymmetry Alpha'], good_code.loc[good_code['Label'] == 'zad3', 'Mean Frontal Asymmetry Alpha']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Frontal Asymmetry Alpha'], good_code.loc[good_code['Label'] == 'zad1', 'Mean Frontal Asymmetry Alpha']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Frontal Asymmetry Alpha'], good_code.loc[good_code['Label'] == 'zad2', 'Mean Frontal Asymmetry Alpha']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Frontal Asymmetry Alpha'], good_code.loc[good_code['Label'] == 'zad3', 'Mean Frontal Asymmetry Alpha']))