from setuptools import setup, find_packages

setup(
    name="omop_abstractor_nlp",
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
        "icecream",
        "pluggy",
        "pyyaml",
        "fastapi",
        "uvicorn",
        # "celery",
        # "rabbitmq",
    ],
    extras_require={"interactive": ["jupyterlab", "rise"]},
    setup_requires=["black"],
    tests_require=["pytest", "pyhamcrest"],
)
