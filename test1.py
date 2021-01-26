import pandas as pd

d = {'a': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
x = 8
df['a'][0] = df.append([[3]])
print(df)
   