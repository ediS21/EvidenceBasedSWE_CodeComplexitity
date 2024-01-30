import pandas as pd
import matplotlib.pyplot as plt

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
plt.show()

#plot graph
plt.figure(figsize=(12, 10))
plt.plot(aCC, tag, marker='o', color='b', alpha=0.7)
plt.title('VLC Studio Average cyclomatic complexity per file')
plt.xlabel('cyclomatic complexity')
plt.ylabel('tag')
plt.grid(True)
plt.show()

#plot graph
plt.figure(figsize=(12, 10))
plt.plot(aFunctions, tag, marker='o', color='b', alpha=0.7)
plt.title('VLC Studio Average number of functions per file')
plt.xlabel('number of functions')
plt.ylabel('tag')
plt.grid(True)
plt.show()

#plot graph
plt.figure(figsize=(12, 10))
plt.plot(sNCSS, tag, marker='o', color='b', alpha=0.7)
plt.title('VLC Studio Sum of number of lines of code per file')
plt.xlabel('number of lines of code')
plt.ylabel('tag')
plt.grid(True)
plt.show()

#plot graph
plt.figure(figsize=(12, 10))
plt.plot(sCCN, tag, marker='o', color='b', alpha=0.7)
plt.title('VLC Studio Sum of cyclomatic complexity per file')
plt.xlabel('cyclomatic complexity')
plt.ylabel('tag')
plt.grid(True)
plt.show()

#plot graph
plt.figure(figsize=(12, 10))
plt.plot(sFunctions, tag, marker='o', color='b', alpha=0.7)
plt.title('VLC Studio Sum of number of functions per file')
plt.xlabel('number of functions')
plt.ylabel('tag')
plt.grid(True)
plt.show()

#scatter graph
#plt.figure(figsize=(12, 10))
#plt.scatter(aCC, tag, marker='o', color='b', alpha=0.7)
#plt.title('GCC scatter plot average cyclomatic complexity per file')
#plt.xlabel('cyclomatic complexity')
#plt.ylabel('tag')
#plt.show()


