import logging
logging.basicConfig(filename="closure.txt", level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(
            "Running '{}' with arguments {}".format(func.__name__, args)
        )
        print(func(*args))
    return log_func




def add (x,y):
    return x + y



def sub (x,y):
    return x - y



add_func = logger(add)
sub_func = logger(sub)

add_func(3,4)
add_func(33,44)
sub_func(35, 25)
sub_func(100, 25)