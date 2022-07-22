from setuptools import setup, find_packages


setup(
    name="sample_python_binary",
    version="0.1",
    description="A sample python binary implementation using pyinstaller",
    author="Ian Panganiban",
    author_email="lkp@noypimaps.com",
    packages=find_packages(),
    entry_points={"console_scripts": ["pipeline=sample_python_binary.run:main"]},
    install_requires=[
        "fire",
        "pyinstaller",
        "numpy",
    ],
)
