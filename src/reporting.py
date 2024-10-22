import matplotlib.pyplot as plt
import pandas as pd

class Reporting:
    @staticmethod
    def generate_report(data: pd.DataFrame, title: str):
        plt.clf()
        data.plot(kind='bar', title=title)
        plt.show()
