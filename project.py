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
print(max(ann.bbox_dims()))
print(ann.bbox_dims())
print(vol[ann.bbox(pad=35.0)].shape)
print(ann.bbox_dims(pad=35.0))

import numpy as np
print("%.2f mm^3, %.2fmm^3" % (ann.volume, np.prod(ann.bbox_dims())))
print(ann.bbox_matrix())

mask = ann.boolean_mask()
bbox = ann.bbox()

print(vol[bbox][mask].mean())
print(vol[bbox][~mask].mean())

import matplotlib.pyplot as plt
i,j,k = ann.centroid
# plt.imshow(vol[:,:,int(k)], cmap=plt.cm.gray)
# plt.plot(j, i, '.r', label="Nodule centroid")
# plt.legend()
# plt.show()
print(i,j,k)

zvals = ann.contour_slice_zvals
kvals = ann.contour_slice_indices
scan_zvals = ann.scan.slice_zvals

for k, z in zip(kvals, zvals):
    print(k, z, scan_zvals[k])

print(ann.contours_matrix)
print(len(ann.contours_matrix))

print(ann.feature_vals(True))
ann.print_formatted_feature_table()

# n = 100
# vol,mask = ann.uniform_cubic_resample(n)
#
# # Setup the plot.
# img = plt.imshow(np.zeros((n+1, n+1)),
#                  vmin=vol.min(), vmax=vol.max(),
#                  cmap=plt.cm.gray)
#
#
# # View all the resampled image volume slices.
# for i in range(n+1):
#     img.set_data(vol[:,:,i] * (mask[:,:,i]*0.6+0.2))
#
#     plt.title("%02d / %02d" % (i+1, n))
#     plt.pause(0.1)

# ann.visualize_in_3d(edgecolor='green', cmap='autumn')

# ann.visualize_in_scan()

con = ann.contours[4]
print(con)
# print(con.inclusion)
print(con.image_z_position)
print(con.image_k_position)
print(con.to_matrix())
# print(con.dicom_file_name)
# print(con.coords)
# k = con.image_k_position
# ii, jj = ann.contours[4].to_matrix(include_k=False).T
#
# plt.imshow(vol[:,:,46], cmap=plt.cm.gray)
# plt.plot(jj, ii, '-r', lw=1, label="Nodule Boundary")
# plt.legend()
# plt.show()

padding = 70.0

mask = ann.boolean_mask(pad = padding)
bbox = ann.bbox(pad = padding)
from pylidc.utils import volume_viewer
volume_viewer(vol[bbox], mask, ls='-', lw=2, c='r')