import pickle
import subprocess


subprocess.CalledProcessError
class BaseExce(object):
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

class Exce(object):
#class Exce(BaseExce):
    def __init__(self, *args, **kwargs):
#    def __init__(self):
        pass
    def f(self):
        print('aa')


class GoodExc(Exception):
    def __init__(self):
        pass


class GoodExc2(Exception):
    def __init__(self, a):
        super(GoodExc2, self).__init__(a)


class BadExc(Exception):
#class BadExc(Exce):
    def __init__(self, a):
        pass


class BadExc2(Exception):
#class BadExc2(Exce):
    def __init__(self, a):
        super(BadExc2, self).__init__()


#s = pickle.dumps(GoodExc())
#pickle.loads(s)
#s = pickle.dumps(GoodExc2(123))
#pickle.loads(s)
#BadExc2(123)
#s = pickle.dumps(BadExc(123), protocol=2)
s = pickle.dumps(BadExc(123))
o = pickle.loads(s)
s = pickle.dumps(BadExc2(123))
pickle.loads(s)
