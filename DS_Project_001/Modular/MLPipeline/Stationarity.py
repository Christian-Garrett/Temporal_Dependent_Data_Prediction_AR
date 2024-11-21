import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as sts
from statsmodels.tsa.seasonal import seasonal_decompose


def check_stationarity(self):
    print(sts.adfuller(self.data.wn))
    print(sts.adfuller(self.data.IOT_Reading))
    print(sts.adfuller(self.walk))
    print(sts.kpss(self.data.IOT_Reading, regression='c'))
    print(sts.kpss(self.data.wn, regression='c'))

    additive = seasonal_decompose(self.data.IOT_Reading, model="additive")
    additive.plot()
    plt.savefig("Modular/output/"+"seasonality.png")
