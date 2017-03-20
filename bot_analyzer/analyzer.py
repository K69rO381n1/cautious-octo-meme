# module for analyzing existing bot.
from os.path import splitext

# default template file
default_file = 'template.py'

TAB = '    '

PYTHON_EXT = '.py'
JAVA_EXT = '.java'
C_SHARP_EXT = '.cs'

PY_DO_TURN_STATEMENT = u'def do_turn\(.+\):'
PY_GAME_WRAPPER_PATH = u'\bot_analyzer\game_wrapper.py'
PY_GAME_OBJECT_WRAPPING = TAB + u'game = GameWrapper(game)'


def load(filename):
    """
    loads file named filename to a string
    """
    with open(filename) as f:
        return '\n'.join(f)


def save(string, filename):
    """
    saves string to file named filename
    """
    with open(filename, 'w') as f:
        f.write(string)


def inject(code, search_string, inject_string, place_before_or_after):
    return code.replace(search_string,
                        search_string + inject_string if
                        place_before_or_after else
                        inject_string + search_string, count=1)


def inject_adapter(bot_file_path, new_bot_path):
    code = load(bot_file_path)

    if splitext(bot_file_path)[1] == PYTHON_EXT:

        code = inject(code, PY_DO_TURN_STATEMENT, PY_GAME_OBJECT_WRAPPING, True)

    elif splitext(bot_file_path)[1] == JAVA_EXT:
        pass

    elif splitext(bot_file_path)[1] == C_SHARP_EXT:
        pass
    
    save(code, new_bot_path)

if __name__ == "__main__":

    import sys

    inject_adapter(sys.argv[1])
    # save(manipulate(load(sys.argv[1])),sys.argv[2])
