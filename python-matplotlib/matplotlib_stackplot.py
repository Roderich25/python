from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

days = [1, 2, 3, 4, 5, 6, 7, 8, 9]

worker1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
worker2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
worker3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['Worker 1', 'Worker 2', 'Worker 3']
colors = ['#008fd5', '#fc4f30', '#6d904f']

plt.stackplot(days, worker1, worker2, worker3, labels=labels, colors=colors)

plt.legend(loc=(0.05, 0.05))

plt.title("Hours worked Stack Plot")
plt.tight_layout()
plt.show()