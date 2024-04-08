import matplotlib.pyplot as plt
import random


# x_points = [1,2,3,4,5,6]
# y_points = [1,4,9,16,25,36]
# x2_points = [-3,-2,-1,0,1,2,3,4,5,6]
# y2_points = [-27,-8,-1,0,1,8,27,64,125,216]

# plt.plot(x_points, y_points, label='squares')
# plt.plot(x2_points, y2_points, label='cubes')

# plt.plot([random.randint(-10,300) for x in range(10)], 'r', label='red random')
# plt.plot([random.randint(-10,300) for x in range(10)], 'b')
# plt.plot([random.randint(-10,300) for x in range(10)], 'c')

# plt.title("Squares and Cubes")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.legend()
# plt.xlim(0,10)
# plt.show()

numbers = [random.randrange(1,10) for i in range(100)]
bin_vals = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
plt.hist(numbers, bins=bin_vals)
plt.savefig("myHistogram.png")
plt.clf()

plt.plot([1,2,3,4,5,6], [1,4,9,16,25,36])
plt.savefig("squares.png")

numbers = [random.randrange(1,10) for i in range(100)]
bins = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
plt.hist(numbers, bins=bins)
plt.savefig("counts.png")