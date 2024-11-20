import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
import numpy as np
import pandas as pd




class WhiteNoise:

    def __init__(self, df_comp):

        self.df_comp = df_comp

        # Generate Random Whitenoise data
        self.generate_whitenoise()

        # plot comparison data
        self.plot_data_comparison()

        # plot autocorrelation
        self.autocorrelation_plot()


    def autocorrelation_plot(self):

        autocorrelation_plot(self.df_comp.IOT_Reading)
        plt.savefig("Modular/output/"+"autocorrelationIOT.png")

        # Plot shows pos correlation with lag values but there is no significant relationship. 
        # No cycles/trends
        autocorrelation_plot(self.df_comp.wn)
        plt.savefig("Modular/output/"+"WN.png")


    def plot_data_comparison(self):

        # Fixes the the illustration output issue
        df = pd.DataFrame({'IOT_Reading' : self.df_comp.IOT_Reading}, index=self.df_comp.index)
        df.plot(figsize=(20,5))

        self.df_comp.wn.plot(figsize=(20,5))
        plt.title("White noise time-series", size=24)
        plt.savefig("Modular/output/"+"whitenoise.png")
        self.df_comp.IOT_Reading.plot(figsize=(20,5))
        plt.title("IOT_Reading_Series", size=24)
        plt.savefig("Modular/output/"+"IOT_Reading.png")
        self.df_comp.wn.plot(figsize=(20,5))
        self.df_comp.IOT_Reading.plot(figsize=(20,5))
        plt.title("White noise vs IOT_Reading Series", size=24)
        plt.savefig("Modular/output/"+"compWNvsIOT.png")


    def generate_whitenoise(self):

        wn = np.random.normal(loc=self.df_comp.IOT_Reading.mean(),
                              scale=self.df_comp.IOT_Reading.std(),
                              size=len(self.df_comp))
        self.df_comp["wn"] = wn


