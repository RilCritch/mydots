#!/usr/bin/bash
### EXPORT ###
export EDITOR='nvim'
export VISUAL='nvim'
export HISTCONTROL=ignoreboth:erasedups
export PAGER='most' # default arcolinux option
# export PAGER='less'
# export PAGER='batman'

# export PAGER=nvimpager

#Ibus settings if you need them
#type ibus-setup in terminal to change settings and start the daemon
#delete the hashtags of the next lines and restart
#export GTK_IM_MODULE=ibus
#export XMODIFIERS=@im=dbus
#export QT_IM_MODULE=ibus

PS1='[\u@\h \W]\$ '

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

if [ -d "$HOME/.bin" ]; then
	PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ]; then
	PATH="$HOME/.local/bin:$PATH"
fi

if [ -d "$HOME/scripts" ]; then
	PATH="$HOME/scripts:$PATH"
fi

#ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

### TEMP STUFF TO ADD TO MY BASH CONFIG FILES ###
export FZF_DEFAULT_COMMAND="fd"
export RANGER_LOAD_DEFAULT_RC=FALSE

### My Config temp ###
# Blur {{{
if [[ $(ps --no-header -p $PPID -o comm) =~ yakuake|kitty ]]; then
	for wid in $(xdotool search --pid $PPID); do
		xprop -f _KDE_NET_WM_BLUR_BEHIND_REGION 32c -set _KDE_NET_WM_BLUR_BEHIND_REGION 0 -id $wid
	done
fi
# }}}

#starship
eval "$(starship init bash)"

# show the list of packages that need this package - depends mpv as example
function_depends() {
	search=$(echo "$1")
	sudo pacman -Sii $search | grep "Required" | sed -e "s/Required By     : //g" | sed -e "s/  /\n/g"
}

alias depends='function_depends'

#shopt
shopt -s autocd  # change to named directory
shopt -s cdspell # autocorrects cd misspellings
shopt -s cmdhist # save multi-line commands in history as single line
shopt -s dotglob
shopt -s histappend     # do not overwrite history
shopt -s expand_aliases # expand aliases

# navigation
up () {
  local d=""
  local limit="$1"

  # Default to limit of 1
  if [ -z "$limit" ] || [ "$limit" -le 0 ]; then
    limit=1
  fi

  for ((i=1;i<=limit;i++)); do
    d="../$d"
  done

  # perform cd. Show error if cd fails
  if ! cd "$d"; then
    echo "Couldn't go up $limit dirs.";
  fi
}

# # ex = EXtractor for all kinds of archives
# # usage: ex <file>
ex() {
	if [ -f $1 ]; then
		case $1 in
      *.tar.bz2) tar xf $1 ;;
      *.tar.gz) tar xzf $1 ;;
      *.bz2) bunzip2 $1 ;;
      *.rar) unrar x $1 ;;
      *.gz) gunzip $1 ;;
      *.tar) tar xf $1 ;;
      *.tbz2) tar xf $1 ;;
		*.tgz) tar xzf $1 ;;
		*.zip) unzip $1 ;;
		*.Z) uncompress $1 ;;
		*.7z) 7z x $1 ;;
		*.deb) ar x $1 ;;
		*.tar.xz) tar xf $1 ;;
		*.tar.zst) tar xf $1 ;;
		*) echo "'$1' cannot be extracted via ex()" ;;
		esac
	else
		echo "'$1' is not a valid file"
	fi
}

[[ -f $HOME/mydots/bashconf/aliases ]] && . $HOME/mydots/bashconf/aliases
[[ -f $HOME/mydots/bashconf/envvars ]] && . $HOME/mydots/bashconf/envvars

#Generic color list
{
	c1='[31m'
	c2='[32m'
	c3='[33m'
	c4='[34m'
	c5='[35m'
	c6='[36m'
	c7='[37m'
	c8='[38m'
	cR='[m'
}
