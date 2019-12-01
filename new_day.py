import os

DIR = os.path.abspath(os.path.dirname(__file__))


def get_day():
    return input('What day should we generate?\n> ')


def make_dir(day):
    path = os.path.join(DIR, day)
    try:
        os.mkdir(path)
    except Exception as e:
        print(f'Error creating directory: {e}')
    else:
        print(f'Directory {day} created successfully.')


def load_contents(path):
    print(f'Loading contents in {path}...')
    with open(path) as f:
        out = f.read()

    return out


def write_contents(contents, path):
    print(f'Writing contents in {path}...')
    with open(path, 'w') as f:
        f.write(contents)


def copy_template(day):
    template_path = os.path.join(DIR, 'template')
    for f in os.listdir(template_path):
        file_path = os.path.join(template_path, f)
        if os.path.isfile(file_path):
            contents = load_contents(file_path)
            contents = contents.replace('xx', day)
            f = f.replace('xx', day)
            out_path = os.path.join(DIR, day, f)
            write_contents(contents, out_path)


def main():
    day = get_day()
    make_dir(day)
    copy_template(day)


if __name__ == '__main__':
    main()
