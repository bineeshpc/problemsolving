"""

Idea is to test every code I have written

This should run everyday on startup and get the result 
published with a date and time stamp

This should eventually change into a robotframework test or something

At the moment I am intending this to be very lightweight 

I should be able to see everything in action in the morning

I should get the test failure report

What directories should be tested should be configurable.


If I have this as a configurable option I can incrementally improve it to 

eventually test everything

"""

import os
import glob

def get_configuration():
    """
    Read the test config file and keep the configuration ready
    """
    class Conf:
        def __init__(self):
            self.directories = ["../", "../calculations"]
            self.outputdir = ["../../testoutput"]

        def is_directory_configured(self, directory):
            return directory in self.directories

    return Conf()

def execute(directory):
    python_files = glob.glob(os.path.join(directory, "*.py"))
    for python_file in python_files:
        #present_path = os.getcwd()
        #print(present_path)
        cmd = "python {}".format(python_file)
        print(cmd)
        os.system(cmd)
        #print(os.getcwd())
        #os.system("cd {}".format(present_path))
        #print(os.getcwd())


def test_everything(directory, conf):
    """
        Go into every sub directory
        if testing is enabled for directory 
            test it
            log it
    """
    #print(directory)
    
    if conf.is_directory_configured(directory) and os.path.isdir(directory):
        print(directory)
        files = os.listdir(directory)
        execute(directory)
        for file in files:
            full_filename = os.path.join(directory, file)
            test_everything(full_filename, conf)
    


def main():
    conf = get_configuration()
    test_everything("../", conf)

if __name__ == '__main__':
    main()