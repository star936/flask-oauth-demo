# coding: utf-8

from flask import current_app, url_for
import requests
from urllib.parse import urlencode, urljoin


class Oauth(object):
    def __init__(self):
        self.config = current_app.config

    def _get(self, url, params=None, **kwargs):
        response = requests.get(url, params, **kwargs)
        return response.json()

    def _post(self, url, data=None, **kwargs):
        response = requests.post(url, data=data, **kwargs)
        return response.json()

    def get_auth_url(self):
        """获取授权确认URL"""
        pass

    def get_access_token(self, code):
        """获取access token"""
        pass

    def get_user_info(self):
        """获取用户信息"""
        pass


class GitHubOauth(Oauth):
    def __init__(self):
        super(GitHubOauth, self).__init__()
        self.client_id = self.config['GITHUB_CLIENT_ID']
        self.client_secret = self.config['GITHUB_CLIENT_SECRECT']
        self.redirect_uri = urljoin(self.config['BASE_URL'], '/github/oauth/redirect')
        self.access_token = None

    def get_auth_url(self):
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri
        }
        url = self.config['GITHUB_AUTHORIZE_URL'] + '?%s' % urlencode(params)
        return url

    def get_access_token(self, code):
        access_token_headers = {'accept': 'application/json'}
        url = self.config['GITHUB_ACCESS_TOKEN_URL'] + '?client_id=' + self.client_id + '&client_secret=' \
            + self.client_secret + '&code=' + code
        res = self._post(url, headers=access_token_headers)
        self.access_token = res['access_token']
        return self.access_token

    def get_user_info(self):
        user_headers = {
            'accept': 'application/json',
            'Authorization': 'token ' + self.access_token
        }
        res = self._get(self.config['GITHUB_USER_INFO_URL'], headers=user_headers)
        return {'name': res['login']}
