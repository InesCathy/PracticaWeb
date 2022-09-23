import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('data/rostro.xlsx')
fig, ax = plt.subplots()

ax.imshow(df)
plt.show()