# coding: utf-8

from flask import Flask, current_app

from app.settings import config, BASE_DIR
from app.views import config_blueprint


def create_app(config_name):
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(config.get(config_name) or 'default')

    # 配置blueprint
    config_blueprint(app)

    return app


app = create_app('default')

