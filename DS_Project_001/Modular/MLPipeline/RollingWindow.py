
def check_windows(self):

    rolling_window(self)
    expanding_window(self)


def expanding_window(self):

    self.data['rolling_mean_IOT_Reading'] = self.data['IOT_Reading'].expanding(min_periods=1).mean()
    print(self.data.rolling_mean_IOT_Reading)
    self.data['rolling_mean_IOT_Reading'] = self.data['IOT_Reading'].expanding(min_periods=1).std()
    print(self.data.rolling_mean_IOT_Reading)


def rolling_window(self):

    self.data['rolling_mean_IOT_Reading'] = self.data['IOT_Reading'].rolling(window=24).mean()
    print(self.data.tail())
    self.data['rolling_mean_IOT_Reading'] = self.data['IOT_Reading'].rolling(window=24).std()
    print(self.data.tail())
