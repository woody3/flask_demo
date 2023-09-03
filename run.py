import logging
import os
import platform
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_restful import Api
from routers.router import api_router
from utils.configUtils import Config

os.environ["NLS_LANG"] = r"SIMPLIFIED CHINESE_CHINA.UTF8"
app = Flask(__name__)
api = Api(app)
app.config["JSON_AS_ASCII"] = False

for item in api_router:
    api.add_resource(item[0], item[1])


if __name__ == '__main__':
    log_path = "logs/logs.log"
    handler = RotatingFileHandler(log_path, maxBytes=200 * 1024 * 1024, backupCount=20, encoding="utf-8")
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - [line: %(lineno)d]: %(message)s")
    handler.setFormatter(fmt)
    logging.basicConfig(level=logging.INFO, handlers=[handler])

    if not app.logger.handlers:
        app.logger.addHandler(handler)

    if logging.root.hasHandlers():
        logging.root.removeHandler(handler)

    port = Config.get_app_port()
    if flag := False if platform.system().lower() in["windows", "darwin"] else True:
        shandler = logging.StreamHandler()
        shandler.setLevel(logging.DEBUG)
        shandler.setFormatter(fmt)
        app.logger.addHandler(shandler)
    app.run(host="0.0.0.0", debug=flag, port=port)


