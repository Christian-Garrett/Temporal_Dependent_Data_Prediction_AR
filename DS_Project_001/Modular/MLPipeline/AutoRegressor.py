# from statsmodels.tsa.arima_model import ARMA
from scipy.stats.distributions import chi2

# import statsmodels.tsa.api as tsa
# import statsmodels.api as sm

import statsmodels.tsa.arima.model as tsa


class AutoRegressor:

    def __init__(self, df_comp):

        self.df_comp = df_comp

        self.model_ar = tsa.ARIMA(self.df_comp.IOT_Reading, order=(1,0,0))
        self.model_ar_2 = tsa.ARIMA(self.df_comp.IOT_Reading, order=(2,0,0))
        self.model_ar_3 = tsa.ARIMA(self.df_comp.IOT_Reading, order=(3,0,0))
        self.model_ar_4 = tsa.ARIMA(self.df_comp.IOT_Reading, order=(4,0,0))

        # Print the ARMA model results
        self.results_ar = self.model_ar.fit()
        print(self.results_ar.summary())
        self.results_ar_2 = self.model_ar_2.fit()
        print(self.results_ar_2.summary())
        self.results_ar_3 = self.model_ar_3.fit()
        print(self.results_ar_3.summary())
        self.results_ar_4 = self.model_ar_4.fit()
        print(self.results_ar_4.summary())

        # Print the LLR Tests
        print(self.LLR_Test(self.results_ar.llf, self.results_ar_2.llf))
        print(self.LLR_Test(self.results_ar_2.llf, self.results_ar_3.llf))
        print(self.LLR_Test(self.results_ar_3.llf, self.results_ar_4.llf))


    @classmethod
    def LLR_Test(self, model_1, model_2, DF=1):
        L1 = model_1
        L2 = model_2
        LR = (2*(L2-L1))
        p = chi2.sf(LR, DF).round(3)
        return p