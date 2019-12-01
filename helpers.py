import os


def load_inputs_lines(folder, file_name, out_type=None):
    path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        folder,
        file_name
    )
    with open(path) as f:
        out = f.readlines()

    if out_type == 'int':
        out = [int(o) for o in out]

    return out
