# coding: utf-8

from flask import Blueprint, current_app, render_template, url_for

main = Blueprint('main', __name__)


@main.route("/", methods=['GET'])
def index():
    config = current_app.config
    data = {'github_url': config['GITHUB_AUTHORIZE_URL'] + '?client_id=' + config['GITHUB_CLIENT_ID']
                          + '&redirect_uri=' + 'http://localhost:5000' + url_for('github.oauth')}
    return render_template("index.html", **data)
