# coding: utf-8

from flask import Blueprint, current_app, jsonify, request

from app.utils.oauth import GitHubOauth

github = Blueprint('github', __name__)


@github.route("/oauth/redirect", methods=['GET'])
def oauth():
    code = request.args.get("code")
    gho = GitHubOauth()
    gho.get_access_token(code)
    user_data = gho.get_user_info()
    return jsonify(user_data)
