import pylidc as pl
from pandas import DataFrame as df
import matplotlib.pyplot as plt

diameter = []
surface_area = []
volume = []
Sphericity = []
for i in range(1,30):
    if i<10:
        s = '000'+str(i)
    elif i<100:
        s = '00'+str(i)
    else:
        s = '0'+str(i)
    pid = 'LIDC-IDRI-{}'.format(s)
    scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == pid).first()
    nodules = scan.cluster_annotations()
    if not nodules:
        continue
    for nodule in nodules:
        diameter.append(nodule[0].diameter)
        surface_area.append(nodule[0].surface_area)
        volume.append(nodule[0].volume)
        Sphericity.append(nodule[0].Sphericity)

data_dic = {}
data_dic['diameter'] = diameter
data_dic['surface_area'] = surface_area
data_dic['volume'] = volume
data_dic['Sphericity'] = Sphericity
df1 = df(data_dic)
print(df1)
print(df1['diameter'].mean())
print(df1['diameter'].std())
print(df1['diameter'].median())
print(df1['diameter'].max())
print(df1['diameter'].min())

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)



ax1.boxplot(df1['diameter'])
ax1.set_title('Box plot of diameter')
ax1.set_ylabel('mm')

ax2.boxplot(df1['surface_area'])
ax2.set_title('Box plot of surface_area')
ax2.set_ylabel('mm^2')

ax3.boxplot(df1['volume'])
ax3.set_title('Box plot of volume')
ax3.set_ylabel('mm^3')

ax4.hist(df1['Sphericity'], align='mid')
ax4.set_title('Nodule Sphericity')
ax4.set_ylabel('number')
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()
