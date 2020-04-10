import pylidc as pl

pid = 'LIDC-IDRI-0001'
scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == pid).first()

ann = scan.annotations[0]
vol = ann.scan.to_volume()
print(ann.scan.patient_id)
print(ann.bbox())
print(vol.shape)
print(vol[ann.bbox()].shape)
print(vol[ann.bbox(pad=2)].shape)
print(vol[ann.bbox(pad=[(1,2), (3,0), (2,4)])].shape)
