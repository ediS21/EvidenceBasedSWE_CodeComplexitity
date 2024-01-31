import pandas as pd

discard = {
    'freebsd': ['cvs'],
    'gcc': [],
    'linux': ['rc'],
    'llvm': ['rc', 'init'],
    'obs': ['rc','beta'],
    'sortix': [],
    'vlc': ['test', 'pre', 'rc', 'ff', 'git']
}
for key in discard.keys():
    pd_file = pd.read_csv(f'{key}.csv')
    discard_list = discard[key]
    if discard_list:
        cleaned = pd_file[~pd_file.tag.str.contains('|'.join(discard_list))]
        cleaned.to_csv(f'{key}-cleaned.csv', index=False)