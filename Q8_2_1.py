import pathlib
a = pathlib.Path('.')
for pf in a.iterdir():
    if pf.is_file():
        print(str(pf))

