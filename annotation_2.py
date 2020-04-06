import pylidc as pl

ann = pl.query(pl.Annotation).first()
print(ann.scan.patient_id)

anns = pl.query(pl.Annotation).filter(pl.Annotation.spiculation==5,
                                      pl.Annotation.malignancy==5)
# print(anns)

ann = pl.query(pl.Annotation)\
    .filter(pl.Annotation.malignancy==4).first()
print(ann.malignancy, ann.Malignancy)
print(ann.margin, ann.Margin)

ann.print_formatted_feature_table()
