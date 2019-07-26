import io
import os
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding='utf-8').read()


setup(
    name='omop-abstractor-nlp',
    version='0.1.0',
    author='Will Thompson',
    author_email='wkt@northwestern.edu',
    maintainer='Will Thompson',
    maintainer_email='wkt@northwestern.edu',
    description='NLP service',
    url='https://github.com/textractortechnologies/omop-abstractor-nlp',
    zip_safe=False,
    packages=['abstractor'],
    include_package_data=True,
    install_requires=[
      ],
    entry_points={
        'console_scripts': []
    }
)