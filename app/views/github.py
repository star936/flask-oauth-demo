# coding: utf-8

from flask import Blueprint, current_app, jsonify, request

import requests
# from app.utils.http import OauthRequest

github = Blueprint('github', __name__)


@github.route("/oauth/redirect", methods=['GET'])
def oauth():
    code = request.args.get("code")
    access_token_headers = {'accept': 'application/json'}
    config = current_app.config
    url = config['GITHUB_ACCESS_TOKEN_URL'] + '?client_id=' + config['GITHUB_CLIENT_ID'] + '&client_secret=' \
        + config['GITHUB_CLIENT_SECRECT'] + '&code=' + code
    data = requests.post(url, headers=access_token_headers).json()

    access_token = data['access_token']
    user_headers = {
      'accept': 'application/json',
      'Authorization': 'token ' + access_token
    }
    user_data = requests.get(config['GITHUB_USER_INFO_URL'], headers=user_headers).json()
    return jsonify({'name': user_data['login']})
