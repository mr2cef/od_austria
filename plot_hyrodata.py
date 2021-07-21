##

import requests
import pandas as pd
import plotly.express as px
from io import StringIO
##
a = requests.get("https://wiski.tirol.gv.at/hydro/ogd/OGD_W.csv")
df = pd.read_csv(StringIO(a.text), sep=";")
df["Zeitstempel in ISO8601"] = pd.to_datetime(df["Zeitstempel in ISO8601"])
df2 = df[df["Stationsname"]\
         .isin([
    "Almdorf",
    "St Johann in Tirol",
    "Kössen Staffenbrücke",
    "Kitzbühel (Bahnhofsbrücke)",
    "Innsbruck"
])]

##
px.line(df2, x="Zeitstempel in ISO8601", y="Wert", color="Stationsname").show()
b = requests.get("https://wiski.tirol.gv.at/hydro/ogd/OGD_N.csv")
df = pd.read_csv(StringIO(b.text), sep=";")
df["Zeitstempel in ISO8601"] = pd.to_datetime(df["Zeitstempel in ISO8601"])
df2 = df[df["Stationsname"]\
         .isin([
    "St Johann in Tirol-Almdorf",
    "Schwaz",
    "St Martin in Gnadenwald",
    "Inzing"
])]
px.line(df2, x="Zeitstempel in ISO8601", y="Wert", color="Stationsname").show()



##

