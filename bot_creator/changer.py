# module for creating bot from parameter matrix

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

def manipulate(string, array):
    '''
    inserts array of matrices into template string.
    '''
    string_mat = [[[str(e) for e in row] for row in mat] for mat in array]
    row_string_array = [['\t\t\t[' + ', '.join(row) + ']' for row in mat] for mat in string_mat]
    mat_strings = ['\t\tnp.array([\n' + ',\n'.join(mat) + '\n\t\t])' for mat in row_string_array]
    mats_string = ',\n'.join(mat_strings)
    return string.replace('#content', mats_string)


def load_matrix_array(filename):
    '''
    loads array of matrices from file
    '''
    with open(filename) as f:
        mats = [[]]
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            if len(line) == 0:
                mats.append([])
            else:
                mats[-1].append([float(s) for s in line.split(' ')])
        return mats

def create_bot(output_file, matrix_list, template_file = default_file)
    '''
    creates bot in output_file, using given matrix list and tamplate file
    '''
    save(manipulate(load(template_file), matrix_list), output_file)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print('use as: changer.py <parameter-file> <output-file>[<template-file>]')
        sys.exit(0)
    if len(sys.argv) < 4:
        sys.argv.append(default_file)
    _, param_file, out_file, tmplt_file = sys.argv[:4]
    create_bot( out_file, load_matrix_array(param_file)tmplt_file)
