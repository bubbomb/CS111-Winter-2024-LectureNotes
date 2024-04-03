import random
import matplotlib.pyplot as plt


# x_points = [1,2,3,4,5,6]
# y_points = [1,4,9,16,25,36]

# plt.plot(x_points, y_points)
# plt.show()


# x_points = [1,2,3,4,5,6]
# y_points = [1,4,9,16,25,36]
# x2_points = [-3,-2,-1,0,1,2,3,4,5,6]
# y2_points = [-27,-8,-1,0,1,8,27,64,125,216]

# plt.plot(x_points, y_points, label='Squares')
# plt.plot(x2_points, y2_points, 'r', label="Cubes")

# plt.title("Squares and Cubes")
# plt.xlabel("x")
# plt.ylabel("f(x)")

# plt.legend()
# plt.show()



# labels = ["M","T","W","Th","F","Sa","Su"]
# values = [3,8,7,9,15,22,14]

# plt.bar(labels, values)

# plt.show()

# numbers = [random.randrange(1,10) for i in range(100)]
# plt.hist(numbers)
# plt.hist(numbers, bins=9)
# plt.show()


# bin_vals = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
# plt.hist(numbers, bins=bin_vals)
# plt.savefig("myHistogram.png")


plt.plot([1,2,3,4,5,6], [1,4,9,16,25,36])
plt.savefig("squares.png")
plt.clf()

numbers = [random.randrange(1,10) for i in range(100)]
bins = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
plt.hist(numbers, bins=bins)
plt.savefig("counts.png")

