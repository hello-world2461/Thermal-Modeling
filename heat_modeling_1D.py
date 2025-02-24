import numpy as np
import matplotlib.pyplot as plt

# defining vars 
thermal_dif = 110
length = 50     # in mm
time = 10        # in sec
nodes = 10

dx = length / nodes
dt = 0.5 * (dx**2) / thermal_dif
t_nodes = int(time/dt)

# Define initial temperature (u IS THE ROD) 
init_temp = 20
u = np.zeros(nodes) + init_temp

# Define boundary conditions
u[0] = 100      # temp at left side of rod
u[-1] = 100     # temp at right side of rod

# Visualize the plot
fig, axis = plt.subplots()
pcm = axis.pcolormesh([u], cmap=plt.cm.jet , vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)

# Simulation
counter = 0

# Loop for iterating over time
while counter < time:
    w = u.copy()

    # Loop for calculating temp at each node
    for i in range(1, nodes - 1):

        u[i] = dt * thermal_dif * (w[i-1] - 2*w[i] + w[i+1]) / dx ** 2 + w[i]

    counter += dt   #add delta t

    print("t: {:.3f} [s], Avg temp: {:.2f} Celcius".format(counter, np.average(u)))

    # update the plot
    pcm.set_array([u])
    axis.set_title("distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.1)

plt.show()