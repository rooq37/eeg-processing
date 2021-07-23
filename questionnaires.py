import pandas as pd
import numpy as np
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind

bad_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\BADCODE_ANKIETY_ANALYSIS.csv", sep=';')
good_code = pd.read_csv("C:\\Users\\Mateusz\\Desktop\\GOODCODE_ANKIETY_ANALYSIS.csv", sep=';')

### Analiza Zad1
# print(shapiro(bad_code['VALUE tlx-1_TLX1_Mental']))
# print(shapiro(good_code['VALUE tlx-1_TLX1_Mental']))
# print(shapiro(bad_code['VALUE tlx-1_TLX1_Overall']))
# print(shapiro(good_code['VALUE tlx-1_TLX1_Overall']))
# print(shapiro(bad_code['VALUE tlx-1_TLX1_Effort']))
# print(shapiro(good_code['VALUE tlx-1_TLX1_Effort']))
# print(shapiro(bad_code['VALUE tlx-1_TLX1_Frustration']))
# print(shapiro(good_code['VALUE tlx-1_TLX1_Frustration']))
# print(shapiro(bad_code['VALUE tlx-1_TLX1_Temporal']))
# print(shapiro(good_code['VALUE tlx-1_TLX1_Temporal']))
# print(shapiro(bad_code['VALUE sam-1_Valence Slider']))
# print(shapiro(good_code['VALUE sam-1_Valence Slider']))
# print(shapiro(bad_code['VALUE sam-1_Arousal Slider']))
# print(shapiro(good_code['VALUE sam-1_Arousal Slider']))
#
# print(ttest_ind(bad_code['VALUE tlx-1_TLX1_Mental'], good_code['VALUE tlx-1_TLX1_Mental']))
# print(ttest_ind(bad_code['VALUE tlx-1_TLX1_Overall'], good_code['VALUE tlx-1_TLX1_Overall']))
# print(mannwhitneyu(bad_code['VALUE tlx-1_TLX1_Effort'], good_code['VALUE tlx-1_TLX1_Effort']))
# print(ttest_ind(bad_code['VALUE tlx-1_TLX1_Frustration'], good_code['VALUE tlx-1_TLX1_Frustration']))
# print(mannwhitneyu(bad_code['VALUE tlx-1_TLX1_Temporal'], good_code['VALUE tlx-1_TLX1_Temporal']))
# print(ttest_ind(bad_code['VALUE sam-1_Valence Slider'], good_code['VALUE sam-1_Valence Slider']))
# print(ttest_ind(bad_code['VALUE sam-1_Arousal Slider'], good_code['VALUE sam-1_Arousal Slider']))


### Analiza Zad2
# print(shapiro(bad_code['VALUE tlx-2_TLX1_Mental']))
# print(shapiro(good_code['VALUE tlx-2_TLX1_Mental']))
# print(shapiro(bad_code['VALUE tlx-2_TLX1_Overall']))
# print(shapiro(good_code['VALUE tlx-2_TLX1_Overall']))
# print(shapiro(bad_code['VALUE tlx-2_TLX1_Effort']))
# print(shapiro(good_code['VALUE tlx-2_TLX1_Effort']))
# print(shapiro(bad_code['VALUE tlx-2_TLX1_Frustration']))
# print(shapiro(good_code['VALUE tlx-2_TLX1_Frustration']))
# print(shapiro(bad_code['VALUE tlx-2_TLX1_Temporal']))
# print(shapiro(good_code['VALUE tlx-2_TLX1_Temporal']))
# print(shapiro(bad_code['VALUE sam-2_Valence Slider']))
# print(shapiro(good_code['VALUE sam-2_Valence Slider']))
# print(shapiro(bad_code['VALUE sam-2_Arousal Slider']))
# print(shapiro(good_code['VALUE sam-2_Arousal Slider']))
#
# print(ttest_ind(bad_code['VALUE tlx-2_TLX1_Mental'], good_code['VALUE tlx-2_TLX1_Mental']))
# print(ttest_ind(bad_code['VALUE tlx-2_TLX1_Overall'], good_code['VALUE tlx-2_TLX1_Overall']))
# print(ttest_ind(bad_code['VALUE tlx-2_TLX1_Effort'], good_code['VALUE tlx-2_TLX1_Effort']))
# print(ttest_ind(bad_code['VALUE tlx-2_TLX1_Frustration'], good_code['VALUE tlx-2_TLX1_Frustration']))
# print(ttest_ind(bad_code['VALUE tlx-2_TLX1_Temporal'], good_code['VALUE tlx-2_TLX1_Temporal']))
# print(mannwhitneyu(bad_code['VALUE sam-2_Valence Slider'], good_code['VALUE sam-2_Valence Slider']))
# print(ttest_ind(bad_code['VALUE sam-2_Arousal Slider'], good_code['VALUE sam-2_Arousal Slider']))


### Analiza Zad3
# print(shapiro(bad_code['VALUE tlx-3_TLX1_Mental']))
# print(shapiro(good_code['VALUE tlx-3_TLX1_Mental']))
# print(shapiro(bad_code['VALUE tlx-3_TLX1_Overall']))
# print(shapiro(good_code['VALUE tlx-3_TLX1_Overall']))
# print(shapiro(bad_code['VALUE tlx-3_TLX1_Effort']))
# print(shapiro(good_code['VALUE tlx-3_TLX1_Effort']))
# print(shapiro(bad_code['VALUE tlx-3_TLX1_Frustration']))
# print(shapiro(good_code['VALUE tlx-3_TLX1_Frustration']))
# print(shapiro(bad_code['VALUE tlx-3_TLX1_Temporal']))
# print(shapiro(good_code['VALUE tlx-3_TLX1_Temporal']))
# print(shapiro(bad_code['VALUE sam-3_Valence Slider']))
# print(shapiro(good_code['VALUE sam-3_Valence Slider']))
# print(shapiro(bad_code['VALUE sam-3_Arousal Slider']))
# print(shapiro(good_code['VALUE sam-3_Arousal Slider']))
#
print(ttest_ind(bad_code['VALUE tlx-3_TLX1_Mental'], good_code['VALUE tlx-3_TLX1_Mental']))
print(ttest_ind(bad_code['VALUE tlx-3_TLX1_Overall'], good_code['VALUE tlx-3_TLX1_Overall']))
print(mannwhitneyu(bad_code['VALUE tlx-3_TLX1_Effort'], good_code['VALUE tlx-3_TLX1_Effort']))
print(mannwhitneyu(bad_code['VALUE tlx-3_TLX1_Frustration'], good_code['VALUE tlx-3_TLX1_Frustration']))
print(ttest_ind(bad_code['VALUE tlx-3_TLX1_Temporal'], good_code['VALUE tlx-3_TLX1_Temporal']))
print(ttest_ind(bad_code['VALUE sam-3_Valence Slider'], good_code['VALUE sam-3_Valence Slider']))
print(ttest_ind(bad_code['VALUE sam-3_Arousal Slider'], good_code['VALUE sam-3_Arousal Slider']))
