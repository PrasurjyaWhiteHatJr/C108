import pandas as pd
import csv
df = pd.read_csv("data.csv")
import plotly.express as px
import plotly.figure_factory as ff
#fig = px.bar(x=df["height"].tolist(), y=df["index"].tolist())
#fig.show()
print(df["height"].tolist())
fig = ff.create_distplot([df["height"].tolist()], ["Height"], show_hist = False)
fig.show()