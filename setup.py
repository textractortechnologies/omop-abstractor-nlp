from setuptools import setup, find_packages

ABOUT = {}
with open("textabstractor/about.py", "r") as about_file:
    exec(about_file.read(), ABOUT)

setup(
    name=ABOUT["__project_name__"],
    version=ABOUT["__version__"],
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
        "pluggy",
        "fastapi",
        "uvicorn",
        "requests",
        "pydantic",
    ],
    extras_require={
        "interactive": ["jupyterlab", "rise"],
        "dev": ["black", "pyment", "twine", "tox", "bumpversion", "flake8", "coverage", "sphinx"],
        "test": ["pytest", "pyhamcrest", "icecream", "starlette", "pyyaml"]
    },
)
