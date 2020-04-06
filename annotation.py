import pylidc as pl

pid = 'LIDC-IDRI-0003'
scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == pid).first()
print(scan.annotations)

nods = scan.cluster_annotations()
print(len(nods))
for i, nod in enumerate(nods):
    print(i+1, len(nods[i]))

vol = scan.to_volume()
print(vol.shape)

#COMMENT SCAN.PY 542~543, 564~565
scan.visualize(annotation_groups=nods)