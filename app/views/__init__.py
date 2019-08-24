# coding: utf-8

from .github import github
from .main import main


DEFAULT_BLUEPRINT = (
    (github, '/github'),
    (main, '')
)


def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
