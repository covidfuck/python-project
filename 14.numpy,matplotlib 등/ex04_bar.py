from matplotlib import pyplot as plt

x = ['apple', 'banana', 'kiwi', 'melon']
y = [30, 20, 40 ,75]

fig = plt.figure()

plt.bar(x, y, color = 'black')
plt.plot(x, y, color = 'orange', marker = '*')
plt.scatter(x, y)

plt.title("Fruits")
plt.xlabel("Quantity")
plt.ylabel("price")

plt.show()