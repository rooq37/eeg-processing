import pandas as pd
import numpy as np

emg_001 = pd.read_csv("D:\\iMotions\\Export\\Mateusz and Konrad[badcode]\\Sensor Data\\001_Dawid Antczak.csv")
emg_002 = pd.read_csv("D:\\iMotions\\Export\\Mateusz and Konrad[badcode]\\Sensor Data\\002_Mateusz Starczyk.csv")
emg_003 = pd.read_csv("D:\\iMotions\\Export\\Mateusz and Konrad[badcode]\\Sensor Data\\003_Emilia Starczyk.csv")
emg_004 = pd.read_csv("D:\\iMotions\\Export\\Mateusz and Konrad[badcode]\\Sensor Data\\004_Filip Loffler.csv")
emg_005 = pd.read_csv("D:\\iMotions\\Export\\Mateusz and Konrad[badcode]\\Sensor Data\\005_Bartek Stajnowski.csv")
emg_006 = pd.read_csv("D:\\iMotions\\Export\\Mateusz and Konrad[badcode]\\Sensor Data\\006_Maciej Chodukiewicz.csv")
emg_007 = pd.read_csv("D:\\iMotions\\Export\\Mateusz and Konrad[badcode]\\Sensor Data\\007_Konrad Kazieczko.csv")
emg_008 = pd.read_csv("D:\\iMotions\\Export\\Mateusz and Konrad[badcode]\\Sensor Data\\008_Michal Borysiuk.csv")
emg_009 = pd.read_csv("D:\\iMotions\\Export\\Mateusz and Konrad[badcode]\\Sensor Data\\009_Szymon Bal.csv")
emg_010 = pd.read_csv("D:\\iMotions\\Export\\Mateusz and Konrad[badcode]\\Sensor Data\\010_Rafał Palak.csv")
emg_011 = pd.read_csv("D:\\iMotions\\Export\\Mateusz and Konrad[badcode]\\Sensor Data\\011_Krzysztof Pilarczyk.csv")
print(emg_001.groupby('SourceStimuliName')['EMG CH1 RAW'].mean())

