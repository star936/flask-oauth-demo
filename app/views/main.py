# coding: utf-8

from flask import Blueprint, render_template, url_for

from ..utils.oauth import GitHubOauth, BaiduOauth

main = Blueprint('main', __name__)


@main.route("/", methods=['GET'])
def index():
    github = GitHubOauth('github')
    baidu = BaiduOauth("baidu")
    data = {
        'github_url': github.get_auth_url(),
        'baidu_url': baidu.get_auth_url()
    }
    return render_template("index.html", **data)
