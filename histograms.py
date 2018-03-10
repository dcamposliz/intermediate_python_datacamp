import matplotlib.pyplot as plt

x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

y_data = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print("x_data =", x_data)
print("y_data =", y_data)

plt.plot(x_data, y_data)
plt.show()

plt.hist(x_data)
plt.show()
