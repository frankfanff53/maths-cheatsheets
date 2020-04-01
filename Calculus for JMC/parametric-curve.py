# this is the code for plotting the parametric graph:
import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot a graph for a given interval
def graph_plotting(start, end, interval, marking):
    x_value = []
    y_value = []
    for t in np.arange(start, end, interval):
        x = t ** 2
        y = t ** 3 - t
        x_value.append(x)
        y_value.append(y)
    plt.plot(x_value, y_value, '-', label = marking)

graph_plotting(-1.5, 0, 0.0005, "t < 0")
graph_plotting(0, 1.5, 0.0005, "t > 0")

# plot arrows to demonstrate the direction of the change of t
def arrow_ploting(start, end, interval):
    for t in np.arange(start, end, interval):
        x = t ** 2
        y = t ** 3 - t
        if t >= 0:
            dx = (t + 0.0000001) ** 2 - x
            dy = (t + 0.0000001) ** 3 - (t + 0.0000001) - y
        else:
            dx = (t - 0.0000001) ** 2 - x
            dy = (t - 0.0000001) ** 3 - (t - 0.0000001) - y
        
        plt.quiver(x, y, dx, dy, color = "r", width = 0.005)

arrow_ploting(-1.5, 1.5, 0.4)

# plot reference lines to the graph
plt.axvline(0, color = 'gray', linestyle = '--', alpha = 0.8)
plt.axhline(0, color = 'gray', linestyle = '--', alpha = 0.8)

# plot special points on the graph
special_points = [(0, 0), (1, 0), (1 / 3, -2 * math.sqrt(3) / 9), 
(1 / 3, 2 * math.sqrt(3) / 9), (1 / 9, 8 / 27)]

plt.scatter(*zip(*special_points))

for point in special_points:
    x0 = point[0]
    y0 = point[-1]
    ax.text(x0, y0, 
    "(" + str(round(x0, 3)) + "," + str(round(y0, 3)) + ")", 
    fontsize = 7, color = "black", style = "italic", 
    weight = "light")

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()