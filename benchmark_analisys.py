import pandas as pd

filename = "Phenom.CSV"

df = pd.read_csv(
    filename,
    encoding="ISO-8859-1",
    header=0,
    parse_dates=[["Date", "Time"]],
    dtype=object,
    index_col=0,
)
df.dropna(how="all", axis="columns", inplace=True)
df.drop(df.tail(2).index, inplace=True)
df