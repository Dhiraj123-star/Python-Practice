import polars as pl

df = pl.DataFrame({
    "Python":["interpreted","Simple"],
    "Java":["Compiled","Popular"],
    "C":["Compiled","Fast"]
})

selected_col = df.select(['Python'])

print(selected_col)
