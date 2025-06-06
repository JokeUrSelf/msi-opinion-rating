import importlib
import pkgutil
from flask import Flask
from utils.routing import get_all_blueprints

def register_blueprints(app: Flask):
    for _, mod_name, _ in pkgutil.iter_modules(__path__):
        importlib.import_module(f"{__name__}.{mod_name}")
    for bp in get_all_blueprints():
        app.register_blueprint(bp)
