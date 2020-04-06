import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manim
from skimage.measure import find_contours

import pylidc as pl
from pylidc.utils import consensus

scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == 'LIDC-IDRI-0003').first()
vol = scan.to_volume()
nods = scan.cluster_annotations()

scan.visualize(annotation_groups=nods)

for i, nod in enumerate(nods):
    print(i, len(nod))
for i in range(len(nods)):
    plt.figure()
    anns = nods[i]

    cmask, cbbox, masks = consensus(anns, clevel = 0.5,
                                    pad = [(20, 20), (20, 20), (0,0)])
    k = int(0.5*(cbbox[2].stop - cbbox[2].start))

    fig, ax = plt.subplots(1, 1, figsize=(5,5))
    ax.imshow(vol[cbbox][:,:,k], cmap=plt.cm.gray, alpha=0.5)

    colors = ['r', 'g', 'b', 'y']

    for j in range(len(masks)):
        for c in find_contours(masks[j][:,:,k].astype(float), 0.5):
            label = "Annotation %d" % (j+1)
            plt.plot(c[:,1], c[:,0], colors[j], label = label)

    for c in find_contours(cmask[:,:,k].astype(float), 0.5):
        plt.plot(c[:, 1], c[:, 0], '--k', label='50% Concensus')

    ax.axis('off')
    ax.legend()
    plt.tight_layout()
    plt.show()

