import csv
import plotly.express as px
import pandas as pd

df=pd.read_csv("coffey.csv")

fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
fig.show()