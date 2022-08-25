from tabnanny import check
from App.Automation import check_domain
from DataAnalysis.data_analyse import data_process
from DataAnalysis.checkDA import check_DA
import pandas 

def auto_process():
    check_domain()
    check_DA()
    data_process()

auto_process()
