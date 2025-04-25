import matplotlib.pyplot as plt

groups = ['Personalized', 'Generic']
open_rates = [31.2, 19.8]
unsubscribe_rates = [0, 1.1]

x = range(len(groups))
plt.figure(figsize=(10,5))
plt.bar(x, open_rates, width=0.4, label='Open Rate (%)', align='center')
plt.bar([p + 0.4 for p in x], unsubscribe_rates, width=0.4, label='Unsubscribe Rate (%)', align='center')
plt.xticks([p + 0.2 for p in x], groups)
plt.title('Comparison of Engagement Metrics')
plt.ylabel('Percentage (%)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()