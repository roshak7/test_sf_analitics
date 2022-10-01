import pandas as pd
import numpy as np

football = pd.read_csv('pandas/players.csv')
a = football[(football.Age < football.Age.mean())&
        (football.Club == 'FC Barcelona')].Wage.mean()
print(football.Penalties.count())