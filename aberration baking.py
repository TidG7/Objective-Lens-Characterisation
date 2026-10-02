from pyotf.zernike import degrees2name

import numpy as np

for n in degrees2name.values():
    print(n)

n = 10  # number of slices

zres = 100000 / 150 * 2  # z step (all lengths in nm)

params = dict(

    size=100,

    zsize=n,

    na=0.3,

    res=114,

    zres=zres,

    wl=399,

    ni=1.0,

    vec_corr="none",

    condition="none",

)

from pyotf.otf import HanserPSF, apply_named_aberrations

from matplotlib import pyplot as plt

psf = HanserPSF(**params)

psf = apply_named_aberrations(psf, {'primary spherical': -.8, 'oblique secondary astigmatism': -0.0,
                                    'vertical secondary coma': -.0})

for s in range(n):
    plt.imshow(psf.PSFi[s, :, :], vmin=0, vmax=np.max(psf.PSFi))

    plt.title("z = %.1fum" % ((s - (n) / 2) * zres / 1000))

    plt.show()