import pandas as pd 

df = pd.read_excel('экономика/для презентации - июль 2022.xlsx')

small_df = df.info()

print(small_df)
