import pandas as pd


class DataCleaner:
    @staticmethod
    def clean_data(df: pd.DataFrame) -> pd.DataFrame:
        df.dropna(inplace=True)
        return df
