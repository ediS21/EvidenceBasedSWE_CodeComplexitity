import pandas as pd
from scipy.stats import describe

# Load data from vlc.csv
vlc_data = pd.read_csv("vlc.csv")

# Extract relevant columns excluding 'tag'
vlc_numeric_data = vlc_data.drop(columns=['tag'])

# Perform statistical analysis for vlc.csv
vlc_statistics = vlc_numeric_data.describe().transpose()[['mean', '50%', 'std']]

# Load data from obs.csv
obs_data = pd.read_csv("obs.csv")

# Extract relevant columns excluding 'tag'
obs_numeric_data = obs_data.drop(columns=['tag'])

# Perform statistical analysis for obs.csv
obs_statistics = obs_numeric_data.describe().transpose()[['mean', '50%', 'std']]

# Display statistical analysis for vlc.csv
print("Statistical Analysis for vlc.csv:")
print(vlc_statistics)

# Display statistical analysis for obs.csv
print("\nStatistical Analysis for obs.csv:")
print(obs_statistics)

# Compare results
print("\nComparison of vlc.csv and obs.csv:")
comparison = pd.DataFrame(index=vlc_statistics.index)
comparison['vlc_mean'] = vlc_statistics['mean']
comparison['obs_mean'] = obs_statistics['mean']
comparison['vlc_median'] = vlc_statistics['50%']
comparison['obs_median'] = obs_statistics['50%']
comparison['vlc_std'] = vlc_statistics['std']
comparison['obs_std'] = obs_statistics['std']

# Display the comparison
print(comparison)
