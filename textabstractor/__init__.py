__version__ = "0.1.1"

PROJECT_NAME = "omop_abstractor_nlp"
import pluggy

hookimpl = pluggy.HookimplMarker(PROJECT_NAME)

from textabstractor import app
from textabstractor import nlp
