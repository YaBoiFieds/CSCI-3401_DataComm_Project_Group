import numpy as np
import pandas as pd

# read data from file
data = pd.read_csv('Fiedler_Project_Adjacency-Matrix__With-Zeros.csv')

# create data frame from data
df = pd.DataFrame(data)

# create numpy array from dataframe
nArr = df.to_numpy()