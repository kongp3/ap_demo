# -*- coding: utf-8 -*-
from flask import request, render_template, jsonify
from config import app, WEB_HOST
from api import error_handler

from application.ap_operator import get_result


@app.route('/ap_data', methods=['GET'])  # 门禁系统文档要求的url
@error_handler
def ap_data(**kwargs):
    response = kwargs.get("response")
    # id = request.values.get('id')
    results = get_result()
    print(results)
    # return response.success(data=jsonify(cp_info))
    return response.success(data=results)


@app.route('/ap_web', methods=['GET'])
def index(**kwargs):
    return render_template('ap_web1.2.html', host=WEB_HOST)
