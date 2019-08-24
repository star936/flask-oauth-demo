# coding: utf-8

from flask import Blueprint, jsonify, request

from app.utils.oauth import BaiduOauth

baidu = Blueprint('baidu', __name__)


@baidu.route("/oauth/redirect", methods=['GET'])
def oauth():
    code = request.args.get("code")
    bdo = BaiduOauth('baidu')
    bdo.get_access_token(code)
    user_data = bdo.get_user_info()
    return jsonify(user_data)
