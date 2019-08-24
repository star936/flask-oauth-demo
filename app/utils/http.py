# coding: utf-8

import requests


class OauthRequest(object):

    @staticmethod
    def post(url, data, **headers):
        res = requests.post(url, data=data, headers=headers)
        return res.json()
