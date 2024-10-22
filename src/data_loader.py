import pandas as pd

class DataLoader:
    @staticmethod
    def load_csv(file_path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise FileNotFoundError(f"Error loading {file_path}: {str(e)}")
