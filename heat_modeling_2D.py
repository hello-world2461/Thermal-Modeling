import numpy as np
import matplotlib.pyplot as plt

# defining vars 
thermal_dif = 110
length = 30     # in mm
time = 3        # in sec
nodes = 50

dx = length / nodes
dy = length / nodes
dt = min( ((dx**2) / (4 * thermal_dif)) , ((dy**2) / (4 * thermal_dif)) )
t_nodes = int(time/dt)

# Define initial temperature (u IS THE ROD) 
init_temp = 20
u = np.zeros((nodes, nodes)) + init_temp

# Define boundary conditions
u[0, :] = 100      # temp at bottom side of rod
u[-1, :] = 100     # temp at top side of rod

u[:, 0] = 100     # temp at left side of rod
u[:, -1] = 100     # temp at right side of rod

# Visualize the plot
fig, axis = plt.subplots()
pcm = axis.pcolormesh(u, cmap=plt.cm.jet , vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)

# Simulation
counter = 0

# Loop for iterating over time
while counter < time:
    w = u.copy()

    # Loop for calculating temp in x
    for x in range(1, nodes - 1):
        for y in range(1, nodes - 1):
            
            dd_ux = (w[x-1, y] - 2*w[x, y] + w[x+1, y]) / dx**2
            dd_uy = (w[x, y-1] - 2*w[x, y] + w[x, y+1]) / dy**2

            u[x, y] = dt * thermal_dif * (dd_ux + dd_uy) + w[x,y]

    counter += dt   #add delta t

    print("t: {:.3f} [s], Avg temp: {:.2f} Celcius".format(counter, np.average(u)))

    # update the plot
    pcm.set_array(u)
    axis.set_title("distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.1)

plt.show()