import pandas as pd
from scipy.stats import ttest_ind

# Load the data from CSV files
obs_df = pd.read_csv('obs.csv')
#obs_df = pd.DataFrame(obs_data)
vlc_df = pd.read_csv('vlc.csv')
#vlc_df = pd.DataFrame(vlc_data)

# Extract the cyclomatic complexity values
obs_data = obs_df['aCC'].tolist()
vlc_data = vlc_df['aCC'].tolist()

# Perform t-test
t_stat, p_value = ttest_ind(obs_data, vlc_data)

# Display results
print(f'T-statistic: {t_stat}, P-value: {p_value}')

if p_value < 0.05:
    print('There is a significant difference between the two datasets.')
else:
    print('There is no significant difference between the two datasets.')
