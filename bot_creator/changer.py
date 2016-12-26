from __future__ import print_function


def load(filename):
    with open(filename) as f:
        return '\n'.join(f)


def save(string, filename):
    with open(filename, 'w') as f:
        f.write(string)


def manipulate(string, array):
    string_mat = [[[str(e) for e in row] for row in mat] for mat in array]
    row_string_array = [['\t\t\t[' + ', '.join(row) + ']' for row in mat] for mat in string_mat]
    mat_strings = ['\t\tnp.array([\n' + ',\n'.join(mat) + '\n\t\t])' for mat in row_string_array]
    mats_string = ',\n'.join(mat_strings)
    return string.replace('#content', mats_string)


def load_matrix_array(filename):
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


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print('use as: changer.py <parameter-file> <output-file>[<template-file>]')
        sys.exit(0)
    if len(sys.argv) < 4:
        sys.argv.append('template.py')
    _, param_file, out_file, tmplt_file = sys.argv[:4]
    save(manipulate(load(tmplt_file), load_matrix_array(param_file)), out_file)
