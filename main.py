import pandas as pd
from sklearn.linear_model import LinearRegression

# Quick test data
data = {'X': [1, 2, 3, 4], 'Y': [2, 4, 6, 8]}
df = pd.DataFrame(data)

print("Environment is ready!")
print(df.head())
