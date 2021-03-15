from setuptools import setup, find_packages

setup(
    name="textabstractor",
    version="0.1.1",
    author="Will Thompson",
    author_email="wkt@northwestern.edu",
    maintainer="Will Thompson",
    maintainer_email="wkt@northwestern.edu",
    description="NLP web service API code for the OMOP Abstractor",
    packages=find_packages(include=["textabstractor", "textabstractor.*"]),
    package_data={'textabstractor': ['data/*']},
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "pluggy >=0.13.1, < 1",
        "fastapi >=0.63.0, < 1",
        "uvicorn >=0.13.4, < 1",
        "requests >= 2.25.1, <3",
        "pydantic >= 1.8.1, < 2",
    ],
    extras_require={
        "interactive": ["jupyterlab", "rise"],
        "dev": ["black", "pyment", "twine", "tox", "bumpversion"],
        "test": ["pytest", "pyhamcrest", "icecream", "starlette", "pyyaml"]
    },
)
