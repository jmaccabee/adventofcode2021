import importlib.util as iutil
import os


class NoRunnerFunctionFoundException(Exception):
    pass


BASE_DIR = '/Users/joshmaccabee/Desktop/aoc2021/'

def mkfilepath(file_or_dir, dir):
    abs_filepath = os.path.abspath(os.path.join(dir, file_or_dir))
    return abs_filepath


INPUT_DIR = mkfilepath('inputs/', BASE_DIR)


def read_input(filename, dir=INPUT_DIR, cast_type=int):
    filepath = mkfilepath(filename, dir)
    with open(filepath, 'r') as filehandle:
        data = [
            # drop empty line
            cast_type(line) for line in
            filehandle.readlines()
            if line != ''
        ]
        return data


def _run_module(module, dir=BASE_DIR):
    filepath = mkfilepath(module + '.py', dir)
    spec = (
        iutil.spec_from_file_location(f"{module}._runner", filepath)
    )
    executable = iutil.module_from_spec(spec)
    spec.loader.exec_module(executable)
    if not hasattr(executable, '_runner'):
        raise NoRunnerFunctionFoundException(
            f"{module} does not have a _runner property defined."
        )

    print(executable._runner())
