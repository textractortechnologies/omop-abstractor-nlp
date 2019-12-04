from setuptools import setup, find_packages

setup(
    name='OMOP Abstractor NLP',
    version='0.1.1',
    author='Will Thompson',
    author_email='will.k.t@gmail.com',
    maintainer='Will Thompson',
    maintainer_email='will.k.t@gmail.com',
    description='NLP library for the OMOP Abstractor project.',
    url='https://github.com/textractortechnologies/omop-abstractor-nlp',
    packages=find_packages(include=['abstractor', 'abstractor.*']),
    # package_data={'abstractor': ['data/*.j2']},
    include_package_data=True,
    install_requires=[
        'fastapi',
        'spacy',
        'en_core_web_sm',
        # 'pysbd',
        'pyaml',
        'scikit-learn',
        'pandas',
        'numpy',
        'rdflib',
        'mypy'
      ],
    extras_require={
        'interactive': ['jupyter', 'jupyter-server', 'jupyterlab']
    },
    # entry_points={
    #     'console_scripts': ['scipt_name=abstractor.<module>:main']
    # },
    setup_requires=['pytest-runner', 'flake8', 'python-dotenv', 'black'],
    tests_require=['pytest', 'pytest-console-scripts'],
)

