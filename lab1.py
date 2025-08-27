import pandas as pd

class StandardNorm:
    def scale(self, df):
        for i in df.columns:
            mean = df[i].mean()
            sd = df[i].std()
            df[i] = (df[i] - mean) / sd
        return df


df = pd.DataFrame(
    [[45000, 42], [32000, 26], [58000, 48], [37000, 32]], columns=["Salary", "Age"]
)
print("Original Data")
print(df)

s = StandardNorm()
df_scaled = s.scale(df)

print("\nNormalized Data")
print(df_scaled)