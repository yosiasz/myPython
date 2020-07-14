import pandas as pd
from IPython.display import display
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
A = pd.read_excel("./data.xlsx", sheet_name=0)

df = A[ (A.Tmax > 0) & (A.Tmin > 0)]

#Average
df['avg'] = df.iloc[:,1:3].mean(axis=1)


#Subtraction
df['minus'] = df['Tmax'] - df['Tmin']

#Addition
df['Sum'] = df['Tmax'] + df['Tmin']
print(df)
