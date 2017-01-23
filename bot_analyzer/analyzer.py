# module for analyzing existing bot.
import re
# default template file
default_file = 'template.py'


def load(filename):
    '''
    loads file named filename to a string
    '''
    with open(filename) as f:
        return '\n'.join(f)


def save(string, filename):
    '''
    saves string to file named filename
    '''
    with open(filename, 'w') as f:
        f.write(string)

def manipulate(string):
    place = re.search(u'def do_turn\(.+\):', string).end(0)
    print place

if __name__ == "__main__":
    import sys
    manipulate(load(sys.argv[1]))
    #save(manipulate(load(sys.argv[1])),sys.argv[2])