# -*- coding: utf-8 -*-
from config import app_host, app_port, app
from api.ap_data import *

if __name__ == '__main__':
    app.run(host=app_host, port=int(app_port))
