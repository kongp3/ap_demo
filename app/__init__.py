import os
from flask import Flask
from app.controller.audit_controller import audit_bp
from app.controller.main_controller import main_bp
from app.controller.draft_controller import draft_bp
from app.util.database import engine, Base
from config import Config
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 配置静态文件夹 - 使用绝对路径
    app.static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

    # 初始化数据库
    Base.metadata.create_all(bind=engine)

    # 注册蓝图
    app.register_blueprint(main_bp)
    app.register_blueprint(audit_bp)
    app.register_blueprint(draft_bp)

    # 全局允许跨域
    CORS(app, supports_credentials=True)

    return app