import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data_histogram.csv')
ids = data['Responder_id']
ages = data['Age']
bins = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
plt.hist(ages, bins=bins, edgecolor='#4c4c4c')  # log=True uses a logarithmic scale

median_age = 29
plt.axvline(median_age, color='#fc4c30', label='Median', linewidth=2)

plt.legend()
plt.title('Ages of Responders')
plt.xlabel('Age')
plt.ylabel('Total')
plt.tight_layout()
plt.savefig('histogram.png')
plt.show()
