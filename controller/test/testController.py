from flask_restful import Resource
from service.testService import testService


class testController(Resource):
    def __init__(self):
        self.request_method = ""

    def get(self):
        self.request_method = "get"
        msg = "%s 请求" % self.request_method
        info = testService().test_service()
        return {"msg": msg, "info": info}

    def post(self):
        self.request_method = "post"
        msg = "%s 请求" % self.request_method
        info = testService().test_service()
        return {"msg": msg, "info": info}

    def put(self):
        self.request_method = "put"
        msg = "%s 请求" % self.request_method
        info = testService().test_service()
        return {"msg": msg, "info": info}

    def delete(self):
        self.request_method = "delete"
        msg = "%s 请求" % self.request_method
        info = testService().test_service()
        return {"msg": msg, "info": info}