import matplotlib.pyplot as plt
import pandas as pd

class Reporting:
    @staticmethod
    def generate_report(data: pd.DataFrame, title: str):
        fig, ax = plt.subplots(figsize=(10, 6))

        bars = data.plot(kind='bar', title=title, ax=ax)

        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

        for bar in bars.patches:
            ax.text(
                bar.get_x() + bar.get_width() / 2, 
                bar.get_height(), 
                f'{bar.get_height():.2f}', 
                ha='center', 
                va='bottom'
            )

        plt.tight_layout()
        plt.show()
