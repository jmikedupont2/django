import pprint

def get_type(v):
    return type(v)


seen = {}
def t(v):
    d = {}
    for x in dir(v) :
        if hasattr(v,x)        :
            v2 = getattr(v,x)
        else:
            v2 = "'MissingAttr'"
        d[x]=c(v2)
def mw(v):
    return str(v)

def myeval(v):
    if not isinstance(v, str):
        vt = type(v) 
        #print (vt)
        tn = vt.__name__
        if  tn == 'type':
            return t(v)
        if tn == 'builtin_function_or_method':
            return  mw(v)
        if tn  in ( 'method-wrapper', 'wrapper_descriptor','method_descriptor'):
            return mw(v)
        if tn in ('int', 'tuple', 'bytes'):
             v = "{}".format(v)
        if tn in ('tuple'):
            if len(v) < 10:
                v = "{}".format(v)
            else:
                return "LongTuple"

    #print ("going to compile '{}' of type {}".format(v, type(v).__name__))
    try :
        code = compile(filename='test.py',source=v, mode='single')
    except SyntaxError as e:
        return e
    except TypeError as e:
        print ("typeerror {} {} {}".format(e, v, type(v).__name__))
        return e
    
    #[x for x in dir(code) if not x.startswith('_')]
    d = {
        'source': v,
    }
    for x in dir(code) :
        if not x.startswith('_'):
            v2 = getattr(code,x)        
            d[x]=v2
    for g in globals():
        if g.startswith('get'):
            v2 = eval(g + "(code)")            
            d[g]=v2
    return d

def c(v):
    if not isinstance(v, str):
        vt = type(v) 
        tn = vt.__name__
        if tn in ( 'mappingproxy'):
            v = tn 

    try :
        if v in seen:
            return seen[v]
        else:
            seen[v]=None #block infinte recursion
    except Exception as e:
        print ("Check",e, tn)
        raise e
    d = myeval(v)    
    seen[v]=d
    return d
def main():
        
        #for x in ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']:
        #print(x, eval(x))
    for x in dir():
        print (x)

    for l in open ('examples.txt'):
        v = c(l.rstrip())
        #pprint.pprint(v)
        #print (','.join([str(x) for x in v['co_code']]))
        print (v['co_code'].hex())
        #print ()
        #pprint.pprint(v)
        
        
    

main()
