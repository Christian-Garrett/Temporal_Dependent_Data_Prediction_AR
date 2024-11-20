import statsmodels.graphics.tsaplots as sgt
import matplotlib.pyplot as plt


class AcfAndPcf:

    def __init__(self, df_comp):

        self.df_comp = df_comp

        # Plot the Acf illustration
        self.plot_acf()

        # Plot the Pacf illustration
        self.plot_pacf()


    def plot_acf(self):

        sgt.plot_acf(self.df_comp.IOT_Reading, lags=40, zero=False)
        plt.title("ACF IOT_Reading")
        plt.savefig("Modular/output/"+"ACF_IOT_Reading.png")

        sgt.plot_acf(self.df_comp.wn, lags=40, zero=False)
        plt.title("ACF White Noise")
        plt.savefig("Modular/output/"+"ACF_WhiteNoise.png")

    def plot_pacf(self):

        sgt.plot_pacf(self.df_comp.IOT_Reading, lags=40, zero=False, method=("ols"))
        plt.title("PACF IOT Reading")
        plt.savefig("Modular/output/"+"PACF_IOT_Reading.png")

        sgt.plot_pacf(self.df_comp.wn, lags=40, zero=False, method=("ols"))
        plt.title("PACF White Noise")
        plt.savefig("Modular/output/"+"PACF_wn.png")

