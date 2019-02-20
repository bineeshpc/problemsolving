import importlib
import sys

def explore_package(module_name, level=0):
    prefix = level * '..'
    print(prefix + module_name)
    module_ = importlib.import_module(module_name)
    try:
        for sub_module in module_.__all__:
            explore_package(module_name + '.' + sub_module, level+1)
    except:
        print(prefix + 'no')

explore_package(sys.argv[1])
