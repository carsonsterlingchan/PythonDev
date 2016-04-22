# This reverse function prints any strings, sets or tuples in reversed order. 
# This is to show how to take advantage of function decorator.

def reverse_wrapper(func):
    
    def wrapper(obj):
        
        if isinstance(obj, dict):
            raise Exception('reverse does not work on a dictionary')
        
        if obj == '':
            return ''
        elif obj == []:
            return []
        elif obj == ():
            return ()
        else:
            if isinstance(obj, set):
                aList = list(obj)
                reversed_obj = func(aList)
            else:
                reversed_obj = func(obj)
                
            if isinstance(obj, str):
                return ''.join(reversed_obj)
            elif isinstance(obj, list):
                return list(reversed_obj)
            elif isinstance(obj, tuple):
                return tuple(reversed_obj)
            else:
                return set(reversed_obj)
            
    return wrapper

@reverse_wrapper
def reverse(obj):    
    
    for i in range(len(obj)-1, -1, -1):
        yield obj[i]
