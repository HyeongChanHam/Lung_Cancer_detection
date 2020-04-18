import pylidc as pl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pid = 'LIDC-IDRI-0007'

scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == pid).first()
vol = scan.to_volume()

zero_matrix = np.zeros((512,512))

for i in range(1,101):
    if i<10:
        s = '000'+str(i)
    elif i<100:
        s = '00'+str(i)
    else:
        s = '0'+str(i)
    pid = 'LIDC-IDRI-{}'.format(s)
    scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == pid).first()
    nodules = scan.cluster_annotations()
    for nodule in nodules:
        ann = nodule[0]
        x, y, _ = ann.bbox()
        m = ann.boolean_mask()
        for i in range(m.shape[2]):
            zero_matrix[(x, y)] += m[:, :, i]

    print(pid)
sns.heatmap(zero_matrix)
plt.title('heatmap of occurance per slice')
plt.axis('off')
plt.show()