from setuptools import setup, find_packages

with open("./README.rst") as f:
    LONG_DESCRIPTION = f.read()

with open("./VERSION") as f:
    VERSION = f.read().strip()

setup(
    name='snek',
    description='Simple Python Project Management',
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    author='David Daniel',
    author_email='davydany@aeroxis.com',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='http://github.com/aeroxis/snek',
    entry_points={
        'console_scripts': [
            'snek=snek.cli:snek'
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Unix Shell",
        "License :: OSI Approved :: MIT License"]
)
