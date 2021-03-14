PROJECT_NAME = "omop_abstractor_nlp"
import pluggy
hookimpl = pluggy.HookimplMarker(PROJECT_NAME)

from abstractor import app
from abstractor import nlp
