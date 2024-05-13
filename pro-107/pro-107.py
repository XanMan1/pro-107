import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv("data.csv")
mean = df.groupby(["sport", "distance"], as_index=False).mean()
fig = px.bar(mean, x="sport", y="distance")
fig.show()