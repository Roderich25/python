import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data_fillbetween.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')
plt.plot(ages, py_salaries, label='Python')

overall_median = 57_287
# plt.fill_between(ages, py_salaries, alpha=0.25) # Default third argument is zero
# plt.fill_between(ages, py_salaries, overall_median, alpha=0.25) # Filling up and down the oveall median
plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries > overall_median),
                 interpolate=True, alpha=0.25, label='Above Overall Median')
plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries < overall_median),
                 interpolate=True, color='red', alpha=0.25, label='Below Overall Median')
plt.xlabel('Ages')
plt.ylabel('USD')
plt.title('Median Salary by Age')

plt.legend()
plt.tight_layout()
plt.savefig('fillbetween.png')
plt.show()
