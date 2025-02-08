import pandas as pd
import os

class Parser :

    @staticmethod
    def read_file(filepath : str) -> pd.DataFrame :
        if os.path.exists(filepath) :
            return pd.read_csv(filepath, delimiter=',')
        return None
