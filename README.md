# NLP Library and Service for OMOP Abstractor

## Installation:
```bash
conda env crate -f environment.yml
conda activate textractor-env
python -m spacy download en_core_web_sm
```
## Usage:
```bash
 uvicorn abstractor.service.main:app --reload
```
