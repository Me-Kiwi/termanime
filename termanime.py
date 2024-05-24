
#!/usr/bin/env python

import argparse
import os
import subprocess
import random
import PIL 
from PIL import Image  

themes_dir = os.path.expanduser('~/.config/termanime/themes')
config_dir = os.path.expanduser('~/.config/termanime/termanime.conf')

def get_theme() :
    with open(config_dir, 'r') as f:
        return f.read().strip()

def print_list() : 
    for i in os.listdir(themes_dir):
        print(i)


def print_img(theme) : 
    path = os.path.join(themes_dir,theme if theme else get_theme())
    for i in os.listdir(path) :
        print(i)

def new_theme(set_theme) :
    path = os.path.join(themes_dir, set_theme)
    if not os.path.exists(path):
        print('Directory does not exists')
    else:
        with open(config_dir, 'w') as f:
            f.write(set_theme)
            
def add_image(add_img, name, theme) :
    img = PIL.Image.open(add_img)
    basename = os.path.basename(add_img)
    wid, hgt = img.size
    new_hgt = 300
    new_wid = int(new_hgt*wid/hgt)
    img_resized = img.resize((new_wid, new_hgt),PIL.Image.LANCZOS)
    if theme :
        path = os.path.join(themes_dir, theme)
        if not os.path.exists(path) :
            os.mkdir(path)
        path = os.path.join(path, name if name else basename)
    else :
        path = os.path.join(themes_dir, get_theme(), name if name else basename)
    img_resized.save(path)

def print_image() :
    theme = get_theme()
    path = os.path.join(themes_dir, theme)
    random_img = random.choice(os.listdir(path))
    display_image = os.path.join(path, random_img)
    subprocess.run(["/usr/bin/kitty", "icat", "--align", "left", display_image])

def main() -> None :
    parser = argparse.ArgumentParser(
    prog='termanime',
    description='Prints your favorate anime in terminal',
    epilog='2024 hyperland zsh kitty'
    )

    parser.add_argument(
        '-s',
        '--set-theme',
        help = 'select theme by name'
    )
    parser.add_argument(
        '-g',
        '--get-theme',
        action='store_true',
        help = 'help'
    )
    parser.add_argument(
        '-m',
        '--mk-theme',
        help = 'help'
    )
    parser.add_argument(
        '-lt',
        '--list-theme',
        action='store_true',
        help = 'help'
    )
    parser.add_argument(
        '-li',
        '--list-img',
        action='store_true',
        help = 'help'
    )
    parser.add_argument(
        '-a',
        '--add-img',
        help = 'help'
    )
    parser.add_argument(
        '-t', 
        '--theme',
        help = 'help'
    )
    parser.add_argument(
        '-n',
        '--name',
        help = 'help'
    )
    parser.add_argument(
        '-r',
        '--remove-img',
        help = 'help'
    )
    args = parser.parse_args()

    if args.list_theme :
        print_list()
    elif args.list_img :
        print_img(args.theme)
    elif args.get_theme:
        print(get_theme())
    elif args.set_theme :
        new_theme(args.set_theme)
    elif args.add_img :
        add_image(args.add_img, args.name, args.theme)
    elif args.remove_img :
        path = os.path.join(themes_dir, args.theme if args.theme else get_theme(), os.path.basename(args.remove_img))
        os.remove(path)
    elif args.mk_theme :
        path = os.path.join(themes_dir, args.mk_theme)
        os.mkdir(path)
    else :
        print_image()
        
if __name__ == "__main__" :
    main()
