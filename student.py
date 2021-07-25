import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
    marks=[]
    days_present=[]
    with open (data_path)as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return {"x":marks,"y":days_present}

def findCorrelation(datasourcs):
    Correlation=np.corrcoef(datasourcs["x"],datasourcs["y"])
    print ("Correlation",Correlation[0,1])

def setup():
    data_path="student.csv"
    datasourcs=getDataSource(data_path)
    findCorrelation(datasourcs)

setup()