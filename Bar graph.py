import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('Instagram_Data.csv')

x = df['User ID']
y = df['Likes']





plt.xlabel('User ID', fontsize=18)
plt.ylabel('Likes', fontsize=16)
plt.bar(x, y)

plt.show()