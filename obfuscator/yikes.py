from math import ceil, log
import textwrap


# not without much inspiration from Ben Kurtovic https://benkurtovic.com/2014/06/01/obfuscating-hello-world.html

def convert_to_bits(num, depth=0):
#  Written by Ben Kurtovic
    result = ""
    while num:
        base = shift = 0
        diff = num
        span = int(ceil(log(abs(num), 1.5))) + (16 >> depth)
        for i in range(span):
            for j in range(span):
                test_diff = abs(num) - (i << j)
                if abs(test_diff) < abs(diff):
                    diff = test_diff
                    base = i
                    shift = j
        if result:
            result += " + " if num > 0 else " - "
        elif num < 0:
            base = -base
        if shift == 0:
            result += encode(base, depth)
        else:
            result += "(%s << %s)" % (encode(base, depth),
                                      encode(shift, depth))
        num = diff if num > 0 else -diff
    return result

encode = (
    lambda num, depth: "_ - _"if num==0 else"_"*num if num<=8 else"("+
    convert_to_bits(num,depth+1)+")"
)
convert = lambda string: [sum([ord(c) for c in line][i] * 256 ** i for i in 
    range(len([ord(c) for c in line]))) for line in [string[i:i+50] for i in 
    range(0, len(string), 50)]]

obfuscate = [locals().__setitem__('obs', lambda code_or_fp, *, output=None, one_line=False, text_wrap=False: [locals().__setitem__('result', f"(lambda _, __, ___, ____, _____, ______, _______, ________:\n\tgetattr(\n\t\tgetattr(\n\t\t\t__import__(True.__abs__.__name__[:__]+\n\t\t\t__doc__.__format__.__name__[_____]+\n\t\t\t__annotations__.__contains__.\n\t\t\t__name__[______:(_<<___)+_]+\n\t\t\t__spec__.__reduce_ex__.__name__[\n\t\t\t________]*__),().__class__.\n\t\t\t__class__.__eq__.__name__[:__]+\n\t\t\tlen.__module__+....__class__.\n\t\t\t__class__.mro.__call__.__format__.\n\t\t\t__qualname__[-((__<<__)//(_<<__)):]\n\t\t),\n\t\t(\n\t\t\t__doc__.__eq__.__class__.\n\t\t\t__reduce_ex__.__name__[(((_ << \n\t\t\t___) + _)):((___ << __) - _)]+\n\t\t\t__import__.__hash__.__class__.\n\t\t\t__delattr__.__name__.maketrans.\n\t\t\t__text_signature__.capitalize.\n\t\t\t__name__[(((_ << ___) + _))]+\n\t\t\t__annotations__.copy.__class__.\n\t\t\t__eq__.__class__.__class__.mro.\n\t\t\t__subclasshook__.__qualname__[\n\t\t\t((___ << ___) - _)]\n\t\t)\n\t)(\n\t\t(\n\t\t\tlambda _____: getattr(\n\t\t\t\t__import__.__class__.\n\t\t\t\t__qualname__.__mul__(_-((__<<__\n\t\t\t\t) // (__<<__))),__import__.\n\t\t\t\t__init_subclass__.__getattribute__.\n\t\t\t\t__qualname__.join.__name__[(__<<__)-________]+\n\t\t\t\tConnectionAbortedError().__repr__()[\n\t\t\t\t-((_ << ____) + _):-((_ << ____) - _)\n\t\t\t\t][::-_]+__doc__.__dir__.__lt__.\n\t\t\t\t__init_subclass__.__text_signature__.__ne__.__name__[__]\n\t\t\t)(\n\t\t\t\t[\n\t\t\t\t\t(lambda _, __, ___:\n\t\t\t\t\t\t_(_, __, ___))(\n\t\t\t\t\t\tlambda _, __, ___: \n\t\t\t\t\t\t\tchr(__ % ___) + _(\n\t\t\t\t\t\t\t\t_, __ // ___, ___)\n\t\t\t\t\t\t\tif __ else \n\t\t\t\t\t\t\t\t__builtins__.globals.__class__.__class__.\n\t\t\t\t\t\t\t\t__module__.strip(([]==[]).__repr__()+....\n\t\t\t\t\t\t\t\t__class__.__name__+ConnectionAbortedError().\n\t\t\t\t\t\t\t\t__repr__()).__mul__(__import__(type.__class__.\n\t\t\t\t\t\t\t\t__class__.__name__[-~({{}}is{{}})].join((False.\n\t\t\t\t\t\t\t\t__str__.__name__[-~(()==())],)*-~(not not[(\n\t\t\t\t\t\t\t\t)]))).maxsize),\n\t\t\t\t\t\t_____,\n\t\t\t\t\t\t_ << ________\n\t\t\t\t\t) for _____ in _____\n\t\t\t\t]\n\t\t\t)\n\t\t)(\n\t\t\t{__import__('json').dumps([convert_to_bits(num) for num in (lambda string: [sum([ord(c) for c in line][i] * 256 ** i for i in range(len([ord(c) for c in line]))) for line in [string[i:i+50] for i in range(0, len(string), 50)]])((lambda fp: (lambda f: [f.read(),f.close][0])(open(fp, 'r')))(code_or_fp) if __import__('os').path.exists(code_or_fp) else code_or_fp)]).replace(chr(10), '').replace(chr(34), '')}\n\t\t), globals()\n\t))(\n\t\t*(lambda _, __, ___: _(_, __, ___))(\n\t\t\t(lambda _, __, ___:\n\t\t\t\t[__(___[(lambda: _).__code__.co_nlocals])] +\n\t\t\t\t_(_, __, ___[(lambda _: _).__code__.co_nlocals:]) if ___ else []\n\t\t\t),\n\t\t\tlambda _: _.__code__.co_argcount,\n\t\t\t(\n\t\t\t\tlambda _: _,\n\t\t\t\tlambda _, __: _,\n\t\t\t\tlambda _, __, ___: _,\n\t\t\t\tlambda _, __, ___, ____: _,\n\t\t\t\tlambda _, __, ___, ____, _____: _,\n\t\t\t\tlambda _, __, ___, ____, _____, ______: _,\n\t\t\t\tlambda _, __, ___, ____, _____, ______, _______: _,\n\t\t\t\tlambda _, __, ___, ____, _____, ______, _______, ________: _\n\t\t\t)\n\t\t)\n\t)"), [locals().__setitem__('result', __import__('re').sub(r"[\s]{2,}", ' ', locals().get('result'), 0, 8)), locals().get('result')][1] if one_line else locals().get('result'), (lambda fp, obj: (lambda f: [f.write(textwrap.TextWrapper(width=89).fill(text=obj) if text_wrap else obj), f.close()])(open(fp, 'w')))(output+'.py' if not output.endswith('.py') else output, locals().get('result')) if output else None][1]), locals().get('obs').__setattr__('__doc__', """Creates a string of the obfuscated program.\n\n    Args:\n        code_or_fp (str): The python code or the file path.\n        output (str, optional): The name of the output file. Defaults to no output file.\n        one_line (bool, optional): Return a formatted program or not. Defaults to False.\n        text_wrap (bool, optional): Text wrap at 89 characters or not. Defaults to False.\n\n    Returns:\n        str: Obfuscated code\n        file (on hard disk): The file with the obfuscated code if set.\n    """), locals().get('obs')][2]


if __name__ == '__main__':
    print(obfuscate.__doc__)
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
    obfuscate(
        code, # code (str) or filename (creates file)
        output='yikes_test', # name of file with or w/o .py extention
        one_line=True, # formatted or not (prefferably not)
        text_wrap=True # text wrap to show off in a terminal or IDE
    )
