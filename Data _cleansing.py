import numpy as np
import pandas as pd
dataset = pd.read_csv("netflix.csv") #import data set
print(dataset.head().columns) #check header col
mis_values = dataset.isnull().sum() #check null values
print(mis_values)


