import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pge-engine",
    version="1.0.1",
    scripts=['pge.py'] ,
    author="André Luís",
    author_email="andreluisportelaneves@gmail.com",
    description="A Python Game Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andreluispy/pge",
    project_urls={
        "Bug Tracker":"https://github.com/andreluispy/pge/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
