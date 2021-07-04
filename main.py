import pandas as pd
import numpy as np
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu


def convert_decibel_to_micro_volt(decibel):
    return pow(10, (decibel / 10.0))


def convert_micro_volt_to_decibel(micro_volt):
    return np.log10(micro_volt) * 10


# bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\BADCODE_EEG_PSD_LEGACY_0.5.csv")
# good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\GOODCODE_EEG_PSD_LEGACY_0.5.csv")

# bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\BADCODE_EEG_PSD_LEGACY_1.csv")
# good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\GOODCODE_EEG_PSD_LEGACY_1.csv")

# bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\BADCODE_EEG_PSD_LEGACY_2.csv")
# good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\GOODCODE_EEG_PSD_LEGACY_2.csv")

# bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\BADCODE_EEG_PSD_WELCH_0.5.csv")
# good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\GOODCODE_EEG_PSD_WELCH_0.5.csv")

bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\BADCODE_EEG_PSD_WELCH_1.csv")
good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\GOODCODE_EEG_PSD_WELCH_1.csv")

# bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\BADCODE_EEG_PSD_WELCH_2.csv")
# good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\PSD&FA\\GOODCODE_EEG_PSD_WELCH_2.csv")

# zamiana decybeli na mikrovolty
bad_code[bad_code.columns[15:50]] = bad_code[bad_code.columns[15:50]].applymap(
    lambda x: convert_decibel_to_micro_volt(x))
good_code[good_code.columns[15:50]] = good_code[good_code.columns[15:50]].applymap(
    lambda x: convert_decibel_to_micro_volt(x))

bad_code_alpha_mean = bad_code[
    ['Mean PSD Ch2 Alpha (dB)', 'Mean PSD Ch3 Alpha (dB)', 'Mean PSD Ch4 Alpha (dB)', 'Mean PSD Ch5 Alpha (dB)', 'Mean PSD Ch6 Alpha (dB)', 'Mean PSD Ch7 Alpha (dB)', 'Mean PSD Ch8 Alpha (dB)']].mean(axis=1, skipna=True)
bad_code_theta_mean = bad_code[
    ['Mean PSD Ch2 Theta (dB)', 'Mean PSD Ch3 Theta (dB)', 'Mean PSD Ch4 Theta (dB)', 'Mean PSD Ch5 Theta (dB)', 'Mean PSD Ch6 Theta (dB)', 'Mean PSD Ch7 Theta (dB)', 'Mean PSD Ch8 Theta (dB)']].mean(axis=1, skipna=True)
bad_code_beta_mean = bad_code[
    ['Mean PSD Ch2 Beta (dB)', 'Mean PSD Ch3 Beta (dB)', 'Mean PSD Ch4 Beta (dB)', 'Mean PSD Ch5 Beta (dB)', 'Mean PSD Ch6 Beta (dB)', 'Mean PSD Ch7 Beta (dB)', 'Mean PSD Ch8 Beta (dB)']].mean(axis=1, skipna=True)


good_code_alpha_mean = good_code[
    ['Mean PSD Ch2 Alpha (dB)', 'Mean PSD Ch3 Alpha (dB)', 'Mean PSD Ch4 Alpha (dB)', 'Mean PSD Ch5 Alpha (dB)', 'Mean PSD Ch6 Alpha (dB)', 'Mean PSD Ch7 Alpha (dB)', 'Mean PSD Ch8 Alpha (dB)']].mean(axis=1, skipna=True)
good_code_theta_mean = good_code[
    ['Mean PSD Ch2 Theta (dB)', 'Mean PSD Ch3 Theta (dB)', 'Mean PSD Ch4 Theta (dB)', 'Mean PSD Ch5 Theta (dB)', 'Mean PSD Ch6 Theta (dB)', 'Mean PSD Ch7 Theta (dB)', 'Mean PSD Ch8 Theta (dB)']].mean(axis=1, skipna=True)
good_code_beta_mean = good_code[
    ['Mean PSD Ch2 Beta (dB)', 'Mean PSD Ch3 Beta (dB)', 'Mean PSD Ch4 Beta (dB)', 'Mean PSD Ch5 Beta (dB)', 'Mean PSD Ch6 Beta (dB)', 'Mean PSD Ch7 Beta (dB)', 'Mean PSD Ch8 Beta (dB)']].mean(axis=1, skipna=True)


bad_code['Mean Alpha'] = bad_code_alpha_mean
bad_code['Mean Theta'] = bad_code_theta_mean
bad_code['Mean Beta'] = bad_code_beta_mean
good_code['Mean Alpha'] = good_code_alpha_mean
good_code['Mean Theta'] = good_code_theta_mean
good_code['Mean Beta'] = good_code_beta_mean

# obliczanie Theta/Alpha Ratio
bad_code_tar = bad_code['Mean Theta'].divide(bad_code['Mean Alpha'], axis='index')
good_code_tar = good_code['Mean Theta'].divide(good_code['Mean Alpha'], axis='index')
bad_code['TAR'] = bad_code_tar
good_code['TAR'] = good_code_tar
bad_code = bad_code.dropna(subset=['TAR'])
good_code = good_code.dropna(subset=['TAR'])

bad_code.to_csv('result_bad.csv', index=False)
good_code.to_csv('result_good.csv', index=False)
bad_code = pd.read_csv('result_bad.csv')
good_code = pd.read_csv('result_good.csv')

print(bad_code.groupby('Label')['TAR'].median())
print(good_code.groupby('Label')['TAR'].median())
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'TAR']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad1', 'TAR']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'TAR']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad2', 'TAR']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.1', 'TAR']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.1', 'TAR']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.2', 'TAR']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.2', 'TAR']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.3', 'TAR']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.3', 'TAR']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.4', 'TAR']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.4', 'TAR']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'TAR'], good_code.loc[bad_code['Label'] == 'zad1', 'TAR']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'TAR'], good_code.loc[bad_code['Label'] == 'zad2', 'TAR']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.1', 'TAR'], good_code.loc[bad_code['Label'] == 'zad3.1', 'TAR']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.2', 'TAR'], good_code.loc[bad_code['Label'] == 'zad3.2', 'TAR']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.3', 'TAR'], good_code.loc[bad_code['Label'] == 'zad3.3', 'TAR']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.4', 'TAR'], good_code.loc[bad_code['Label'] == 'zad3.4', 'TAR']))


# Theta Band Power
print(bad_code.groupby('Label')['Mean Theta'].median())
print(good_code.groupby('Label')['Mean Theta'].median())
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Theta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad1', 'Mean Theta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Theta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad2', 'Mean Theta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Theta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Theta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Theta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Theta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Theta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Theta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Theta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Theta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Theta'], good_code.loc[bad_code['Label'] == 'zad1', 'Mean Theta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Theta'], good_code.loc[bad_code['Label'] == 'zad2', 'Mean Theta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Theta'], good_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Theta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Theta'], good_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Theta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Theta'], good_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Theta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Theta'], good_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Theta']))


# Alpha Band Power
print(bad_code.groupby('Label')['Mean Alpha'].median())
print(good_code.groupby('Label')['Mean Alpha'].median())
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Alpha']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad1', 'Mean Alpha']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Alpha']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad2', 'Mean Alpha']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Alpha']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Alpha']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Alpha']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Alpha']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Alpha']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Alpha']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Alpha']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Alpha']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Alpha'], good_code.loc[bad_code['Label'] == 'zad1', 'Mean Alpha']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Alpha'], good_code.loc[bad_code['Label'] == 'zad2', 'Mean Alpha']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Alpha'], good_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Alpha']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Alpha'], good_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Alpha']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Alpha'], good_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Alpha']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Alpha'], good_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Alpha']))


# Beta Band Power
print(bad_code.groupby('Label')['Mean Beta'].median())
print(good_code.groupby('Label')['Mean Beta'].median())
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Beta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad1', 'Mean Beta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Beta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad2', 'Mean Beta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Beta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Beta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Beta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Beta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Beta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Beta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Beta']))
# print(shapiro(good_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Beta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Beta'], good_code.loc[bad_code['Label'] == 'zad1', 'Mean Beta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Beta'], good_code.loc[bad_code['Label'] == 'zad2', 'Mean Beta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Beta'], good_code.loc[bad_code['Label'] == 'zad3.1', 'Mean Beta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Beta'], good_code.loc[bad_code['Label'] == 'zad3.2', 'Mean Beta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Beta'], good_code.loc[bad_code['Label'] == 'zad3.3', 'Mean Beta']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Beta'], good_code.loc[bad_code['Label'] == 'zad3.4', 'Mean Beta']))




















# print(bad_code[bad_code.columns[15:50]].applymap(lambda x: convert_decibel_to_micro_volt(x)))

# print(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean PSD Electrode Cluster Average Alpha (dB)'])
