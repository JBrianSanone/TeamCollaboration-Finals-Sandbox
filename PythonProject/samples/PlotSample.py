import numpy as np
import matplotlib.pyplot as plt

# Define function f
def f(x, a, b, c):
    return a * np.sin(b * x) + c

def plot1():
    # Data Generation
    x = np.linspace(0, 2 * np.pi, 100)  # Use 2 * np.pi for a full sine wave
    y = np.sin(x)

    plt.plot(x, y)  # Creates the plot

    # Plot Customization
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Sine Wave Plot')

    # Display the Plot
    plt.show()

def plot2():
    xlist = np.arange(-10, 10.1, 0.1)

    a = 6
    b = 1
    c = 3
    ylist = f(xlist, a, b, c)

    plt.figure(num=0, dpi=120)
    plt.plot(xlist, ylist, label="f(x)")
    plt.plot(xlist, np.sqrt(ylist), '--g', label=r"f(x)$^{0.5}$")
    plt.title("Plotting example")
    plt.xlabel("Distance / ft")
    plt.ylabel("Height / ft")
    plt.legend()
    plt.show()

plot1()
plot2()
