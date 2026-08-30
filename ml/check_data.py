import pandas as pd

file_path = "ml/data/cleaned_agmarknet.csv"

df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())