import pylidc as pl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

pid = 'LIDC-IDRI-0002'
scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == pid).first()

images = scan.load_all_dicom_images()
print(len(images))
# zs = [float(img.ImagePositionPatient[2]) for img in images]
# print(zs[1] - zs[0],  scan.slice_thickness)
for i in range(19):
    plt.figure()
    plt.imshow(images[i].pixel_array, cmap=plt.cm.gray)
plt.show()