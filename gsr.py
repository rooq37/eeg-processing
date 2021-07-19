import pandas as pd
import numpy as np
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind

bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\GSR\\GOODCODE_GSR_500\\GSR Summary Scores.csv")
good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\GSR\\GOODCODE_GSR_500\\GSR Summary Scores.csv")


# usuwanie wybranych uczestników
good_code = good_code[~good_code['Respondent Name'].isin(['Mateusz Rokosa', 'Filip Błażełek'])]
bad_code = bad_code[~bad_code['Respondent Name'].isin(['Konrad Kazieczko', 'Mateusz Starczyk'])]


### Analiza liczby pików
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

