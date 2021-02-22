from setuptools import setup, find_packages

setup(
    name="omop-abstractor-nlp",
    version="0.1.0",
    author="Will Thompson",
    author_email="wkt@northwestern.edu",
    maintainer="Will Thompson",
    maintainer_email="wkt@northwestern.edu",
    description="NLP interface code for the OMOP Abstractor",
    packages=find_packages(include=["abstractor", "abstractor.*"]),
    include_package_data=True,
    install_requires=[
        "requests",
        "celery",
        "rabbitmq",
        "icecream",
        "pandas",
        "regex",
        "pluggy",
        "pyyaml",
        "fastapi",
        "uvicorn",
        "spacy>=3"
    ],
    extras_require={"interactive": ["jupyterlab", "rise"]},
    setup_requires=["black"],
    tests_require=["pytest"],
)
