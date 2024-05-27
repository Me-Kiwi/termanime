#!/bin/sh
echo "Uninstalling termanime..."
echo """                                    
████████╗███████╗██████╗ ███╗   ███╗ █████╗ ███╗   ██╗██╗███╗   ███╗███████╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██╔══██╗████╗  ██║██║████╗ ████║██╔════╝
   ██║   █████╗  ██████╔╝██╔████╔██║███████║██╔██╗ ██║██║██╔████╔██║█████╗  
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║╚██╔╝██║██╔══╝  
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║██║██║ ╚═╝ ██║███████╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚══════╝
"""

APP_NAME="termanime"
THEME_DIR="$HOME/.themes/$APP_NAME"
BIN_DIR="/usr/local/bin"
CONFIG_DIR="$HOME/.config/$APP_NAME"

echo "Looking for executable python file"
if [ -d "$BIN_DIR" ]; then
   echo "Executable python file found :"
   read -p "Remove python file (y/N): " exeopt
   if [ "$exeopt" = "y" ] || [ "$exeopt" = "Y" ]; then
      echo "Removing python executable...."
      sudo rm -rf "$BIN_DIR/$APP_NAME" || { echo "Error removing python executable at $BIN_DIR"; exit 1; }
   fi
else 
   echo "$BIN_DIR does not exist"
fi

echo "Looking for config directory"
if [ -d "$CONFIG_DIR" ]; then
   echo "Config directory found :"
   read -p "Remove config directory (y/N): " conopt 
   if [ "$conopt" = "y" ] || [ "$conopt" = "Y" ]; then
      echo "Removing config directory...."
      rm -rf "$CONFIG_DIR" || { echo "Error removing config directory ($CONFIG_DIR)"; exit 1; }
   fi
else 
   echo "$CONFIG_DIR does not exist"
fi 

if [ -d "$THEME_DIR" ]; then
   echo "Theme directory found :"
   read -p "Remove theme directory (y/N): " themeopt
   if [ "$themeopt" = "y" ] || [ "$themeopt" = "Y" ]; then
      echo "Removing theme directory...."
      rm -rf "$THEME_DIR" || { echo "Error removing theme directory($THEME_DIR)"; exit 1; }
   fi
else
   echo "$THEME_DIR does not exist"
fi 

echo "Uninstallation complete!"
