from tabnanny import check
from App.Automation import check_domain
from DataAnalysis.data_analyse import df
import pandas 

def auto_process():
    check_domain()
    df.to_csv("src/DataAnalysis/data/result.csv")