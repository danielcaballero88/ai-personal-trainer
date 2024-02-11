import os


HERE = os.path.dirname(__file__)


def get_dirname(filepath, n):
    dirname = filepath
    for i in range(n):
        dirname = os.path.dirname(dirname)
    return dirname


def get_project_root():
    return get_dirname(HERE, 2)
