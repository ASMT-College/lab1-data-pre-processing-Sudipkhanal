import numpy as np
import pandas as pd


class MinMaxNorm:
    def scale(self, df):
        for c in df.columns:
            min = df[c].min()
            max = df[c].max()
            df[c] = (df[c] - min) / (max - min)
        return df


df = pd.DataFrame(
    [[45000, 42], [32000, 26], [58000, 48], [37000, 32]], columns=["Salary", "Age"]
)
print("Original Data")
print(df)

s = MinMaxNorm()
df_scaled = s.scale(df)

print("\nNormalized Data")
print(df_scaled)