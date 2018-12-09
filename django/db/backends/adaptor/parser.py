import sqlparse
import pprint

from sqlparse import tokens
from sqlparse.sql import (Token, 
                          Function,
                          Parenthesis,
                          IdentifierList,
                          Identifier,
                          Where)

d = {}

def food2(x):
    for f in ('_get_repr_name',
              '_get_repr_value',
              ):
        if hasattr(x,f):
            v = getattr(x,f)
            v2= v()
            v3 = str(f) + str(v2 )
            if v3 not in d:
                d[v3]=1
                print (f, v2)
def function(x):
    # selector of table and fieldnames, occurs only in inserts
    print ("FUNC",x)
    #pass

def token(x):
    if x.ttype == tokens.Whitespace:
        pass
    elif x.ttype == tokens.Punctuation:
        if x.value == ',': # comma
            pass
        else:
            print ("token punc",x.value)
    else:
        print ("token other", x, x.ttype, x.value)
    #print(dir(x))
def paren(x):
    print ("paren", x)
    # contains the data inserted
    pass

    
def idlist(x):
    print ("idl", x)
def idf(x):
    print ("id", x)
def where(x):
    print ("where", x)
def foo(x):
    c = x.__class__
    cn = c.__name__

    if c == Function:
        #print (x)
        function(x)
    elif c == Token:
        token(x)
    elif c == Parenthesis:
        paren(x)
    elif c == IdentifierList:
        idlist(x)
    elif c == Identifier:
        idf(x)
    elif c == Where:
        where(x)
    else:
        print ("What",x)
                          
    # if cn not in d:
    #     d[cn]=1
    #     #print (x.__class__, cn)
    #     print ("from sqlparse.sql import {}".format(cn))
    
    # for f in (
    #         '_pprint_tree',
    #         '_get_repr_name',
    #         '_get_repr_value'):
    #     if hasattr(x,f):
    #         v = getattr(x,f)
    #         v2= v()
    #         v3 = str(f) + str(v2 )
    #         if v3 not in d:
    #             d[v3]=1
    #             print (f, v2)

    #print (x.__class__, dir(x))
#     for f in (
# #              'is_group',
# #              'is_keyword',
# #              'is_whitespace',
# #              'normalized',
#               'ttype',
# #              'value',
#               ):
#         if hasattr(x,f):
#             v = getattr(x,f)
#             v2 = v
#             v3 = str(f) + str(v2 )
#             #if v3 not in d:
#             #    d[v3]=1
#             print (x.__class__.__name__, f, v2)





for x in open('sql.txt'):
    sql = x.rstrip()
    if sql:
        statement = sqlparse.parse(sql)
        #print("sql_parse", statement)
        #print("sql_parse", pprint.pformat(statement))
        for x in statement:
            #print("sql_parse", pprint.pformat(x))
            #print("sql_parse tree", pprint.pformat(x._pprint_tree()))
            #print("sql_parse flatten", pprint.pformat([y for y in x.flatten()]))

            c = x.__class__
            ttype = "unknown"
            if hasattr(x, 'get_type'):
                ttype = x.get_type()
            tablename = ""
            if hasattr(x, 'get_name'):
                tablename = x.get_name()
            print("\n\n","NEW",tablename, ttype, c)
            for y in x:
                #pprint.pprint(dir(y))
                foo(y)
