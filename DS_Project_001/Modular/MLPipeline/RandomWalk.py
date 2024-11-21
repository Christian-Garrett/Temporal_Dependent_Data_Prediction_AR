import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot


def generate_randomwalk(self):

        walk = [99]  # Initial value of the walk
        walk.extend(walk[-1] + (-1 if np.random.random() < 0.5 else 1) for _ in range(1900))


        plt.plot(walk)
        plt.savefig("Modular/output/"+"randomwalk.png")

        autocorrelation_plot(walk)
        plt.savefig("Modular/output/randomwalkAutocorrelation.png")
        self.walk = walk
