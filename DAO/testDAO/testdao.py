class testDAO(object):
    def __init__(self):
        self.msg = "模拟数据库操作"

    def testQueryAll(self):
        print("%s: 全查询 " % self.msg)

    def testInsert(self, sql):
        print("%s: %s " % (self.msg, sql))

    def testUpdate(self, id):
        print("%s: %d " % (self.msg, id))

    def testDelete(self, id):
        print("%s: %d " % (self.msg, id))