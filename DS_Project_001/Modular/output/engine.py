import pandas as pd
import seaborn as sns
from pathlib import Path
import os
import sys
sns.set()

module_path = Path(__file__).parents[1]
sys.path.append(str(module_path))

from MLPipeline.WhiteNoise import WhiteNoise
from MLPipeline.Preprocess import Preprocess
from MLPipeline.AcfAndPacf import AcfAndPcf
from MLPipeline.AutoRegressor import AutoRegressor
from MLPipeline.RandomWalk import RandomWalk
from MLPipeline.RollingWindow import RollingWindow
from MLPipeline.Stationarity import Stationarity


def run_pipeline():
    # Importing the Data
    raw_csv_data = pd.read_csv(os.path.join(module_path, 
                                            "input/Data-Chillers.csv"))
    
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


run_pipeline()
