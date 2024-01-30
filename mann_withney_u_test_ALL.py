from scipy.stats import mannwhitneyu
import pandas as pd
from itertools import combinations

# Loadr data into Pandas DataFrames
dataset_names = ['obs', 'vlc', 'freebsd', 'sortix', 'linux', 'llvm', 'gcc']

# Create a list to hold the datasets
# Choose between aNCSS,aCC,aFunctions,sNCSS,sCCN,sFunctions
datasets = [pd.read_csv(f'{name}.csv')['aNCSS'] for name in dataset_names]

# Open a file for writing
with open('mann_whitney_results.txt', 'w') as result_file:
    # Perform pairwise Mann-Whitney U tests
    for pair in combinations(range(len(datasets)), 2):
        dataset1 = datasets[pair[0]]
        dataset2 = datasets[pair[1]]
        
        # Perform Mann-Whitney U test
        statistic, p_value = mannwhitneyu(dataset1, dataset2)
        
        # Output results to the file
        print(f"Mann-Whitney U test between {dataset_names[pair[0]]} and {dataset_names[pair[1]]}:", file=result_file)
        print(f"Test Statistic: {statistic}, p-value: {p_value}", file=result_file)

        # Interpret the results
        alpha = 0.05
        if p_value < alpha:
            print("Reject the null hypothesis. There is a significant difference between the datasets.", file=result_file)
        else:
            print("Fail to reject the null hypothesis. There is no significant difference between the datasets.", file=result_file)
        print("", file=result_file)  # Add an empty line for better readability
