import pandas as pd
import numpy as np

def column_detector(df):
    column_types = {}
    for col in df.columns:
        dtype = df[col].dtype
        unique_count = df[col].nunique()
        
        if dtype in ['float64', 'int64']:
            column_types[col] = 'numerical'
        elif dtype == 'object':
            if unique_count <= 5:
                column_types[col] = 'categorical'
            else:
                column_types[col] = 'text'
        else:
            column_types[col] = 'other'
    
    return column_types


if __name__ == "__main__":
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': ['apple', 'banana', 'apple', 'orange', 'banana'],
        'C': [0.1, 0.2, 0.3, 0.4, 0.5]
    })

    print(column_detector(df))
