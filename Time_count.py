import datetime
# 用于统计运行时间的装饰器
def timecount(func):
    def wr(*args,**kw):
        starttime = datetime.datetime.now()
        func(*args,**kw)
        endtime = datetime.datetime.now()
        print ("time:"+str(endtime - starttime))
    return wr