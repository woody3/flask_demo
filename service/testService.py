from DAO.testDAO.testdao import testDAO


class testService(object):
    def __init__(self):
        self.msg = ""

    def test_service(self):
        self.msg = "调用service层"
        testDAO().testQueryAll()
        return self.msg
