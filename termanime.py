#!/usr/bin/env python

import argparse
import os
import toml
import subprocess
import random
import PIL 
from PIL import Image  

themes_dir = os.path.expanduser('~/.themes/termanime')
config_dir = os.path.expanduser('~/.config/termanime/termanime.conf')

cofig = {}

def load_config() :
    global config 
    config = toml.load(config_dir)

def save_config():
    if not os.path.exists(config_dir):
        print('Config file not found :(')
    else:
        with open(config_dir, 'w') as f:
            toml.dump(config, f)


def print_list() : 
    for i in os.listdir(themes_dir):
        print(i)

def print_img(theme) :
    path = ''
    if theme:
        path = os.path.join(themes_dir, theme)
        if not os.path.exists(path):
            print("Theme does not exist..")
            exit(1)
    else:
        path = os.path.join(themes_dir, config["theme"])

    for i in os.listdir(path) :
        print(i)

def change_theme(theme) :
    config["theme"] = theme
    path = os.path.join(themes_dir, theme)
    if not os.path.exists(path):
        print('Theme does not exist')
    save_config()
            
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
            print("Theme does not exist do you want to create one (y/N): ", end='')
            a=input()
            if 'y' in a.lower():
                os.mkdir(path)
            else:
                exit(1)
        path = os.path.join(path, name if name else basename)
    else :
        path = os.path.join(themes_dir, config["theme"], name if name else basename)
    img_resized.save(path)

def state_toggle(state) :
    config['enabled'] = state
    save_config()

def print_image() :
    theme = config["theme"]
    path = os.path.join(themes_dir, theme)
    random_img = random.choice(os.listdir(path))
    display_image = os.path.join(path, random_img)
    subprocess.run(["/usr/bin/kitty", "icat", "--align", "left", display_image])

def main() -> None :
    load_config()
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
        '-ri',
        '--remove-img',
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
        '-e',
        '--enable',
        action='store_true',
        help = 'help'
    )
    parser.add_argument(
        '-d',
        '--disable',
        action='store_true',
        help = 'help'
    )
    
    args = parser.parse_args()

    if args.list_theme :
        print_list()
    elif args.list_img :
        print_img(args.theme)
    elif args.get_theme:
        print(config["theme"])
    elif args.set_theme :
        change_theme(args.set_theme)
    elif args.add_img :
        add_image(args.add_img, args.name, args.theme)
    elif args.remove_img :
        path = os.path.join(themes_dir, args.theme if args.theme else config["theme"], os.path.basename(args.remove_img))
        os.remove(path)
    elif args.mk_theme :
        path = os.path.join(themes_dir, args.mk_theme)
        os.mkdir(path)
    elif args.enable or args.disable :
        state_toggle(True if args.enable else False)
    elif not config['enabled'] :
        exit(1) 
    else :
        print_image()
                
    if not config['enabled'] :
        exit(1)
        
if __name__ == "__main__":
    main()
