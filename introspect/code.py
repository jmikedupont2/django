x = compile(filename='',source='1',mode='single')
code_class = type(x)

#code_class(1,2,3,4,5,b'',(),(),(),'10','11',12,b'')


#            
#            
#            
#            
#            
#            
#            filename='foo', #10
#            name='bar', # 11
#            firstlineno=1) # 12
#            #|        
           
code0 = code_class(0,0,0,0,0,b'',(),(),(),'filename','name',12,b'')

for b1 in (
        '6400460064005300',
        '6400460064015300',
        '64005a0064015300',
        '6400640184005a0064025300'):
    code0 = code_class(0,# argcount=0,#1
                       0,# kwonlyargcount=0,#2
                       0,# nlocals=0,#3
                       0,# stacksize=0,#4
                       0,# flags=0, #5
                       bytes.fromhex(b1), #codestring=b'', #6
                       (), # constants='', #7
                       (), # names=(),#8
                       (), # varnames=(), #9
                       'filename', 
                       'name',
                       12, # first line no
                       b'' # lnotab
                       # freevars
                       # cellvars
    )
    
