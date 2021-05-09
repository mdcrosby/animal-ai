from setuptools import setup, find_packages

setup(
    name="animalai",
    version="3.0.0",
    description="Animal AI environment Python API",
    url="",
    author="Matthew Crosby",
    author_email="m.crosby@imperial.ac.uk",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe=False,
    install_requires=["mlagents==0.16.1", "jsonpickle", "pyyaml"],
    python_requires=">=3.7",
)
