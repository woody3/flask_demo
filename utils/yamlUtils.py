import os
import yaml


class Config(object):
    @classmethod
    def parse(cls, file):
        config_file = os.path.join(os.path.dirname(os.getcwd(), "config", file))
        with open(config_file, mode="r", encoding="utf-8") as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    @classmethod
    def get_wx_path(cls):
        return cls.parse("maotai.yaml").get("wx_path")

    @classmethod
    def boot_waiting_sec(cls):
        return cls.parse("maotai.yaml").get("boot_waiting_sec")

    @classmethod
    def qrcode_refresh_sec(cls):
        return cls.parse("maotai.yaml").get("qrcode_refresh_sec")
