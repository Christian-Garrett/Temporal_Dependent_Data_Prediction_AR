import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as sts
from statsmodels.tsa.seasonal import seasonal_decompose


class Stationarity:

    def __init__(self, df_comp, walk):
        self.df_comp = df_comp

        print(sts.adfuller(df_comp.wn))
        print(sts.adfuller(df_comp.IOT_Reading))
        print(sts.adfuller(walk))
        print(sts.kpss(df_comp.IOT_Reading, regression='c'))
        print(sts.kpss(df_comp.wn, regression='c'))

        self.seasonality_test(df_comp)


    def seasonality_test(self, df_comp):
        # Seasonality
        # Naive decomposition
        additive = seasonal_decompose(df_comp.IOT_Reading, model="additive")
        additive.plot()
        plt.savefig("Modular/output/"+"seasonality.png")

