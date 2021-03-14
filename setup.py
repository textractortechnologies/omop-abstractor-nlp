from setuptools import setup, find_packages

setup(
    name="omop_abstractor_nlp",
    version="0.1.0",
    author="Will Thompson",
    author_email="wkt@northwestern.edu",
    maintainer="Will Thompson",
    maintainer_email="wkt@northwestern.edu",
    description="NLP web service API code for the OMOP Abstractor",
    packages=find_packages(include=["abstractor", "abstractor.*"]),
    include_package_data=True,
    install_requires=[
        "pluggy",
        "fastapi",
        "uvicorn",
        "requests",
        "pydantic",
        # "celery",
        # "rabbitmq",
    ],
    extras_require={
        "interactive": ["jupyterlab", "rise"],
        "tests": ["pytest", "pyhamcrest", "icecream", "starlette", "pyyaml"],
        "dev": ["black", "pyment"]
    },
)
