from pathlib import Path
import os
import sys
import pandas as pd

module_path = Path(__file__).parents[1]
sys.path.append(str(module_path))

from scipy.stats.distributions import chi2
import statsmodels.tsa.arima.model as tsa


class DataPipeline:
    from MLPipeline.Preprocess import (plot_data,
                                       reshape_data,
                                       fill_missing_values,
                                       set_freq,
                                       set_date_index,
                                       plot_QQPlots)
    from MLPipeline.WhiteNoise import (plot_autocorrelation,
                                       plot_data_comparison,
                                       generate_whitenoise)
    from MLPipeline.RandomWalk import generate_randomwalk
    from MLPipeline.Stationarity import check_stationarity
    from MLPipeline.AcfAndPacf import (plot_acf,
                                       plot_pacf)



    def __init__(self, data_path):
        self.data_path=data_path
        self.data=pd.read_csv(os.path.join(module_path, 
                                           "input/Data-Chillers.csv"))
        self.model_list=[]

    def preprocess_data(self):     
        self.plot_data()  # Plotting the data as line plots
        self.plot_QQPlots()  # Plotting the data as QQPlots
        self.set_date_index()  # Changing the data to datetime format
        self.set_freq()  # Setting the frequency
        self.fill_missing_values()  # Filling the missing values
        self.reshape_data()  # Reshape univariate data

    def perform_EDA(self):
        self.generate_whitenoise()
        self.plot_data_comparison()
        self.plot_autocorrelation()
        self.generate_randomwalk()
        self.check_stationarity()
        self.plot_acf()
        self.plot_pacf()

    def train_models(self):
        self.model_list=[(tsa.ARIMA(self.data.IOT_Reading, order=(x,0,0))) for x in range(1,5)]
    
    def evaluate_models(self):
        report_list=[model.fit() for model in self.model_list]
        for report in report_list:
            print(report.summary())

        for i in range(len(report_list)-1):
            print(self.LLR_Test(report_list[i].llf, 
                                report_list[i+1].llf))

    @classmethod
    def LLR_Test(self, model_1, model_2, DF=1):
        L1 = model_1
        L2 = model_2
        LR = (2*(L2-L1))
        p = chi2.sf(LR, DF).round(3)
        return p
