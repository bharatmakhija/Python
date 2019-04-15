# closures
import logging

logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
        # Necessary for closure to work (returning WITHOUT parenthesis)

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

# here add_logger and sub_logger are having log_func passed to it. So basically two instances of log_func are created at
# at seperate memory locations so add_logger is pointing to one log_func instance that has add method and sub_logger points
# to another one.
# Even though log_func is out of scope of logger method, it remembers that what func (add and sub) was passed to it so basically when we execute add_logger or
# sub_logger those add and sub methods will be called.

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)