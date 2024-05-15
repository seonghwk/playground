# playground

https://inpa.tistory.com/entry/LINUX-📚-모던-리눅스-터미널을-화려하게-🐧-최신식-CLI-모음

ls              -> exa, lsd
cat             -> bat
find            -> fd
grep            -> ripgrep
more/less/diff  -> delta
man             -> tldr
cd              -> zoxide
tree            -> broot
du              -> dust
ps              -> procs
ping            -> gping
history         -> mcfly
od              -> hexyl
sed             -> jq, fx
curl            -> httpie, xh
dig             -> dog
mv/cp/mkdir     -> nnn

fzf
gtop, bottom

Crtl + X , Ctrl + E -> Edit command line in Editor

## lsd

https://gracefullight.dev/en/2019/05/27/install-lsd-on-mac/

```bash
brew install lsd

alias ls='lsd'
alias ll='ls -alhF'
```

## bat

```bash
sudo apt install bat
ln -s /usr/bin/batcat ~/.local/bin/bat
```

## fd
```bash
sudo install fd-find
ln -s $(which fdfind) ~/.local/bin/fd


fd  # same as ls

fd <Filename>       # search from current directory
fd <Filename> <path>

fd -e png   # filter by extension

fd -E <directory>   # Exclude chosen directory from search

fd -g '*.png'       # glob pattern enable
```

## ripgrep
```bash
sudo apt install ripgrep


rg <Pattern> <path or file>

rg -i <Pattern>     # ignore case
```

## zoxide

```bash

z foo bar   # cd into highest ranked directory matching foo and bar
z foo /     # cd into a subdirectory starting with foo

zi foo      # cd with interactive selection (using fzf)

z foo<SPACE><TAB>   # show interactive completion

```
