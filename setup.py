from setuptools import setup, find_packages

setup(
    name="pine2py",
    version="0.1.0",
    description="Translate TradingView Pine Script (v5/v6) to executable Python (pandas/TA-Lib)",
    author="pine2py contributors",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24",
        "pandas>=2.0",
        "matplotlib>=3.7",
        "ta-lib>=0.4.28",
        "parso>=0.11",
        "python-dateutil>=2.8",
    ],
    python_requires=">=3.9",
    include_package_data=True,
)



