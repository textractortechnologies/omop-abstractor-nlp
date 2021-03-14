from abstractor import app
from abstractor import nlp
import pluggy

PROJECT_NAME = "omop_abstractor_nlp"

hookimpl = pluggy.HookimplMarker(PROJECT_NAME)
