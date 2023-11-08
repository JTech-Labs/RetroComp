import numpy as np
import matplotlib.pyplot as plt

# Create an array of theta values in degrees
ThetaDegrees = np.linspace(0, 113*360, 10000)

# Convert degrees to radians
ThetaRadians = np.deg2rad(ThetaDegrees)

#Calculate z(theta) using the formula, 1j is maginary number
z = np.exp(ThetaRadians *1j) + np.exp(np.pi * ThetaRadians *1j)

# Separate the real and imaginary parts of z
x = np.real(z)
y = np.imaj(z)

# Create a plot with specific settings
plt.figure(figsize=(10,10)) # Set a square figure
plt.plot(x, y, color='white', linewidth=0.5) # Set line colour to white and line width to 0.5

plt.gca().set_facecolor('black') # Set background color to black
plt.gca().set_aspect('equal') # Equal aspect ratio
plt.grid(False) # Turn off the grids
plt.xlim(-2.5, 2.5) # X-axis limit
plt.ylim(-2.5, 2.5) # Y-axis limit

plt.show() # Display the plot