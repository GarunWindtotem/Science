import matplotlib.pyplot as plt
import numpy as np
# Set up the scatter plot
fig, ax = plt.subplots(1,1, figsize=(10,10))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Circle')

# Radius of the circle
r = 1
# Number of points to use
n = 1000
# Create a list of points that form the circle
points = []
for i in range(n):
    angle = 2 * np.pi * i / n
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    points.append((x, y))
# Unpack the points into separate lists of x and y coordinates
x, y = zip(*points)
# Plot the points
ax.scatter(x, y, c='b', s=2)
# Plot the point
ax.scatter(x=0, y=0, c='r', s=10)
# Show the plot
plt.show()





