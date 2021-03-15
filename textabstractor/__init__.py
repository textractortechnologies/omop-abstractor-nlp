from textabstractor.about import __project_name__, __version__  # noqa F401

import pluggy

hookimpl = pluggy.HookimplMarker(__project_name__)

from textabstractor import app  # noqa: E402, F401
from textabstractor import nlp  # noqa: E402, F401
