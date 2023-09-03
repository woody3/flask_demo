from flask_restful import Resource, request
from flask import current_app as app

from service.wechat import Wechat


class QrcodeView(Resource):
    def __init__(self):
        self.mobile = ""
        self.merchant_name = ""

    def post(self):
        app.logger.info(f"入参: {request.json}")
        self.mobile = request.json.get("mobile")
        self.merchant_name = request.json.get("merchant_name")
        qrcode_str = Wechat.get_login_qrcode()
        data = {"qrcode": qrcode_str}
        return {"code": 0, "success": True, "data": data}