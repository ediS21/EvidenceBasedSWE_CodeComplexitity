import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import norm

#CHANGE CSV FILE TO DESIRED ONE
data = pd.read_csv("vlc.csv") 
#print(data.columns)
df = pd.DataFrame(data)
print(df.columns)

#variables to plot - these are in the header of each csv file
tag = df['tag']
aNCSS = df['aNCSS'] 
aCC = df['aCC'] 
aFunctions = df['aFunctions']
sNCSS = df['sNCSS']
sCCN = df['sCCN']
sFunctions = df['sFunctions']

#plot graph
plt.figure(figsize=(12, 10))
plt.plot(aNCSS, tag, marker='o', color='b', alpha=0.7)
plt.title('VLC Studio Average number of lines of code per file')
plt.xlabel('lines of code')
plt.ylabel('tag')
plt.grid(True)
#plt.show()

#plot graph
plt.figure(figsize=(12, 10))
plt.plot(aCC, tag, marker='o', color='b', alpha=0.7)
plt.title('VLC Studio Average cyclomatic complexity per file')
plt.xlabel('cyclomatic complexity')
plt.ylabel('tag')
plt.grid(True)
#plt.show()

#plot graph
plt.figure(figsize=(12, 10))
plt.plot(aFunctions, tag, marker='o', color='b', alpha=0.7)
plt.title('VLC Studio Average number of functions per file')
plt.xlabel('number of functions')
plt.ylabel('tag')
plt.grid(True)
#plt.show()

#plot graph
plt.figure(figsize=(12, 10))
plt.plot(sNCSS, tag, marker='o', color='b', alpha=0.7)
plt.title('VLC Studio Sum of number of lines of code per file')
plt.xlabel('number of lines of code')
plt.ylabel('tag')
plt.grid(True)
#plt.show()

#plot graph
plt.figure(figsize=(12, 10))
plt.plot(sCCN, tag, marker='o', color='b', alpha=0.7)
plt.title('VLC Studio Sum of cyclomatic complexity per file')
plt.xlabel('cyclomatic complexity')
plt.ylabel('tag')
plt.grid(True)
#plt.show()

#plot graph
plt.figure(figsize=(12, 10))
plt.plot(sFunctions, tag, marker='o', color='b', alpha=0.7)
plt.title('VLC Studio Sum of number of functions per file')
plt.xlabel('number of functions')
plt.ylabel('tag')
plt.grid(True)
#plt.show()

# Plot histogram
plt.subplot(2, 2, 3)
sns.histplot(sNCSS, bins=30, kde=True, color='skyblue')
plt.title('Histogram of Average number of lines of code per file')
plt.xlabel('Lines of Code')
plt.ylabel('Frequency')
plt.grid(True)
#plt.show()

# QQ plot
plt.subplot(2, 2, 4)
sm.qqplot(sNCSS, line='s', fit=True)
plt.title('QQ Plot of Average number of lines of code per file')
plt.grid(True)

plt.tight_layout()
plt.show()

#scatter graph
#plt.figure(figsize=(12, 10))
#plt.scatter(aCC, tag, marker='o', color='b', alpha=0.7)
#plt.title('GCC scatter plot average cyclomatic complexity per file')
#plt.xlabel('cyclomatic complexity')
#plt.ylabel('tag')
#plt.show()


