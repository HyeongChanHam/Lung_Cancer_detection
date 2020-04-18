import pylidc as pl
import matplotlib.pyplot as plt
pid = 'LIDC-IDRI-0011'

scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == pid).first()
anns = scan.cluster_annotations()

print(scan.slice_zvals)
print(len(scan.slice_zvals))
z_list = {}
# for ann in anns:
#     for z in ann[0].contour_slice_zvals:
#         if z in z_list.keys():
#             z_list[z] += 1
#         else:
#             z_list[z] = 1
# print(z_list)


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
    for anns in nodules:
        for z in anns[0].contour_slice_zvals:
            z //=1
            if z>0:
                continue
            if z in z_list.keys():
                z_list[z] += 1
            else:
                z_list[z] = 1
            if z > 1000:
                print(pid)

print(z_list)
plt.bar(z_list.keys(), z_list.values())
plt.title('number of nodules for z-value')
plt.xlabel('z-value')
plt.ylabel('count')
plt.show()