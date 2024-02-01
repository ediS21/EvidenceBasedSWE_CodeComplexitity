from scipy.stats import shapiro
import pandas as pd

# load data into Pandas DataFrames
obs_data = pd.read_csv('obs.csv')['sCCN']
vlc_data = pd.read_csv('vlc.csv')['sCCN']

# Shapiro-Wilk test for OBS data
stat_obs, p_value_obs = shapiro(obs_data)
print("Shapiro-Wilk test for OBS data:")
print(f"Test Statistic: {stat_obs}, p-value: {p_value_obs}")

# Shapiro-Wilk test for VLC data
stat_vlc, p_value_vlc = shapiro(vlc_data)
print("\nShapiro-Wilk test for VLC data:")
print(f"Test Statistic: {stat_vlc}, p-value: {p_value_vlc}")
