from matplotlib import pyplot as plt

x = ['apple', 'banana', 'kiwi']
y = [10, 5, 7]

plt.plot(x, y, color = '#42f5aa', marker = 'v', linestyle = 'dotted')

plt.title('Fruit')
plt.xlabel('Name')
plt.ylabel('Quantity')

plt.show()
