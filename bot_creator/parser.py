from __future__ import print_function

import re


def python_token_scope_parser(token, bot_file_path):
    """
    
    :param token: Python's language token (such as 'def', 'class' etc.)
    :param bot_file_path: ython (.py) file.
    :return: Dictionary which maps every token's namespace, found in $bot_file_path, to its body.
    """
    assert bot_file_path.endswith('.py') or bot_file_path.endswith('.py\\'), \
        "File type is not supported."

    token_dict = {}

    is_inside_token_scope = True

    current_func_name = None
    current_func = ''

    def add_func(function_body):
        if function_body != '':
            token_dict[current_func_name] = (function_body.strip())

    with open(bot_file_path, 'r') as bot_file:
        for line in bot_file.readlines():

            # Check if this is an empty line, and ignore it
            if line.strip() == '':
                pass

            # Check if the current line contains static code.
            elif not line.startswith('    ') and not line.startswith('\t'):
                is_inside_token_scope = False

            # If we are at the beginning of token's scope
            if line.startswith(token):
                add_func(current_func)
                current_func = ''

                is_inside_token_scope = True
                current_func_name = re.split(' +|\(', line)[1]

            if is_inside_token_scope:
                current_func += '\n' + line

            else:
                add_func(current_func)
                current_func = ''

    return token_dict


def func_parser(bot_file_path):
    """
    :param bot_file_path: Python (.py) file.
    :return: Dictionary which maps every static function's name, found in $bot_file_path, to its body.
    """
    return python_token_scope_parser('def ', bot_file_path)

def class_parser(bot_file_path):
    """
    
    :param bot_file_path: Python (.py) file.
    :return: Dictionary which maps every class's name, found in $bot_file_path, to its body.
    """
    return python_token_scope_parser('class ', bot_file_path)
