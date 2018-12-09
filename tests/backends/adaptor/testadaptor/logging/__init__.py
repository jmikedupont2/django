import pprint

def doprint(*args,**kwargs):
    pass
    #pprint.pprint([args, kwargs])
    #if 'extra' in kwargs:
    #    if sql 
    
config = 1
class Logger:
    def addHandler(self):
        pass
    def error(*args,**kwargs):
        doprint(*args, **kwargs)
    def debug(*args,**kwargs):
        doprint(*args, **kwargs)
    def info(*args,**kwargs):
        doprint(*args, **kwargs)
    def warning(*args,**kwargs):
        doprint(*args, **kwargs)
    
class Handler:
    pass
class NullHandler(Handler):
    pass
class Filter:
    pass
class Formatter:
    pass
class StreamHandler:
    pass

def getLogger(name):
    return Logger
