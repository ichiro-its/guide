# Setup Zsh

- Install **Zsh** using `apt` command.
  ``` sh
  ~$ sudo apt install zsh
  ```
- Replace default bash with **Zsh**.
  ``` sh
  ~$ chsh -s /usr/bin/zsh
  ```
- Open a new terminal, you will be prompted to configure **Zsh**.
  type `2` to choose recommended option, else you will need to configure **Zsh** by yourself.

# Setup Oh My Zsh

## Installation

- Run **Oh My Zsh** installer script with the following command
  ``` sh
  ~$ sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
  ```
- When asked to change default shell to zsh, choose `Y`.

## Change Theme _(Optional)_

- In `~/.zshrc`, modify the `ZSH_THEME` parameter with the desired theme _(it is recommended to use **agnoster** theme)_.
  For full list of **Zsh** theme, check [here](https://github.com/robbyrussell/oh-my-zsh/wiki/Themes).

> **Note:** Most **Zsh** theme display uncommon characters.
  It is recommended to use a font that support those characters in the terminal _(ex: [hermit font](https://pcaro.es/p/hermit/))_.

# Add Extra Plugins _(Optional)_

## Extract Plugin

- In `~/.zshrc`, add `extract` to `plugins` parameter _(separate each plugin with space)_.

## Syntax Highlighting Plugin

- Clone the **Zsh Syntax Highlighting** plugin to the **Zsh** plugin directory.
  ``` sh
  ~$ git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
  ```
- In `~/.zshr`, add `zsh-syntax-highlighting` to `plugins` parameter _(separate each plugin with space)_.

## Auto Suggestions Plugin

- Clone the **Zsh Auto Suggestions** plugin to the **Zsh** plugin directory.
  ``` sh
  ~$ git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
  ```
- In `~/.zshrc`, add `zsh-autosuggestions` to `plugins` parameter _(separate each plugins with space)_.