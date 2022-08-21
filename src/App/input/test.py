import pandas as pd

df = pd.read_csv("src/assets/input.csv", header = None)
df.columns = ["Domains"]

domains = []

def get_chunk(dataframe: pd.DataFrame, chunk_size: int, start_row: int = 0) -> pd.DataFrame:
    end_row  = min(start_row + chunk_size, dataframe.shape[0])

    return dataframe.iloc[start_row:end_row, :]

def get_end(dataframe: pd.DataFrame, chunk_size: int, start_row: int = 0) -> pd.DataFrame:
    end_row  = min(start_row + chunk_size, dataframe.shape[0])

    return end_row

# print(get_chunk(df, 200, 0))
# a = []
# start = 0
# for i in df["Domains"]:
#     if len(domains) < 200:
#         get_chunk(df, 200)
#     else:
#         get_chunk(df, 200, )

# print(a)

# print(df.loc[:, "pinarealestateacademy.com"])
df.drop(index=df.index[:200], axis=0, inplace=True)
print(df)
