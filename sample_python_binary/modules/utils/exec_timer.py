import sys
import time

def exec_time(func):
    def count_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start
        if 'unittest' not in sys.modules.keys(): # check if running under unittest
            print("Total time taken in : ", func.__name__, execution_time)
        return result
    return count_time
    
