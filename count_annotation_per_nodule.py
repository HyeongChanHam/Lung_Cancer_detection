import pylidc as pl
import matplotlib.pyplot as plt
import numpy as np
pid = 'LIDC-IDRI-0007'

anns = pl.query(pl.Annotation).filter(pl.Scan.patient_id == pid)
scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == pid).first()
nodules = scan.cluster_annotations()
for i in nodules:
    print(len(i))
annotation_list = []
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
    for i in nodules:
        annotation_list.append(len(i))
        if len(i)>4:
            print(pid)

label = list(dict.fromkeys(annotation_list))
print(label)
print(annotation_list)
plt.hist(annotation_list,align='mid')
plt.title('number of annotations per nodule')
plt.xticks(label)
plt.xlabel('annotations')
plt.ylabel('count')
plt.show()

