import sys
import time
import os
import commands
import six


def prevent_multiple_runs(func):
    running_indicator = 'hello_running'
    while True:
        if not os.path.exists(running_indicator) and commands.getstatusoutput('ps -ef | grep hello'):
            with open(running_indicator, 'w') as f:
                func()
            os.remove(running_indicator)
            break
        six.print_('hello is already running, waiting for it to complete')
        time.sleep(5)


def prevent_multiple_runs_dec(func):
    """
    This function is used to decorate the func 
    and this is used to 
    """
    def wrapper():
        running_indicator = 'hello_running'
        while True:
            if not os.path.exists(running_indicator) and commands.getstatusoutput('ps -ef | grep hello'):
                with open(running_indicator, 'w') as f:
                    func()
                os.remove(running_indicator)
                break
            six.print_('hello is already running, waiting for it to complete')
            time.sleep(5)
    return wrapper


"""
I am decorating the function run with prevent multiple runs dec function
There are other ways to do this
for example
A call like this also would have given me the same result
prevent_multiple_runs(run)
Decorator is just a different way of achieving the same result
"""
@prevent_multiple_runs_dec
def run():
    for i in range(6):
        print('hello {}'.format(i))
        time.sleep(5)


# prevent_multiple_runs(run)


run()