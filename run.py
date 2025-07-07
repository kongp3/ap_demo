import os
from app import create_app

# 设置当前工作目录为项目根目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)