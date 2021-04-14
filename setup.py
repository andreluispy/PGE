import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pge-engine",
    version="1.1.5",
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
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    package_dir={"": "src"},
)
