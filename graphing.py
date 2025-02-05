import numpy as np
import matplotlib.pyplot as plt

# Load the residues list from the text file
residues = []
with open('residues.txt', 'r') as file:
    for line in file:
        # Assuming each line in the file is a string representation of a NumPy array
        residues.append(np.fromstring(line.strip(), sep=' '))

# Load the past array from the binary file
past = np.load('past_array.npy', allow_pickle=True)

# Create three 2D matrices to store the first, second, and third subelements
pressures = np.empty_like(past, dtype=np.float64)
u_speeds = np.empty_like(past, dtype=np.float64)
v_speeds = np.empty_like(past, dtype=np.float64)
x_coords = np.empty_like(past, dtype=np.float64)
y_coords = np.empty_like(past, dtype=np.float64)

# Loop over each element in the past matrix to extract the corresponding subelements
for i in range(past.shape[0]):  # Iterate over rows
    for j in range(past.shape[1]):  # Iterate over columns
        pressures[i, j] = past[i, j][0]  # First subelement
        u_speeds[i, j] = past[i, j][1]  # Second subelement
        v_speeds[i, j] = past[i, j][2]  # Third subelement
        x_coords[i, j] = past[i, j][3]
        y_coords[i, j] = past[i, j][4]

# Assuming 'u_speeds', 'x_coords', and 'y_coords' arrays are already available

# Create the grid using x_coords and y_coords
x_vals = np.unique(x_coords)
y_vals = np.unique(y_coords)

# Generate a 2D grid based on unique x and y coordinates
X, Y = np.meshgrid(x_vals, y_vals)

# Initialize an empty grid for u_speeds
u_speeds_grid = np.zeros((len(y_vals), len(x_vals)))

# Map the u_speeds values to their correct coordinates
for i in range(len(x_coords)):
    x_index = np.searchsorted(x_vals, x_coords[i])
    y_index = np.searchsorted(y_vals, y_coords[i])
    u_speeds_grid[y_index, x_index] = u_speeds[i]

# Plot using pcolormesh
plt.figure(figsize=(10, 5))
plt.pcolormesh(X, Y, u_speeds_grid, cmap='jet', shading='auto')
plt.colorbar(label='u_speed (m/s)')
plt.title('Horizontal Velocity (u_speed)')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable='box')  # Ensure axes are proportional
plt.show()


# Initialize an empty grid for u_speeds
v_speeds_grid = np.zeros((len(y_vals), len(x_vals)))

# Map the u_speeds values to their correct coordinates
for i in range(len(x_coords)):
    x_index = np.searchsorted(x_vals, x_coords[i])
    y_index = np.searchsorted(y_vals, y_coords[i])
    v_speeds_grid[y_index, x_index] = v_speeds[i]

# Plot using pcolormesh
plt.figure(figsize=(10, 5))
plt.pcolormesh(X, Y, v_speeds_grid, cmap='jet', shading='auto')
plt.colorbar(label='u_speed (m/s)')
plt.title('Vertical Velocity (u_speed)')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable='box')  # Ensure axes are proportional
plt.show()

# Initialize an empty grid for u_speeds
pressures_grid = np.zeros((len(y_vals), len(x_vals)))

# Map the u_speeds values to their correct coordinates
for i in range(len(x_coords)):
    x_index = np.searchsorted(x_vals, x_coords[i])
    y_index = np.searchsorted(y_vals, y_coords[i])
    pressures_grid[y_index, x_index] = pressures[i]

# Plot using pcolormesh
plt.figure(figsize=(10, 5))
plt.pcolormesh(X, Y, pressures_grid, cmap='jet', shading='auto')
plt.colorbar(label='Pressure')
plt.title('Pressure')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable='box')  # Ensure axes are proportional
plt.show()


# Replace 'data.txt' with your filename
data = np.loadtxt('residues.txt')


# Assuming the file has three columns:
var1 = data[:, 0]
var2 = data[:, 1]
var3 = data[:, 2]

# Create an iteration number vector (starting from 1)
iterations = np.arange(1, data.shape[0] + 1)

# Plot the variables
plt.figure(figsize=(10, 6))
plt.plot(iterations, var1, label='P Residue')
plt.plot(iterations, var2, label='U Residue')
plt.plot(iterations, var3, label='V Residue')

# Set y-axis to logarithmic scale
plt.yscale('log')

# Labeling the plot
plt.xlabel('Iteration Number')
plt.ylabel('Residue')
plt.title('Residue values')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Display the plot
plt.show()
