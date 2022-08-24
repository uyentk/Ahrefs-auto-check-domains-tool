import pandas as pd

# Lists of exported files
export_res = ['src/DataAnalysis/data/batch_analysis_export.utf-16.csv', "src/DataAnalysis/data/batch_analysis_export.utf-16 (1).csv"]

# Read all of the files
df = pd.DataFrame()
for i in export_res:
    with open(i, encoding='utf-16-le') as f:
        res = pd.read_table(f).set_index("#")
        df = df.append(res, ignore_index=True)

# Read file DA Check
da_check_df = pd.read_csv("src/DataAnalysis/data/output.csv")
da_check_df.columns = ["Target", "DA"]
# print(da_check_df)

# Merge DA Check file to the main dataframe
df = df.merge(da_check_df, how='inner', on= "Target")

# Analyse and filter the data
df["Backlink Dofollow"] = df["Total Backlinks"] - df["Backlinks NoFollow"]
df = df.loc[:, ["Target","Domain Rating", "Ref domains Dofollow", "Backlink Dofollow", "DA"]]
df["Check"] = ""
df.loc[(df["Domain Rating"] <= 10) | (df["Ref domains Dofollow"] <= 100) | (df["DA"] <= 30), 'Check'] = "x"
print(df)
