import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot


class RandomWalk:

    def __init__(self):

        walk = [99]

        for i in range(1900):
            # Create random noise
            noise = -1 if np.random.random() < 0.5 else 1
            walk.append(walk[-1] + noise)

        plt.plot(walk)
        plt.savefig("Modular/output/"+"randomwalk.png")

        autocorrelation_plot(walk)
        plt.savefig("Modular/output/randomwalkAutocorrelation.png")
        self.walk = walk
