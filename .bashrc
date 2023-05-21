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

#common dirs
# alias trash='cd $HOME/.local/share/Trash/files/ && clear && lsa'
alias trash='ranger $HOME/.local/share/Trash/files/'

#utility
alias scr='xdpyinfo | grep dimensions'

# show the list of packages that need this package - depends mpv as example
function_depends() {
	search=$(echo "$1")
	sudo pacman -Sii $search | grep "Required" | sed -e "s/Required By     : //g" | sed -e "s/  /\n/g"
}

alias depends='function_depends'

#pacman unlock
alias unlock="sudo rm /var/lib/pacman/db.lck"
alias rmpacmanlock="sudo rm /var/lib/pacman/db.lck"

#arcolinux logout unlock
alias rmlogoutlock="sudo rm /tmp/arcologout.lock"

# paru as aur helper - updates everything
alias pksyua="paru -Syu --noconfirm"
alias upall="paru -Syu --noconfirm"
alias upa="paru -Syu --noconfirm"

#backup contents of /etc/skel to hidden backup folder in home/user
alias bupskel='cp -Rf /etc/skel ~/.skel-backup-$(date +%Y.%m.%d-%H.%M.%S)'

#get fastest mirrors in your neighborhood
alias mirror="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
alias mirrord="sudo reflector --latest 30 --number 10 --sort delay --save /etc/pacman.d/mirrorlist"
alias mirrors="sudo reflector --latest 30 --number 10 --sort score --save /etc/pacman.d/mirrorlist"
alias mirrora="sudo reflector --latest 30 --number 10 --sort age --save /etc/pacman.d/mirrorlist"
#our experimental - best option for the moment
alias mirrorx="sudo reflector --age 6 --latest 20  --fastest 20 --threads 5 --sort rate --protocol https --save /etc/pacman.d/mirrorlist"
alias mirrorxx="sudo reflector --age 6 --latest 20  --fastest 20 --threads 20 --sort rate --protocol https --save /etc/pacman.d/mirrorlist"
alias ram='rate-mirrors --allow-root --disable-comments arch | sudo tee /etc/pacman.d/mirrorlist'
alias rams='rate-mirrors --allow-root --disable-comments --protocol https arch  | sudo tee /etc/pacman.d/mirrorlist'

#shopt
shopt -s autocd  # change to named directory
shopt -s cdspell # autocorrects cd misspellings
shopt -s cmdhist # save multi-line commands in history as single line
shopt -s dotglob
shopt -s histappend     # do not overwrite history
shopt -s expand_aliases # expand aliases

#youtube download
alias yta-aac="yt-dlp --extract-audio --audio-format aac "
alias yta-best="yt-dlp --extract-audio --audio-format best "
alias yta-flac="yt-dlp --extract-audio --audio-format flac "
alias yta-mp3="yt-dlp --extract-audio --audio-format mp3 "
alias ytv-best="yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 "

#Recent Installed Packages
alias rip="expac --timefmt='%Y-%m-%d %T' '%l\t%n %v' | sort | tail -200 | nl"
alias riplong="expac --timefmt='%Y-%m-%d %T' '%l\t%n %v' | sort | tail -3000 | nl"

#iso and version used to install ArcoLinux
alias iso="cat /etc/dev-rel | awk -F '=' '/ISO/ {print $2}'"
alias isoo="cat /etc/dev-rel"

#search content with ripgrep
alias rg="rg --sort path"

#nvim for important configuration files
#know what you do in these files 
### CHANGE FOR STUFF I WANT TO EDIT OFTEN
alias nvlxdm="sudo $EDITOR /etc/lxdm/lxdm.conf"
alias nvlightdm="sudo $EDITOR /etc/lightdm/lightdm.conf"
alias nvpacman="sudo $EDITOR /etc/pacman.conf"
alias nvgrub="sudo $EDITOR /etc/default/grub"
alias nvconfgrub="sudo $EDITOR /boot/grub/grub.cfg"
alias nvmkinitcpio="sudo $EDITOR /etc/mkinitcpio.conf"
alias nvmirrorlist="sudo $EDITOR /etc/pacman.d/mirrorlist"
alias nvarcomirrorlist="sudo $EDITOR /etc/pacman.d/arcolinux-mirrorlist"
alias nvsddm="sudo $EDITOR /etc/sddm.conf"
alias nvsddmk="sudo $EDITOR /etc/sddm.conf.d/kde_settings.conf"
alias nvfstab="sudo $EDITOR /etc/fstab"
alias nvnsswitch="sudo $EDITOR /etc/nsswitch.conf"
alias nvsamba="sudo $EDITOR /etc/samba/smb.conf"
alias nvgnupgconf="sudo $EDITOR /etc/pacman.d/gnupg/gpg.conf"
alias nvhosts="sudo $EDITOR /etc/hosts"
alias nvhostname="sudo $EDITOR /etc/hostname"
alias nvresolv="sudo $EDITOR /etc/resolv.conf"
alias nvz="$EDITOR ~/.zshrc"
alias nvf="$EDITOR ~/.config/fish/config.fish"
alias nvneofetch="$EDITOR ~/.config/neofetch/config.conf"

#gpg
#verify signature for isos
alias gpg-check="gpg2 --keyserver-options auto-key-retrieve --verify"
alias fix-gpg-check="gpg2 --keyserver-options auto-key-retrieve --verify"
#receive the key of a developer
alias gpg-retrieve="gpg2 --keyserver-options auto-key-retrieve --receive-keys"
alias fix-gpg-retrieve="gpg2 --keyserver-options auto-key-retrieve --receive-keys"
alias fix-keyserver="[ -d ~/.gnupg ] || mkdir ~/.gnupg ; cp /etc/pacman.d/gnupg/gpg.conf ~/.gnupg/ ; echo 'done'"

#hblock (stop tracking with hblock)
#use unhblock to stop using hblock
alias unhblock="hblock -S none -D none"

#shutdown or reboot
alias ssn="sudo shutdown now" # system util
alias sr="reboot" # system util

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
		*.tar.bz2) tar xjf $1 ;;
		*.tar.gz) tar xzf $1 ;;
		*.bz2) bunzip2 $1 ;;
		*.rar) unrar x $1 ;;
		*.gz) gunzip $1 ;;
		*.tar) tar xf $1 ;;
		*.tbz2) tar xjf $1 ;;
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

#git
alias rmgitcache="rm -r ~/.cache/git"
alias grh="git reset --hard"

#pamac
alias pamac-unlock="sudo rm /var/tmp/pamac/dbs/db.lock"

#moving your personal files and folders from /personal to ~
alias personal='cp -Rf /personal/* ~'

[[ -f $HOME/mydots/bashconf/bashaliases ]] && . $HOME/mydots/bashconf/bashaliases

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
