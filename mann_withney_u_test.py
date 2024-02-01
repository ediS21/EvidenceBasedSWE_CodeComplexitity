from scipy.stats import mannwhitneyu
import pandas as pd

# Assuming you have loaded your data into Pandas DataFrames
# Choose between aNCSS,aCC,aFunctions,sNCSS,sCCN,sFunctions
obs_data = pd.read_csv('obs.csv')['sNCSS']
vlc_data = pd.read_csv('vlc.csv')['sNCSS']

# Perform Mann-Whitney U test
statistic, p_value = mannwhitneyu(obs_data, vlc_data)
print("Mann-Whitney U test:")
print(f"Test Statistic: {statistic}, p-value: {p_value}")

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("\nReject the null hypothesis. There is a significant difference between OBS and VLC data.")
else:
    print("\nFail to reject the null hypothesis. There is no significant difference between OBS and VLC data.")
