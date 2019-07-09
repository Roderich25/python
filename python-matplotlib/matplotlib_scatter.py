import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data_scatter.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']
plt.scatter(view_count, likes, c=ratio, cmap='summer',
            edgecolor='#4c4c4c', linewidths=1, alpha=0.75)
plt.xscale('log')
plt.yscale('log')

cbar = plt.colorbar()
cbar.set_label('Like/Dislike ratio')

plt.title('Trending Videos')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.tight_layout()
plt.savefig('scatter.png')
plt.show()
