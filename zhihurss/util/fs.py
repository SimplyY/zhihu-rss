import os


def mkdirp(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass
    except:
        raise


def ensure_dir(path):
    dirname = os.path.dirname(path)
    if not os.path.isdir(dirname):
        mkdirp(dirname)
