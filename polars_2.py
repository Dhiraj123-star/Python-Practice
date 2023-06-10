import polars as pl

df = pl.read_csv("cars.csv")

colors = df.select('color') # select the color column color

print(colors)