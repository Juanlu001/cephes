import os.path
from setuptools import setup, Extension


cephes_src = ([os.path.join('src', 'cephes', '*.c')] + 
              [os.path.join('src', 'cephes', '*.h')])

cephes_ext = Extension('cephes', sources=cephes_src)

setup(
    name="cephes",
    version="2016.03.11",
    description="CEPHES mathematical library",
    maintainer="Juan Luis Cano Rodríguez",
    maintainer_email="hello@juanlu.space",
    url="https://github.com/poliastro/cephes",
    ext_modules=[cephes_ext],
)