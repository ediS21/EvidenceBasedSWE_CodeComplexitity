import pandas as pd
import matplotlib.pyplot as plt

#CHANGE CSV FILE TO DESIRED ONE
data = pd.read_csv("gcc.csv") 
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
plt.plot(aCC, tag, marker='o', color='b', alpha=0.7)
plt.title('GCC Average cyclomatic complexity per file')
plt.xlabel('cyclomatic complexity')
plt.ylabel('tag')
plt.grid(True)
plt.show()

#scatter graph
plt.figure(figsize=(12, 10))
plt.scatter(aCC, tag, marker='o', color='b', alpha=0.7)
plt.title('GCC scatter plot average cyclomatic complexity per file')
plt.xlabel('cyclomatic complexity')
plt.ylabel('tag')
plt.show()


