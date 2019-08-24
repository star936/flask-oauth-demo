# coding: utf-8

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    BASE_URL = "http://localhost:5000"

    GITHUB_AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
    GITHUB_CLIENT_ID = "97e6fce8aa0571095fc3"
    GITHUB_CLIENT_SECRECT = "2107fe7b7403d79e2e75f447779c73f8933502a7"
    GITHUB_ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"
    GITHUB_USER_INFO_URL = 'https://api.github.com/user'


config = {
    "default": Config
}
