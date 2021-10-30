import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SELCON", # Replace with your own username
    version="1.0.0",
    author = "dummy",
    author_email = "dummy",
    description = "A Subset Selection Method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sanidhyaanand/SELCON",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib'
    ]
)