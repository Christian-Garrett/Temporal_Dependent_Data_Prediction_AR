from pathlib import Path
import os
import sys
import pandas as pd

module_path = Path(__file__).parents[1]
sys.path.append(str(module_path))

from scipy.stats.distributions import chi2
import statsmodels.tsa.arima.model as tsa


class DataPipeline:
    """
    A class used to create the data pipeline.
    ...

    Attributes
    ----------
    data_path : str
        Time series input data text path
    data : df
        Time series input data
    model_list : list
        List of 4 AR models for comparison

    Methods
    -------
    preprocess_data()
        Load data, set index, change formats, visual sanity checks.
    perform_EDA()
        Check for stationarity, examine autocorrelation attributes.
    train_models()
        Train 4 autoregression models for comparison.
    evaluate_models()
        Compare models using LLR test and examine rolling/expanding windows.

    """
    from MLPipeline.Preprocess import (plot_line_graphs,
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
    from MLPipeline.RollingWindow import check_windows


    def __init__(self, data_path):

        self.data_path=data_path
        self.data=pd.read_csv(os.path.join(module_path, 
                                           "input/Data-Chillers.csv"))
        self.model_list=[]

    def preprocess_data(self):   

        self.plot_line_graphs()
        self.plot_QQPlots()
        self.set_date_index()
        self.set_freq()
        self.fill_missing_values()
        self.reshape_data()

    def perform_EDA(self):

        self.generate_whitenoise()
        self.plot_data_comparison()
        self.plot_autocorrelation()
        self.generate_randomwalk()
        self.check_stationarity() # Compared to white noise and randomwalk 
        self.plot_acf()
        self.plot_pacf()

    def train_models(self):

        self.model_list=[(tsa.ARIMA(self.data.IOT_Reading, order=(x,0,0))) for x in range(1,5)]
    
    def evaluate_models(self):
        
        report_list=[model.fit() for model in self.model_list]
        for i in range(len(report_list)):
            print(report_list[i].summary())
            None if i==0 else print(self.LLR_Test(report_list[i-1].llf, report_list[i].llf))

        self.check_windows()

    @classmethod
    def LLR_Test(self, model_1, model_2, DF=1):
        L1 = model_1
        L2 = model_2
        LR = (2*(L2-L1))
        p = chi2.sf(LR, DF).round(3)
        return p
