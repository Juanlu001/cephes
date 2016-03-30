import os.path
from glob import glob

import setuptools
from numpy.distutils.core import setup, Extension

cephes_src = glob(os.path.join("src", "*.c"))
cephes_ext = Extension('cephes', sources=cephes_src)

setup(
    name="cephes",
    version="2016.03.30",
    description="CEPHES mathematical library",
    maintainer="Juan Luis Cano Rodríguez",
    maintainer_email="hello@juanlu.space",
    url="https://github.com/poliastro/cephes",
    ext_modules=[cephes_ext],
)
