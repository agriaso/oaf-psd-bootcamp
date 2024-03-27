import pandas as pd
import matplotlib.pyplot as plt

class DataHandler():

    def __init__(self, service):
        self.service = service

    def plot_data(self, df):
        """Plots the weather df.
        
        Args:
            df (pd.DataFrame): The weather data to plot.
        """
        df.plot(x = "date", y = ["temperature_2m_max", "temperature_2m_min"], title = "Temperature (°F)", grid = True, figsize = (10, 5))
        plt.show()