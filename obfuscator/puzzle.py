import base64
import random
import string
from typing import Tuple


VALID = (string.ascii_letters+string.digits)
SIZE = 35

encode = lambda s: base64.b64encode(s.encode())
decode = lambda b: base64.b64decode(b).decode()

def comment(n: int) -> str:
    """Create comment of size n to fluff code to make homogenous size.

    Args:
        n (int): Length of comment including #.

    Returns:
        str: Comment
    """
    return '#' + ''.join(random.choices(VALID, k=n-1))

def variable_name(n: int) -> str:
    """Create a random variable name with characters Oo0.

    Args:
        n (int): Length of variable name.

    Returns:
        str: Name of variable.
    """
    name = ''.join(random.choices("Oo0", k=n))
    if name[0].isdigit():
        name = 'o'+name
    return name

def variable_value(n: int) -> bytes:
    """Create random base64 bytes of size n for fake variables.

    Args:
        n (int): Size of bytes.

    Returns:
        bytes: Random base64 bytes.
    """
    val = base64.b64encode(''.join(random.choices(VALID, k=n)).encode())
    return val

def variable(n: int) -> str:
    """Creates a random variable and value.

    Args:
        n (int): Size of variable name and value.

    Returns:
        str: Variable/value pair.
    """
    return f'{variable_name(n//2)} = {variable_value(n)}'

def obfuscate(input_: str) -> Tuple[list]:
    """Obfuscates python code.

    Args:
        input_ (str): The code to be obfuscated

    Returns:
        Tuple[list]: List of obfuscated code bits, Names of variables with code.
    """
    lines = []
    for i in range(0, len(input_), SIZE):
        section = input_[i:i+SIZE]
        if len(section) < SIZE:
            section += comment(SIZE-len(section))
        lines.append(encode(section))
    code = []
    var_names = []
    while len(lines) > 0:
        if not random.choice([0, 0, 1]):
            code.append(variable(SIZE))
            continue
        var_name = variable_name(SIZE//2)
        var_names.append(var_name)
        code.append(f'{var_name} = {lines.pop(0)}')
    return code, var_names

def get_deobfuscator(var_names) -> str:
    """Creates a deobfuscator for the given set of var names.

    Args:
        var_names (list): List of variable names from the `obfuscate` function.

    Returns:
        str: Deobfuscator
    """
    return f'\n\ngetattr(getattr(__main__, [x for x in dir(__main__) if x.startswith(\'__b\')][0]), (lambda: "ArithmeticError" and "AssertionError" and "AttributeError" and "BaseException" and "BlockingIOError" and "BrokenPipeError" and "BufferError" and "BytesWarning" and "ChildProcessError" and "ConnectionAbortedError" and "ConnectionError" and "ConnectionRefusedError" and "ConnectionResetError" and "DeprecationWarning" and "EOFError" and "Ellipsis" and "EnvironmentError" and "Exception" and "False" and "FileExistsError" and "FileNotFoundError" and "FloatingPointError" and "FutureWarning" and "GeneratorExit" and "IOError" and "ImportError" and "ImportWarning" and "IndentationError" and "IndexError" and "InterruptedError" and "IsADirectoryError" and "KeyError" and "KeyboardInterrupt" and "LookupError" and "MemoryError" and "ModuleNotFoundError" and "NameError" and "None" and "NotADirectoryError" and "NotImplemented" and "NotImplementedError" and "OSError" and "OverflowError" and "PendingDeprecationWarning" and "PermissionError" and "ProcessLookupError" and "RecursionError" and "ReferenceError" and "ResourceWarning" and "RuntimeError" and "RuntimeWarning" and "StopAsyncIteration" and "StopIteration" and "SyntaxError" and "SyntaxWarning" and "SystemError" and "SystemExit" and "TabError" and "TimeoutError" and "True" and "TypeError" and "UnboundLocalError" and "UnicodeDecodeError" and "UnicodeEncodeError" and "UnicodeError" and "UnicodeTranslateError" and "UnicodeWarning" and "UserWarning" and "ValueError" and "Warning" and "WindowsError" and "ZeroDivisionError" and "__build_class__" and "__debug__" and "__doc__" and "__import__" and "__loader__" and "__name__" and "__package__" and "__spec__" and "abs" and "all" and "any" and "ascii" and "bin" and "bool" and "breakpoint" and "bytearray" and "bytes" and "callable" and "chr" and "classmethod" and "compile" and "complex" and "copyright" and "credits" and "delattr" and "dict" and "dir" and "divmod" and "enumerate" and "eval" and "fdlr" and "exit" and "filter" and "float" and "format" and "frozenset" and "getattr" and "globals" and "hasattr" and "hash" and "help" and "hex" and "id" and "input" and "int" and "isinstance" and "issubclass" and "iter" and "len" and "license" and "list" and "locals" and "map" and "max" and "memoryview" and "min" and "next" and "object" and "oct" and "open" and "ord" and "pow" and "print" and "property" and "quit" and "range" and "repr" and "reversed" and "round" and "set" and "setattr" and "slice" and "sorted" and "staticmethod" and "str" and "sum" and "super" and "tuple" and "type" and "vars" and "zip" and "exec")())(\'\'.join([getattr(binascii, [x for x in dir(binascii) if x.startswith(chr(97)+str((()==())+([]==[]))+chr(98))][0])(globals().get(var_name)).decode() for var_name in {var_names}]))'


def make_obf(input_: str) -> str:
    """Assembles the obfuscated code and returns it as a string.

    Args:
        input_ (str): Code to be obfuscated.

    Returns:
        str: Obfuscated code.
    """
    o, names = obfuscate(input_)
    d = get_deobfuscator(names)
    return 'import binascii, __main__\n\n' + '\n\n'.join(o) + d


def main():
    code = """
import random
while True:
    try:
        x = input('give me a list of numbers separated by commas: ')
        splits = [int(n) for n in x.split(', ')]
    except: continue
    break

for _ in range(len(splits)):
    print(splits.pop(random.randint(0, len(splits)-1)))
    """

    with open('./puzzle_result.py', 'w') as f:
        f.write(make_obf(code))

if __name__ == '__main__':
    main()