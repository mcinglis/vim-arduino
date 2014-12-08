#!/bin/env python3

# Copyright 2014 Malcolm Inglis <http://minglis.id.au>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from pathlib import Path


TEMPLATE_PATH = 'template.vim'

CPP_KEYWORDS = {
    'auto', 'const', 'double', 'float', 'int', 'short', 'struct', 'unsigned',
    'break', 'continue', 'else', 'for', 'long', 'signed', 'switch', 'void',
    'case', 'default', 'enum', 'goto', 'register', 'sizeof', 'typedef', 'volatile',
    'char', 'do', 'extern', 'if', 'return', 'static', 'union', 'while',
    'asm', 'dynamic_cast', 'namespace', 'reinterpret_cast', 'try',
    'bool', 'explicit', 'new', 'static_cast', 'typeid',
    'catch', 'false', 'operator', 'template', 'typename',
    'class', 'friend', 'private', 'this', 'using',
    'const_cast', 'inline', 'public', 'throw', 'virtual',
    'delete', 'mutable', 'protected', 'true', 'wchar_t',
}

GROUP_MAPPINGS = {
    'LITERAL1': 'arduinoConstant',
    'KEYWORD1': 'arduinoType',
    'KEYWORD2': 'arduinoFunc',
    'KEYWORD3': 'arduinoModule'
}


def main(argv, outfile, errfile):
    if len(argv) != 2:
        print('Usage: {} <arduino_root>'.format(argv[0]), file=errfile)
        return 1

    arduino_root = Path(argv[1])
    template_path = Path(argv[0]).parent / TEMPLATE_PATH
    for line in gen_syntax_file(arduino_root, template_path):
        print(line, end='', file=outfile)
    return 0


def gen_syntax_file(arduino_root, template_path):
    with template_path.open() as template_file:
        for line in template_file:
            if line == '{{{RULES}}}\n':
                for vg, ks in get_rules(arduino_root).items():
                    yield ('syntax keyword {:<16} {}\n\n'
                             .format(vg, ' '.join(sorted(ks))))
            else:
                yield line


def get_rules(arduino_root):
    acc = {vg: [] for vg in GROUP_MAPPINGS.values()}
    for vim_group, keyword in gen_rules(arduino_root):
        acc[vim_group].append(keyword)
    return acc


def gen_rules(arduino_root):
    with (arduino_root / 'lib' / 'keywords.txt').open() as keywords_file:
        done = set()
        for line in keywords_file:
            line = line.strip()
            if not line or line[0] == '#':
                continue
            fields = line.split()
            if len(fields) < 2:
                continue
            keyword, group = fields[:2]
            if ((keyword in done)
                    or (keyword in CPP_KEYWORDS)
                    or (group not in GROUP_MAPPINGS.keys())):
                continue
            done.add(keyword)
            yield GROUP_MAPPINGS[group], keyword


if __name__ == '__main__':
    import sys
    sys.exit(main(argv    = sys.argv,
                  outfile = sys.stdout,
                  errfile = sys.stderr))


