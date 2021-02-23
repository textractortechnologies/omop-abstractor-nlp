import pluggy

import abstractor
from abstractor.nlp import hookspecs, lib


def get_plugin_manager():
    pm = pluggy.PluginManager(abstractor.PROJECT_NAME)
    pm.add_hookspecs(hookspecs)
    pm.load_setuptools_entrypoints(abstractor.PROJECT_NAME)
    pm.register(lib)
    return pm
