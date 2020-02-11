from setuptools import setup, find_packages

setup(
    name='team11package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA2020 team 11 predict',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='Monica Farrell',
    author_email='monicafar147@gmail.com'
)