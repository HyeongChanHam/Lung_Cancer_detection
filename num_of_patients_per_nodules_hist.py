import pandas as pd
import matplotlib.pyplot as plt
import os
pre = os.path.dirname(os.path.realpath(__file__))
file = 'lidc_idri_nodule_counts.xlsx'
path = os.path.join(pre, file)
df_raw = pd.read_excel(path)
df = df_raw[['TCIA Patent ID', 'Number of Nodules >=3mm**']].dropna()
df[['Number of Nodules >=3mm**']].hist(cumulative=True, histtype='step', density=1, bins=1000)
plt.title("number of nodules cumulative histogram")
plt.grid(False)

plt.show()