import scipy.stats
import pylab
import matplotlib.pyplot as plt
import pandas as pd


def plot_data(self):

        self.data.IOT_Sensor_Reading.plot(figsize=(20,5), title="IOT_Sensor_Reading")
        plt.savefig("Modular/output/"+"IOT_Sensor.png")
        self.data.Error_Present.plot(figsize=(20,5), title="Error_Present")
        plt.savefig("Modular/output/"+"Error_Present.png")
        self.data.Sensor_2.plot(figsize=(20,5), title="Sensor_2")
        plt.savefig("Modular/output/"+"Sensor_2.png")
        self.data.Sensor_Value.plot(figsize=(20,5), title="Sensor_Value")
        plt.savefig("Modular/output/"+"Sensor_Value.png")


def reshape_data(self):
        
        self.data["IOT_Reading"] = self.data.IOT_Sensor_Reading
        self.data.describe()
        del self.data['IOT_Sensor_Reading']
        del self.data['Error_Present']
        del self.data['Sensor_2']
        del self.data['Sensor_Value']


def fill_missing_values(self):

    self.data.IOT_Sensor_Reading = self.data.IOT_Sensor_Reading.ffill()
    self.data.Error_Present = self.data.Error_Present.bfill()
    self.data.Sensor_2 = self.data.Sensor_2.bfill()
    self.data.Sensor_Value = self.data.Sensor_Value.fillna(value=self.data.Sensor_Value.mean())


def set_freq(self):
    self.data = self.data.asfreq('h')


def set_date_index(self):

    # taken as text field
    self.data.time = pd.to_datetime(self.data.time, format='%d-%m-%Y %H:%M')
    self.data.set_index("time", inplace=True)


def plot_QQPlots(self):

    # The QQ plot
    scipy.stats.probplot(self.data.IOT_Sensor_Reading, plot=pylab)
    plt.title("QQ plot for IOT_Sensor_Reading")
    pylab.savefig("Modular/output/"+"QQ_IOT_Sensor.png")

    # The QQ plot
    scipy.stats.probplot(self.data.Error_Present, plot=pylab)
    plt.title("QQ plot for Error_Present")
    pylab.savefig("Modular/output/"+"Error_Present.png")

    # The QQ plot
    scipy.stats.probplot(self.data.Sensor_2, plot=pylab)
    plt.title("QQ plot for Sensor_2")
    pylab.savefig("Modular/output/"+"Sensor_2.png")

    # The QQ plot
    scipy.stats.probplot(self.data.Sensor_Value, plot=pylab)
    plt.title("QQ plot for Sensor_Value")
    pylab.savefig("Modular/output/"+"Sensor_Value.png")
