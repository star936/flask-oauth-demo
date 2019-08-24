# coding: utf-8

from flask import current_app
import logging as log
import requests
from requests.exceptions import ConnectionError, RequestException
from urllib.parse import urlencode, urljoin


class Oauth(object):
    def __init__(self, name):
        self.name = name.upper()
        self.config = current_app.config
        self.client_id = self.config['{}_CLIENT_ID'.format(self.name)]
        self.client_secret = self.config['{}_CLIENT_SECRECT'.format(self.name)]
        self.redirect_uri = urljoin(self.config['BASE_URL'], '/{}/oauth/redirect'.format(self.name.lower()))
        self.access_token = None

    def _get(self, url, params=None, **kwargs):
        try:
            response = requests.get(url, params, **kwargs)
            return response.json()
        except ConnectionError as ce:
            log.error('{} connection error: {}'.format(self.name, ce))
            return None
        except RequestException as re:
            log.error('{} request error: {}'.format(self.name, re))
            return None

    def _post(self, url, data=None, **kwargs):
        try:
            response = requests.post(url, data=data, **kwargs)
            return response.json()
        except ConnectionError as ce:
            log.error('{} connection error: {}'.format(self.name, ce))
            return None
        except RequestException as re:
            log.error('{} request error: {}'.format(self.name, re))
            return None

    def get_auth_url(self):
        """获取授权确认URL"""
        pass

    def get_access_token(self, code):
        """获取access token"""
        pass

    def get_user_info(self):
        """获取用户信息"""
        pass

    def exist_token(self, result):
        if result is None or 'access_token' not in result:
            log.error('{} access token is invalid, error: {}'.format(self.name, result))
            self.access_token = None
        else:
            self.access_token = result['access_token']


class GitHubOauth(Oauth):

    def get_auth_url(self):
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri
        }
        url = self.config['GITHUB_AUTHORIZE_URL'] + '?%s' % urlencode(params)
        return url

    def get_access_token(self, code):
        access_token_headers = {'accept': 'application/json'}
        url = self.config['GITHUB_ACCESS_TOKEN_URL'] + '?client_id=' + self.client_id + '&client_secret=' \
            + self.client_secret + '&code=' + code
        res = self._post(url, headers=access_token_headers)
        print(res)
        return self.exist_token(res)

    def get_user_info(self):
        if self.access_token is None:
            return {'error': 'Use GitHub login failed!'}
        user_headers = {
            'accept': 'application/json',
            'Authorization': 'token ' + self.access_token
        }
        res = self._get(self.config['GITHUB_USER_INFO_URL'], headers=user_headers)
        return {'name': res['login']}


class BaiduOauth(Oauth):

    def get_auth_url(self):
        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': 'basic',
            'display': 'popup'
        }
        url = self.config['BAIDU_AUTHORIZE_URL'] + '?%s' % urlencode(params)
        return url

    def get_access_token(self, code):
        url = self.config['BAIDU_ACCESS_TOKEN_URL'] + '?grant_type=authorization_code' + '&code=' + code + '&client_id=' \
              + self.client_id + '&client_secret=' + self.client_secret + '&redirect_uri=' + self.redirect_uri
        res = self._post(url)
        return self.exist_token(res)

    def get_user_info(self):
        if self.access_token is None:
            return {'error': 'Use Baidu login failed'}
        url = self.config['BAIDU_USER_INFO_URL'] + '?access_token={}'.format(self.access_token)
        res = self._post(url)
        return {'name': res['uname']}

