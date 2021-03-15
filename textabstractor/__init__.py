from textabstractor.about import __project_name__, __version__

import pluggy

hookimpl = pluggy.HookimplMarker(__project_name__)

from textabstractor import app
from textabstractor import nlp
