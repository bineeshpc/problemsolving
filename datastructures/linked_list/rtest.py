import argparse
import linkedlist


def parse_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", help="enter the test function to use")
    parser.add_argument("inputfile", help="enter the test inputfile to use")
    parser.add_argument("-e", "--element", type=int,
                    help="element to be deleted")
    args = parser.parse_args()
    return args

def create_list(args):
    with open(args.inputfile) as f:
        line = f.readline()
    lst1 = [int(i) for i in line.split()]
    lst = linkedlist.List()
    lst.createlist(lst1)
    return lst

def test_create_list(args):
    lst = create_list(args)
    print lst.tolist()


def test_delete(args):
    lst = create_list(args)
    lst.delete(args.element)
    print lst.tolist()


def test_delete_elements(args):
    lst = create_list(args)
    with open(args.inputfile) as f:
        _ = f.readline()     # ignore the first line with elements to create
        line = f.readline()  # read second line with elements to delete
        elements_to_delete = [int(x) for x in line.split()]
    for element in elements_to_delete:
        lst.delete(element)
    print lst.tolist()

if __name__ == '__main__':
    args = parse_cmdline()
    test_function_name = args.function
    test_function = globals()[test_function_name]
    test_function(args)
