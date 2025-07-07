import os
from flask import Blueprint, send_from_directory, current_app

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    # 获取静态文件目录的绝对路径
    static_folder = current_app.static_folder

    # 发送index.html文件
    return send_from_directory(static_folder, 'index.html')


@main_bp.route('/<path:filename>')
def static_files(filename):
    # 处理静态文件请求
    return send_from_directory(current_app.static_folder, filename)