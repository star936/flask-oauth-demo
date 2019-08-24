# coding: utf-8

from flask import Blueprint, current_app, render_template, url_for

from ..utils.oauth import GitHubOauth

main = Blueprint('main', __name__)


@main.route("/", methods=['GET'])
def index():
    github = GitHubOauth()
    data = {'github_url': github.get_auth_url()}
    return render_template("index.html", **data)
