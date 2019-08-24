# coding: utf-8

from .baidu import baidu
from .github import github
from .main import main


DEFAULT_BLUEPRINT = (
    (main, ''),
    (github, '/github'),
    (baidu, '/baidu')
)


def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
