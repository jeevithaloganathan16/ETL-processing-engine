import pandas as pd

def extract(path="C:/Users/sandh/PycharmProjects/ETL-processing-engine/data/sales/sales.csv"):
    return pd.read_csv(path)