#!/bin/sh
echo "Installing termanime..."
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

# Check if config directory exists, create if not
if [ ! -d "$CONFIG_DIR" ]; then
  echo "Creating config directory: $CONFIG_DIR"
  mkdir -p "$CONFIG_DIR" || { echo "Error creating config directory"; exit 1; }
fi

# Copy default config if no config exists
if [ ! -e "$CONFIG_DIR/config_file" ]; then
  echo "Copying default config files to: $CONFIG_DIR"
  cp -r config/* "$CONFIG_DIR"/ || { echo "Error copying config files"; exit 1; }
fi

# Check if theme directory exists, create if not
if [ ! -d "$THEME_DIR" ]; then
  echo "Creating theme directory: $THEME_DIR"
  mkdir -p "$THEME_DIR" || { echo "Error creating theme directory"; exit 1; }
fi

# Copy default theme if no theme exists
if [ ! -e "$THEME_DIR/theme_file" ]; then
  echo "Copying default theme files to: $THEME_DIR"
  cp -r ./config/themes/* "$THEME_DIR"/ || { echo "Error copying theme files"; exit 1; }
fi

# Move new binary to bin directory
echo "Installing binary to: $BIN_DIR"
sudo cp ./termanime.py "$BIN_DIR/termanime" || { echo "Error installing binary"; exit 1; }
sudo chmod +x "$BIN_DIR/termanime" || { echo "Error setting permissions for binary"; exit 1; }

echo "Installation complete!"
