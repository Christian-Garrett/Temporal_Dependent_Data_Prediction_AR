import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
import numpy as np
import pandas as pd


def generate_whitenoise(self):

    wn = np.random.normal(loc=self.data.IOT_Reading.mean(),
                            scale=self.data.IOT_Reading.std(),
                            size=len(self.data))
    self.data["wn"] = wn


def plot_data_comparison(self):

    df = pd.DataFrame({'IOT_Reading' : self.data.IOT_Reading}, index=self.data.index)
    df.plot(figsize=(20,5))

    self.data.wn.plot(figsize=(20,5))
    plt.title("White noise time-series", size=24)
    plt.savefig("Modular/output/"+"whitenoise.png")
    self.data.IOT_Reading.plot(figsize=(20,5))
    plt.title("IOT_Reading_Series", size=24)
    plt.savefig("Modular/output/"+"IOT_Reading.png")
    self.data.wn.plot(figsize=(20,5))
    self.data.IOT_Reading.plot(figsize=(20,5))
    plt.title("White noise vs IOT_Reading Series", size=24)
    plt.savefig("Modular/output/"+"compWNvsIOT.png")


def plot_autocorrelation(self):

    autocorrelation_plot(self.data.IOT_Reading)
    plt.savefig("Modular/output/"+"autocorrelationIOT.png")

    # Plot shows pos correlation with lag values but there is no significant relationship. 
    autocorrelation_plot(self.data.wn)
    plt.savefig("Modular/output/"+"WN.png")
