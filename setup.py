from setuptools import setup, find_packages

setup(
    name='ocr review',
    version='0.1.1',
    author='Will Thompson',
    author_email='wkt@northwestern.edu',
    maintainer='Will Thompson',
    maintainer_email='wkt@northwestern.edu',
    description='NLP Library for OMOP Abstractor',
    url='https://github.com/textractortechnologies/omop-abstractor-nlp',
    packages=find_packages(include=['review', 'review.*']),
    # package_data={'review': ['data/*.j2']},
    include_package_data=True,
    install_requires=[
        'fastapi',
        'spacy',
        'pysbd',
        'pyaml',
      ],
    extras_require={
        'interactive': ['jupyter', 'jupyter-server', 'jupyterlab']
    },
    # entry_points={
    #     'console_scripts': ['load_moodys_tables=abstractor.<module>:main']
    # },
    setup_requires=['pytest-runner', 'flake8', 'python-dotenv', 'black'],
    tests_require=['pytest', 'pytest-console-scripts'],
)

