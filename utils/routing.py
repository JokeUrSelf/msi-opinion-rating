import inspect
from flask import Blueprint

_blueprint_registry = {}

def route(rule, **options):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    if not module: 
        raise "route decorator wasn't called from a module"
    mod_name = module.__name__.split('.')[-1]

    if mod_name not in _blueprint_registry:
        _blueprint_registry[mod_name] = Blueprint(mod_name, module.__name__)

    def decorator(f):
        _blueprint_registry[mod_name].route(rule, **options)(f)
        return f
    return decorator

def get_all_blueprints():
    return _blueprint_registry.values()
