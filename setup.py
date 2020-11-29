import setuptools
from distutils.util import convert_path

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fp:
    install_requires = fp.read()

with open('ignorefile/ignorefile') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[1].replace("'",'')
            break



setuptools.setup(
    name="ignorefile",
    version=version,
    author="Otmane Boughaba",
    author_email="otmaneboughaba@gmail.com",
    license="MIT",
    keywords="gitignore github generate",
    description="Download .gitignore file for a language of your choice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Otman404/ignorefile",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    install_requires=install_requires,
    scripts=['ignorefile/ignorefile']
)
