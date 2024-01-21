import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('injury.csv')
# x = list(df['Season'])
# y = list(df['Number of injuries'])

plt.scatter(df['Season'],df['Number of injuries'])
plt.title('Line Plot of DataFrame Values')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
