from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np


def impute_data(df: pd.DataFrame) -> pd.DataFrame:
    # Create a SimpleImputer Class
    imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')

    # Fit the columns to the object
    columns = ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g']
    imputer=imputer.fit(df[columns])

    # Transform the DataFrames column with the fitted data
    df[columns]=imputer.transform(df[columns])


    return df

def drop_missing_records(df: pd.DataFrame) -> pd.DataFrame:
    # Dropping missing records in the sex column
    df = df.dropna(subset=['sex'])
    return df

def funcao_nao_usada(valor: int) -> float:
    return valor/100
