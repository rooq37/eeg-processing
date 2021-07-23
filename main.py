import pandas as pd
import numpy as np
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind


def convert_decibel_to_micro_volt(decibel):
    return pow(10, (decibel / 10.0))


def convert_micro_volt_to_decibel(micro_volt):
    return np.log10(micro_volt) * 10


# bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\BADCODE_EEG_BETAS_LEGACY_0_5\\PSD_metrics.csv")
# good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\GOODCODE_EEG_BETAS_LEGACY_0_5\\PSD_metrics.csv")

# bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\BADCODE_EEG_BETAS_LEGACY_1\\PSD_metrics.csv")
# good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\GOODCODE_EEG_BETAS_LEGACY_1\\PSD_metrics.csv")

# bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\BADCODE_EEG_BETAS_LEGACY_2\\PSD_metrics.csv")
# good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\GOODCODE_EEG_BETAS_LEGACY_2\\PSD_metrics.csv")

# bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\BADCODE_EEG_BETAS_WELCH_0_5\\PSD_metrics.csv")
# good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\GOODCODE_EEG_BETAS_WELCH_0_5\\PSD_metrics.csv")

# bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\BADCODE_EEG_BETAS_WELCH_1\\PSD_metrics.csv")
# good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\GOODCODE_EEG_BETAS_WELCH_1\\PSD_metrics.csv")

bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\BADCODE_EEG_BETAS_WELCH_2\\PSD_metrics.csv")
good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\EGG_BETAS\\GOODCODE_EEG_BETAS_WELCH_2\\PSD_metrics.csv")


# usuwanie wybranych uczestników
good_code = good_code[~good_code['Respondent Name'].isin(['Mateusz Rokosa'])]
bad_code = bad_code[~bad_code['Respondent Name'].isin(['Konrad Kazieczko'])]


# zamiana decybeli na mikrovolty
bad_code[bad_code.columns[15:50]] = bad_code[bad_code.columns[15:50]].applymap(
    lambda x: convert_decibel_to_micro_volt(x))
good_code[good_code.columns[15:50]] = good_code[good_code.columns[15:50]].applymap(
    lambda x: convert_decibel_to_micro_volt(x))


# alpha_channels = ['Mean PSD Ch2 Alpha (dB)', 'Mean PSD Ch3 Alpha (dB)', 'Mean PSD Ch4 Alpha (dB)', 'Mean PSD Ch5 Alpha (dB)', 'Mean PSD Ch6 Alpha (dB)', 'Mean PSD Ch7 Alpha (dB)', 'Mean PSD Ch8 Alpha (dB)']
alpha_channels = ['Mean PSD Ch2 Alpha (dB)', 'Mean PSD Ch3 Alpha (dB)', 'Mean PSD Ch4 Alpha (dB)', 'Mean PSD Ch5 Alpha (dB)', 'Mean PSD Ch6 Alpha (dB)', 'Mean PSD Ch7 Alpha (dB)', 'Mean PSD Ch8 Alpha (dB)']
theta_channels = ['Mean PSD Ch2 Theta (dB)', 'Mean PSD Ch3 Theta (dB)', 'Mean PSD Ch4 Theta (dB)', 'Mean PSD Ch5 Theta (dB)', 'Mean PSD Ch6 Theta (dB)', 'Mean PSD Ch7 Theta (dB)', 'Mean PSD Ch8 Theta (dB)']
low_beta_channels = ['Mean PSD Ch2 Delta (dB)', 'Mean PSD Ch3 Delta (dB)', 'Mean PSD Ch4 Delta (dB)', 'Mean PSD Ch5 Delta (dB)', 'Mean PSD Ch6 Delta (dB)', 'Mean PSD Ch7 Delta (dB)', 'Mean PSD Ch8 Delta (dB)']
regular_beta_channels = ['Mean PSD Ch2 Beta (dB)', 'Mean PSD Ch3 Beta (dB)', 'Mean PSD Ch4 Beta (dB)', 'Mean PSD Ch5 Beta (dB)', 'Mean PSD Ch6 Beta (dB)', 'Mean PSD Ch7 Beta (dB)', 'Mean PSD Ch8 Beta (dB)']
high_beta_channels = ['Mean PSD Ch2 Gamma (dB)', 'Mean PSD Ch3 Gamma (dB)', 'Mean PSD Ch4 Gamma (dB)', 'Mean PSD Ch5 Gamma (dB)', 'Mean PSD Ch6 Gamma (dB)', 'Mean PSD Ch7 Gamma (dB)', 'Mean PSD Ch8 Gamma (dB)']


bad_code_alpha_mean = bad_code[alpha_channels].mean(axis=1, skipna=True)
bad_code_theta_mean = bad_code[theta_channels].mean(axis=1, skipna=True)
bad_code_low_beta_mean = bad_code[low_beta_channels].mean(axis=1, skipna=True)
bad_code_regular_beta_mean = bad_code[regular_beta_channels].mean(axis=1, skipna=True)
bad_code_high_beta_mean = bad_code[high_beta_channels].mean(axis=1, skipna=True)


good_code_alpha_mean = good_code[alpha_channels].mean(axis=1, skipna=True)
good_code_theta_mean = good_code[theta_channels].mean(axis=1, skipna=True)
good_code_low_beta_mean = good_code[low_beta_channels].mean(axis=1, skipna=True)
good_code_regular_beta_mean = good_code[regular_beta_channels].mean(axis=1, skipna=True)
good_code_high_beta_mean = good_code[high_beta_channels].mean(axis=1, skipna=True)


bad_code['Mean Alpha'] = bad_code_alpha_mean
bad_code['Mean Theta'] = bad_code_theta_mean
bad_code['Mean Low Beta'] = bad_code_low_beta_mean
bad_code['Mean Regular Beta'] = bad_code_regular_beta_mean
bad_code['Mean High Beta'] = bad_code_high_beta_mean
good_code['Mean Alpha'] = good_code_alpha_mean
good_code['Mean Theta'] = good_code_theta_mean
good_code['Mean Low Beta'] = good_code_low_beta_mean
good_code['Mean Regular Beta'] = good_code_regular_beta_mean
good_code['Mean High Beta'] = good_code_high_beta_mean


# obliczanie Theta/Alpha Ratio
bad_code_tar = bad_code['Mean Theta'].divide(bad_code['Mean Alpha'], axis='index')
good_code_tar = good_code['Mean Theta'].divide(good_code['Mean Alpha'], axis='index')
bad_code['TAR'] = bad_code_tar
good_code['TAR'] = good_code_tar
bad_code = bad_code.dropna(subset=['TAR'])
good_code = good_code.dropna(subset=['TAR'])


# czyszczenie kolumn
columns_to_save = ['Respondent Name', 'Label', 'Mean Alpha', 'Mean Theta', 'Mean Low Beta', 'Mean Regular Beta', 'Mean High Beta', 'TAR']
good_code = good_code[columns_to_save]
bad_code = bad_code[columns_to_save]


# agregacja zadań 3.1-3.4
good_code_z3 = good_code[good_code['Label'].isin(['zad3.2', 'zad3.3', 'zad3.4'])].groupby('Respondent Name', as_index=False).agg('mean')
good_code_z3['Label'] = 'zad3'
good_code = good_code[~good_code['Label'].isin(['zad3.1', 'zad3.2', 'zad3.3', 'zad3.4'])].append(good_code_z3, ignore_index=True)

bad_code_z3 = bad_code[bad_code['Label'].isin(['zad3.2', 'zad3.3', 'zad3.4'])].groupby('Respondent Name', as_index=False).agg('mean')
bad_code_z3['Label'] = 'zad3'
bad_code = bad_code[~bad_code['Label'].isin(['zad3.1', 'zad3.2', 'zad3.3', 'zad3.4'])].append(bad_code_z3, ignore_index=True)


bad_code.to_csv('result_bad.csv', index=False)
good_code.to_csv('result_good.csv', index=False)
bad_code = pd.read_csv('result_bad.csv')
good_code = pd.read_csv('result_good.csv')


### Analiza Theta/Alpha
# print(bad_code.groupby('Label')['TAR'].median())
# print(good_code.groupby('Label')['TAR'].median())
print(bad_code.groupby('Label')['TAR'].mean())
print(good_code.groupby('Label')['TAR'].mean())
# print(bad_code.groupby('Label')['TAR'].std())
# print(good_code.groupby('Label')['TAR'].std())
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'TAR']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad1', 'TAR']))
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'TAR']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad2', 'TAR']))
print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3', 'TAR']))
print(shapiro(good_code.loc[good_code['Label'] == 'zad3', 'TAR']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'TAR'], good_code.loc[good_code['Label'] == 'zad1', 'TAR']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'TAR'], good_code.loc[good_code['Label'] == 'zad2', 'TAR']))
print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3', 'TAR'], good_code.loc[good_code['Label'] == 'zad3', 'TAR']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad1', 'TAR'], good_code.loc[good_code['Label'] == 'zad1', 'TAR']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad2', 'TAR'], good_code.loc[good_code['Label'] == 'zad2', 'TAR']))
print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad3', 'TAR'], good_code.loc[good_code['Label'] == 'zad3', 'TAR']))


# Theta Band Power
# print(bad_code.groupby('Label')['Mean Theta'].median())
# print(good_code.groupby('Label')['Mean Theta'].median())
# print(bad_code.groupby('Label')['Mean Theta'].mean())
# print(good_code.groupby('Label')['Mean Theta'].mean())
# print(bad_code.groupby('Label')['Mean Theta'].std())
# print(good_code.groupby('Label')['Mean Theta'].std())
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Theta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad1', 'Mean Theta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Theta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad2', 'Mean Theta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Theta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad3', 'Mean Theta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Theta'], good_code.loc[good_code['Label'] == 'zad1', 'Mean Theta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Theta'], good_code.loc[good_code['Label'] == 'zad2', 'Mean Theta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Theta'], good_code.loc[good_code['Label'] == 'zad3', 'Mean Theta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Theta'], good_code.loc[good_code['Label'] == 'zad1', 'Mean Theta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Theta'], good_code.loc[good_code['Label'] == 'zad2', 'Mean Theta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Theta'], good_code.loc[good_code['Label'] == 'zad3', 'Mean Theta']))


# Alpha Band Power
# print(bad_code.groupby('Label')['Mean Alpha'].median())
# print(good_code.groupby('Label')['Mean Alpha'].median())
# print(bad_code.groupby('Label')['Mean Alpha'].mean())
# print(good_code.groupby('Label')['Mean Alpha'].mean())
# print(bad_code.groupby('Label')['Mean Alpha'].std())
# print(good_code.groupby('Label')['Mean Alpha'].std())
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Alpha']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad1', 'Mean Alpha']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Alpha']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad2', 'Mean Alpha']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Alpha']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad3', 'Mean Alpha']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Alpha'], good_code.loc[good_code['Label'] == 'zad1', 'Mean Alpha']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Alpha'], good_code.loc[good_code['Label'] == 'zad2', 'Mean Alpha']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Alpha'], good_code.loc[good_code['Label'] == 'zad3', 'Mean Alpha']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Alpha'], good_code.loc[good_code['Label'] == 'zad1', 'Mean Alpha']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Alpha'], good_code.loc[good_code['Label'] == 'zad2', 'Mean Alpha']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Alpha'], good_code.loc[good_code['Label'] == 'zad3', 'Mean Alpha']))


# Low Beta Band Power
# print(bad_code.groupby('Label')['Mean Low Beta'].median())
# print(good_code.groupby('Label')['Mean Low Beta'].median())
# print(bad_code.groupby('Label')['Mean Low Beta'].mean())
# print(good_code.groupby('Label')['Mean Low Beta'].mean())
# print(bad_code.groupby('Label')['Mean Low Beta'].std())
# print(good_code.groupby('Label')['Mean Low Beta'].std())
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Low Beta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad1', 'Mean Low Beta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Low Beta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad2', 'Mean Low Beta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Low Beta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad3', 'Mean Low Beta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Low Beta'], good_code.loc[good_code['Label'] == 'zad1', 'Mean Low Beta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Low Beta'], good_code.loc[good_code['Label'] == 'zad2', 'Mean Low Beta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Low Beta'], good_code.loc[good_code['Label'] == 'zad3', 'Mean Low Beta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Low Beta'], good_code.loc[good_code['Label'] == 'zad1', 'Mean Low Beta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Low Beta'], good_code.loc[good_code['Label'] == 'zad2', 'Mean Low Beta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Low Beta'], good_code.loc[good_code['Label'] == 'zad3', 'Mean Low Beta']))


# Regular Beta Band Power
# print(bad_code.groupby('Label')['Mean Regular Beta'].median())
# print(good_code.groupby('Label')['Mean Regular Beta'].median())
# print(bad_code.groupby('Label')['Mean Regular Beta'].mean())
# print(good_code.groupby('Label')['Mean Regular Beta'].mean())
# print(bad_code.groupby('Label')['Mean Regular Beta'].std())
# print(good_code.groupby('Label')['Mean Regular Beta'].std())
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Regular Beta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad1', 'Mean Regular Beta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Regular Beta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad2', 'Mean Regular Beta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Regular Beta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad3', 'Mean Regular Beta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Regular Beta'], good_code.loc[good_code['Label'] == 'zad1', 'Mean Regular Beta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Regular Beta'], good_code.loc[good_code['Label'] == 'zad2', 'Mean Regular Beta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Regular Beta'], good_code.loc[good_code['Label'] == 'zad3', 'Mean Regular Beta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean Regular Beta'], good_code.loc[good_code['Label'] == 'zad1', 'Mean Regular Beta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean Regular Beta'], good_code.loc[good_code['Label'] == 'zad2', 'Mean Regular Beta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean Regular Beta'], good_code.loc[good_code['Label'] == 'zad3', 'Mean Regular Beta']))


# High Beta Band Power
# print(bad_code.groupby('Label')['Mean High Beta'].median())
# print(good_code.groupby('Label')['Mean High Beta'].median())
# print(bad_code.groupby('Label')['Mean High Beta'].mean())
# print(good_code.groupby('Label')['Mean High Beta'].mean())
# print(bad_code.groupby('Label')['Mean High Beta'].std())
# print(good_code.groupby('Label')['Mean High Beta'].std())
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean High Beta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad1', 'Mean High Beta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean High Beta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad2', 'Mean High Beta']))
# print(shapiro(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean High Beta']))
# print(shapiro(good_code.loc[good_code['Label'] == 'zad3', 'Mean High Beta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean High Beta'], good_code.loc[good_code['Label'] == 'zad1', 'Mean High Beta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean High Beta'], good_code.loc[good_code['Label'] == 'zad2', 'Mean High Beta']))
# print(mannwhitneyu(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean High Beta'], good_code.loc[good_code['Label'] == 'zad3', 'Mean High Beta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean High Beta'], good_code.loc[good_code['Label'] == 'zad1', 'Mean High Beta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad2', 'Mean High Beta'], good_code.loc[good_code['Label'] == 'zad2', 'Mean High Beta']))
# print(ttest_ind(bad_code.loc[bad_code['Label'] == 'zad3', 'Mean High Beta'], good_code.loc[good_code['Label'] == 'zad3', 'Mean High Beta']))


# ERD Alpha
# bad_code_pivot = pd.pivot_table(bad_code, values=['Mean Alpha', 'Mean Beta', "Mean Theta"], index='Respondent Name', columns='Label').reset_index()
# good_code_pivot = pd.pivot_table(good_code, values=['Mean Alpha', 'Mean Beta', "Mean Theta"], index='Respondent Name', columns='Label').reset_index()
#
#
# bad_code_pivot[('ERD zad1', 'ERD zad1')] = ((bad_code_pivot[('Mean Alpha', 'baseline-1')] - bad_code_pivot[('Mean Alpha', 'zad1')]) / bad_code_pivot[('Mean Alpha', 'baseline-1')]) * 100
# good_code_pivot[('ERD zad1', 'ERD zad1')] = ((good_code_pivot[('Mean Alpha', 'baseline-1')] - good_code_pivot[('Mean Alpha', 'zad1')]) / good_code_pivot[('Mean Alpha', 'baseline-1')]) * 100
# bad_code_pivot[('ERD zad2', 'ERD zad2')] = ((bad_code_pivot[('Mean Alpha', 'baseline-2')] - bad_code_pivot[('Mean Alpha', 'zad2')]) / bad_code_pivot[('Mean Alpha', 'baseline-2')]) * 100
# good_code_pivot[('ERD zad2', 'ERD zad2')] = ((good_code_pivot[('Mean Alpha', 'baseline-2')] - good_code_pivot[('Mean Alpha', 'zad2')]) / good_code_pivot[('Mean Alpha', 'baseline-2')]) * 100
# bad_code_pivot[('ERD zad3.1', 'ERD zad3.1')] = ((bad_code_pivot[('Mean Alpha', 'baseline-3')] - bad_code_pivot[('Mean Alpha', 'zad3.1')]) / bad_code_pivot[('Mean Alpha', 'baseline-3')]) * 100
# good_code_pivot[('ERD zad3.1', 'ERD zad3.1')] = ((good_code_pivot[('Mean Alpha', 'baseline-3')] - good_code_pivot[('Mean Alpha', 'zad3.1')]) / good_code_pivot[('Mean Alpha', 'baseline-3')]) * 100
# bad_code_pivot[('ERD zad3.2', 'ERD zad3.2')] = ((bad_code_pivot[('Mean Alpha', 'baseline-3')] - bad_code_pivot[('Mean Alpha', 'zad3.2')]) / bad_code_pivot[('Mean Alpha', 'baseline-3')]) * 100
# good_code_pivot[('ERD zad3.2', 'ERD zad3.2')] = ((good_code_pivot[('Mean Alpha', 'baseline-3')] - good_code_pivot[('Mean Alpha', 'zad3.2')]) / good_code_pivot[('Mean Alpha', 'baseline-3')]) * 100
# bad_code_pivot[('ERD zad3.3', 'ERD zad3.3')] = ((bad_code_pivot[('Mean Alpha', 'baseline-3')] - bad_code_pivot[('Mean Alpha', 'zad3.3')]) / bad_code_pivot[('Mean Alpha', 'baseline-3')]) * 100
# good_code_pivot[('ERD zad3.3', 'ERD zad3.3')] = ((good_code_pivot[('Mean Alpha', 'baseline-3')] - good_code_pivot[('Mean Alpha', 'zad3.3')]) / good_code_pivot[('Mean Alpha', 'baseline-3')]) * 100
# bad_code_pivot[('ERD zad3.4', 'ERD zad3.4')] = ((bad_code_pivot[('Mean Alpha', 'baseline-3')] - bad_code_pivot[('Mean Alpha', 'zad3.4')]) / bad_code_pivot[('Mean Alpha', 'baseline-3')]) * 100
# good_code_pivot[('ERD zad3.4', 'ERD zad3.4')] = ((good_code_pivot[('Mean Alpha', 'baseline-3')] - good_code_pivot[('Mean Alpha', 'zad3.4')]) / good_code_pivot[('Mean Alpha', 'baseline-3')]) * 100


# print(bad_code_pivot[('ERD zad1', 'ERD zad1')].median())
# print(good_code_pivot[('ERD zad1', 'ERD zad1')].median())
# print(bad_code_pivot[('ERD zad2', 'ERD zad2')].median())
# print(good_code_pivot[('ERD zad2', 'ERD zad2')].median())
# print(bad_code_pivot[('ERD zad3.1', 'ERD zad3.1')].median())
# print(good_code_pivot[('ERD zad3.1', 'ERD zad3.1')].median())
# print(bad_code_pivot[('ERD zad3.2', 'ERD zad3.2')].median())
# print(good_code_pivot[('ERD zad3.2', 'ERD zad3.2')].median())
# print(bad_code_pivot[('ERD zad3.3', 'ERD zad3.3')].median())
# print(good_code_pivot[('ERD zad3.3', 'ERD zad3.3')].median())
# print(bad_code_pivot[('ERD zad3.4', 'ERD zad3.4')].median())
# print(good_code_pivot[('ERD zad3.4', 'ERD zad3.4')].median())
# print(shapiro(bad_code_pivot[('ERD zad1', 'ERD zad1')]))
# print(shapiro(good_code_pivot[('ERD zad1', 'ERD zad1')]))
# print(shapiro(bad_code_pivot[('ERD zad2', 'ERD zad2')]))
# print(shapiro(good_code_pivot[('ERD zad2', 'ERD zad2')]))
# print(shapiro(bad_code_pivot[('ERD zad3.1', 'ERD zad3.1')]))
# print(shapiro(good_code_pivot[('ERD zad3.1', 'ERD zad3.1')]))
# print(shapiro(bad_code_pivot[('ERD zad3.2', 'ERD zad3.2')]))
# print(shapiro(good_code_pivot[('ERD zad3.2', 'ERD zad3.2')]))
# print(shapiro(bad_code_pivot[('ERD zad3.3', 'ERD zad3.3')]))
# print(shapiro(good_code_pivot[('ERD zad3.3', 'ERD zad3.3')]))
# print(shapiro(bad_code_pivot[('ERD zad3.4', 'ERD zad3.4')]))
# print(shapiro(good_code_pivot[('ERD zad3.4', 'ERD zad3.4')]))
# print(mannwhitneyu(bad_code_pivot[('ERD zad1', 'ERD zad1')], good_code_pivot[('ERD zad1', 'ERD zad1')]))
# print(mannwhitneyu(bad_code_pivot[('ERD zad2', 'ERD zad2')].dropna(), good_code_pivot[('ERD zad2', 'ERD zad2')].dropna()))
# print(mannwhitneyu(bad_code_pivot[('ERD zad3.1', 'ERD zad3.1')].dropna(), good_code_pivot[('ERD zad3.1', 'ERD zad3.1')].dropna()))
# print(mannwhitneyu(bad_code_pivot[('ERD zad3.2', 'ERD zad3.2')].dropna(), good_code_pivot[('ERD zad3.2', 'ERD zad3.2')].dropna()))
# print(mannwhitneyu(good_code_pivot[('ERD zad3.3', 'ERD zad3.3')].dropna(), good_code_pivot[('ERD zad3.3', 'ERD zad3.3')].dropna()))
# print(mannwhitneyu(bad_code_pivot[('ERD zad3.4', 'ERD zad3.4')].dropna(), good_code_pivot[('ERD zad3.4', 'ERD zad3.4')].dropna()))

# bad_code_pivot.to_csv('bad_code_pivot.csv')














# print(bad_code[bad_code.columns[15:50]].applymap(lambda x: convert_decibel_to_micro_volt(x)))

# print(bad_code.loc[bad_code['Label'] == 'zad1', 'Mean PSD Electrode Cluster Average Alpha (dB)'])
