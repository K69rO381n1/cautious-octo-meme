# module for analyzing existing bot.
from os.path import splitext

# default template file
from bot_creator.parser import func_parser

default_file = 'template.py'

TAB = '    '

PYTHON_EXT = '.py'
JAVA_EXT = '.java'
C_SHARP_EXT = '.cs'

PY_DO_TURN_STATEMENT = 'def do_turn(game):'
# PY_GAME_WRAPPER_PATH = u"\bot_analyzer\game_wrapper.py"
PY_GAME_OBJECT_WRAPPING = '\n' + TAB + u'game = GameWrapper(game)'
PY_PARAM_DICT_INITIALIZATION_STATEMENT = u'param_dict = '


def load(filename):
    """
    loads file named filename to a string
    """
    with open(filename) as f:
        return ''.join(f)


# Required the modules below:
PY_GAME_WRAPPER = load('game_wrapper.py') + '\n'

# Clear from sub-imports
PY_PARAM_DICT_PROTOCOL = load('param_dict_protocol.py')

# Clear from sub-imports
analyzers_functions = func_parser('analyzer.py')
PY_SAVE_FUNC = analyzers_functions['save']
PY_PARAM_DICT_TO_STRING_FUNC = analyzers_functions['param_dict2str']
del analyzers_functions

# The entire class is needed because od the multiple dependencies
PY_PIRATE_CLASS = load('pythonRunner.py')


def save(string, filename):
    """
    saves string to file named filename
    """
    with open(filename, 'w') as f:
        f.write(string)


def inject(code, search_string, inject_string, place_before_or_after):
    """
    :param code:    string which contains python code.
                    Other languages support (such as Java, Cs) will come in the future.
    :param search_string:   The sub-string which we will place $inject_string in a relative location to.
    :param inject_string:   The code that we want to inject.
    :param place_before_or_after:   The direction which we will place $inject_string: True => After, False => Before.
    :return:    The modified code (after the injection).
    """
    return code.replace(search_string,
                        search_string + inject_string if
                        place_before_or_after else
                        inject_string + search_string, 1)


def inject_adapter(bot_file_path, new_bot_path=None):
    """
    This function takes a bot file (We assume it fills the game's requirements, i.e do_turn func)
    and inject all the code required for the monitoring process. 
    :param bot_file_path:   Path to the bot's file
    :param new_bot_path:    Path to the new bot (which has the adapter injected).
                            Using the default value will cause overriding the original bot's code.
    """
    if new_bot_path is None:
        new_bot_path = bot_file_path

    code = load(bot_file_path)
    code_s = str(code)
    if splitext(bot_file_path)[1] == PYTHON_EXT:

        code = inject(code, PY_DO_TURN_STATEMENT, PY_GAME_WRAPPER, False)
        code = inject(code, PY_GAME_WRAPPER, PY_PIRATE_CLASS, False)
        code = inject(code, PY_GAME_WRAPPER, PY_PARAM_DICT_PROTOCOL, False)
        code = inject(code, PY_GAME_WRAPPER, PY_SAVE_FUNC, False)
        code = inject(code, PY_GAME_WRAPPER, PY_PARAM_DICT_TO_STRING_FUNC, False)

        code = inject(code, PY_DO_TURN_STATEMENT, PY_GAME_OBJECT_WRAPPING, True)

    elif splitext(bot_file_path)[1] == JAVA_EXT:
        pass

    elif splitext(bot_file_path)[1] == C_SHARP_EXT:
        pass
    print code == code_s
    save(code, new_bot_path)


def inject_param_dict(template_file_path, param_dict, new_bot_file=None):
    """
    This function takes a Bot template and inject the param_dict into it in order to make it operational.
    :param template_file_path:  See 'bot_creator\ template.py' for an example.
    :param param_dict:  Dictionary which fill the requirements found in 'bot_analyzer\ param_dict_protocol.py'.
    :param new_bot_file: Path to the new bot (which has the parameters dictionary injected).
                            Using the default value will cause overriding the original bot's code.
    """
    if new_bot_file is None:
        new_bot_file = template_file_path

    code = load(template_file_path)

    if splitext(template_file_path)[1] == PYTHON_EXT:

        code = inject(code, PY_PARAM_DICT_INITIALIZATION_STATEMENT, str(param_dict), True)

    elif splitext(template_file_path)[1] == JAVA_EXT:
        pass

    elif splitext(template_file_path)[1] == C_SHARP_EXT:
        pass

    save(code, new_bot_file)


if __name__ == "__main__":

    import sys

    inject_adapter(sys.argv[1])
