import traceback

def safe(default=None):
    def wrapper(func):
        def inner(*args, **kw):
            try: return func(*args, **kw)
            except: 
                traceback.print_exc()
                return default
        return inner
    return wrapper