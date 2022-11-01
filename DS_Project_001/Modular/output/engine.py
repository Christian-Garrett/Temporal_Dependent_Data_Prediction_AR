import pandas as pd
import seaborn as sns
sns.set()

import sys; print(sys.path)


from Modular.MLPipeline.WhiteNoise import WhiteNoise
from Modular.MLPipeline.Preprocess import Preprocess
from Modular.MLPipeline.AcfAndPacf import AcfAndPcf
from Modular.MLPipeline.AutoRegressor import AutoRegressor
from Modular.MLPipeline.RandomWalk import RandomWalk
from Modular.MLPipeline.RollingWindow import RollingWindow
from Modular.MLPipeline.Stationarity import Stationarity

def run():
    # importing the data
    raw_csv_data = pd.read_csv("Modular/input/Data-Chillers.csv")

    df_comp = raw_csv_data.copy()

    # Preprocess
    prep = Preprocess(df_comp)

    # White Noise
    wnoise = WhiteNoise(prep.df_comp)

    # Random Walk
    wlk = RandomWalk()

    # Stationarity
    Stationarity(wnoise.df_comp, wlk.walk)

    # ACF and PCF
    AcfAndPcf(wnoise.df_comp)

    # AutoRegressor
    AutoRegressor(wnoise.df_comp)

    # Rolling Window
    RollingWindow(wnoise.df_comp)



run()

