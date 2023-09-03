import os
import yaml


class Config(object):
    configs = {}

    def __init__(self):
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config")
        for item in os.listdir(config_path):
            config_file = os.path.join(config_path, item)
            config_key = item.removesuffix(".yaml")
            with open(config_file, mode="r", encoding="utf-8") as f:
                self.configs[config_key] = yaml.load(f.read(), Loader=yaml.FullLoader)

    @classmethod
    def get_wx_path(cls):
        self = cls()
        return self.configs["maotai"].get("wx_path")

    @classmethod
    def boot_waiting_sec(cls):
        self = cls()
        return self.configs["maotai"].get("boot_waiting_sec")

    @classmethod
    def qrcode_refresh_waiting_sec(cls):
        self = cls()
        return self.configs["maotai"].get("qrcode_refresh_sec")

    @classmethod
    def get_app_port(cls):
        self = cls()
        return self.configs["maotai"].get("server.port")
