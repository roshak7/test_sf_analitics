
#УНИКАЛЬНЫЕ ЗНАЧЕНИЯ 
import pandas as pd
df  = pd.read_csv("pandas/players.csv")
small_df = df[df.columns[0:7]].head(25)
print(small_df['Nationality'].unique())#  Уникальное значение списка
print(small_df['Nationality'].nunique())# Уникальное значение число