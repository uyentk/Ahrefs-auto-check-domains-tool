import pandas as pd

def data_process():
    # Lists of exported files
    input = pd.read_csv("src/assets/input.csv")
    row_count = len(input.index)
    path = "src/DataAnalysis/data/batch_analysis_export.utf-16 "

    export_res = ["src/DataAnalysis/data/batch_analysis_export.utf-16.csv"]
    if row_count % 200 == 0:
        ls = row_count / 200
    else:
        ls = row_count / 200 + 1

    for i in range(1, int(ls)):
        temp = path + f"({i})" + ".csv"
        export_res.append(temp)

    # Read all of the files
    df = pd.DataFrame()
    for i in export_res:
        with open(i, encoding='utf-16-le') as f:
            res = pd.read_table(f).set_index("#")
            df = df.append(res, ignore_index=True)

    # Read file DA Check
    da_check_df = pd.read_csv("src/DataAnalysis/data/DA_output.csv")
    da_check_df.columns = ["Target", "DA"]
    # print(da_check_df)

    # Merge DA Check file to the main dataframe
    df = df.merge(da_check_df, how='inner', on= "Target")

    # Analyse and filter the data
    df["Backlink Dofollow"] = df["Total Backlinks"] - df["Backlinks NoFollow"]
    df = df.loc[:, ["Target","Domain Rating", "Ref domains Dofollow", "Backlink Dofollow", "DA"]]
    df["Check"] = ""
    df.loc[(df["Domain Rating"] <= 10) | (df["Ref domains Dofollow"] <= 100) | (df["DA"] <= 30), 'Check'] = "x"
    df.to_csv("src/DataAnalysis/data/result.csv")
