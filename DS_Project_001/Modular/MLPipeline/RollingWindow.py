


class RollingWindow:

    def __init__(self, df_comp):

        self.df_comp = df_comp 
        # Rolling Window
        self.rollingWindow()

        # Expanding Window 
        self.expandingWindow()

    def expandingWindow(self):

        self.df_comp['rolling_mean_IOT_Reading'] = self.df_comp['IOT_Reading'].expanding(min_periods=1).mean()
        print(self.df_comp.rolling_mean_IOT_Reading)
        self.df_comp['rolling_mean_IOT_Reading'] = self.df_comp['IOT_Reading'].expanding(min_periods=1).std()
        print(self.df_comp.rolling_mean_IOT_Reading)

    def rollingWindow(self):

        self.df_comp['rolling_mean_IOT_Reading'] = self.df_comp['IOT_Reading'].rolling(window=24).mean()
        print(self.df_comp.tail())
        self.df_comp['rolling_mean_IOT_Reading'] = self.df_comp['IOT_Reading'].rolling(window=24).std()
        print(self.df_comp.tail())
