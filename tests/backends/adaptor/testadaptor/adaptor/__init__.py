#
class Middleware :
    pass


def middleware(handler):

    def middleware2(request):

        return handler(request)
    
    return middleware2
