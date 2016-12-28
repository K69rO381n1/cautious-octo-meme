from __future__ import print_function


def func_parser(bot_file_path):
    assert bot_file_path.endswith('.py') or bot_file_path.endswith('.py\\'), \
        "File type is not supported."

    func_list = []

    is_in_the_middle_of_func = False
    current_func = ''

    with open(bot_file_path, 'r') as bot_file:

        for line in bot_file.readlines():

            if line.startswith('def'):
                is_in_the_middle_of_func = True

            elif not line.startswith('    '):
                is_in_the_middle_of_func = False

            if is_in_the_middle_of_func:
                current_func += '\n' + line

            elif current_func != '':
                func_list.append(current_func.strip('\n'))
                current_func = ''

    return func_list


if __name__ == '__main__':
    print(func_parser('actions.py'))
