from setuptools import setup

setup (
    name='cerub',
    version='1.0',
    description='Conjunto de funciones que gerencian el flujo interno de un procedimiento clinico de tratamientos médicos de infusión intravenosa de medicamentos',
    author='Carlos Scarpini',
    author_email='carlosscarpinibr@gmail.com',
    url='https://github.com/carlosscarpinibr',
    packages=['cerub', 'cerub.archivos', 'cerub.guiestadistica', 'cerub.guilistar', 'cerub.guimenu', 'cerub.guinvisita','cerub.guirevision'],
    scripts=[]
    )