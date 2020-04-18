import pylidc as pl

pid = 'LIDC-IDRI-0007'

scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == pid).first()
print(scan)

#patiend_id
print(scan.patient_id)

#informations

#slice thickness
# print(scan.slice_thickness)
#slice_spacing
# print(scan.slice_spacing)

#slice_zvals : z values increasing order
# print(scan.slice_zvals)



#annotation
# print(scan.annotations)

#annotations clustering per nodules
anns = scan.cluster_annotations()
# print(anns)
for i,nod in enumerate(anns):
    print(i, nod)

# print(scan.get_path_to_dicom_files())

import matplotlib.pyplot as plt

#call image all info
# images = scan.load_all_dicom_images()

#indicate z values(minus value)
# zs = [float(img.ImagePositionPatient[2]) for img in images]
#represent thickness, which is equal to slice_thickness
# print(zs[1] - zs[0], scan.slice_thickness)

#to plot image, use pixel_array(512,512), and 1 channel
# plt.imshow(images[0].pixel_array, cmap=plt.cm.gray )
# plt.show()

#scan 3D numpy array
print(scan.to_volume().shape)

#visualize one slice with scan info
#includes Slice thickness and Pixel spacing
# scan.visualize()


#also possible to represent with annotation info
#includes # nodules, near slice position
scan.visualize(annotation_groups=anns)