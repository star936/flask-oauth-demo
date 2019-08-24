# coding: utf-8

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    BASE_URL = "http://localhost:5000"
    # GitHub设置
    GITHUB_AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
    GITHUB_CLIENT_ID = "97e6fce8aa0571095fc3"
    GITHUB_CLIENT_SECRECT = "2107fe7b7403d79e2e75f447779c73f8933502a7"
    GITHUB_ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"
    GITHUB_USER_INFO_URL = 'https://api.github.com/user'

    # baidu设置
    BAIDU_AUTHORIZE_URL = "http://openapi.baidu.com/oauth/2.0/authorize"
    BAIDU_CLIENT_ID = "uYIyg2UmFtVy0TDQdSPQRTHr"
    BAIDU_CLIENT_SECRECT = "vd8RhI4Ec4dU8tZjFHOjlMVV1bZZKrvG"
    BAIDU_ACCESS_TOKEN_URL = "https://openapi.baidu.com/oauth/2.0/token"
    BAIDU_USER_INFO_URL = "https://openapi.baidu.com/rest/2.0/passport/users/getLoggedInUser"


config = {
    "default": Config
}
