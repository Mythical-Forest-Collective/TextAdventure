from sys import stdout
from time import sleep
from json import load as jload, dump as jdump

default_config = {
  'colour': True,
  'force_color_mode': None
}

config = {}

try:
    with open('config.json') as f:
        config = jload(f)
except FileNotFoundError:
    config.update(default_config)
    with open('config.json', 'w+') as f:
        jdump(config, f, indent=4)

config = {**default_config, **config}

with open('config.json', 'w+') as f:
    jdump(config, f, indent=4)

if not config.get('colour', True):
    _color = '0'
    __import__('os').environ['FORCE_COLOR'] = _color

if config.get('force_color_mode', None):
    _color = str(config['force_color_mode'])
    __import__('os').environ['FORCE_COLOR'] = _color


def typer(*text, delay=0.05, sep=' ', end='\n', file=stdout):
    x = 0
    text = sep.join(text)
    skip = []

    for i in range(len(text)):
        if text[i] == '\x1b' and text[i+4] == 'm': # \x1b[31m
            skip.extend(range(i, i+5))
        elif text[i] == '\x1b' and text[i+9] == 'm': #\x1b[38;5;71m
            skip.extend(range(i, i+10))
        elif text[i] == '\x1b' and text[i+16] == 'm': # \x1b[38;2;51;153;51m
            skip.extend(range(i, i+17))

    for i in text:
        print(i, flush=True, file=file, end='')
        if not x in skip:
            sleep(delay)
        x += 1
    print(end=end)
