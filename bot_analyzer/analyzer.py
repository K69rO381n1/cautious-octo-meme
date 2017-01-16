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
    place = re.match(u'def do_turn\(.+\):')