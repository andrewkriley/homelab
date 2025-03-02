#GIT Branch to Terminal
function parse_git_branch() {
    git branch 2> /dev/null | sed -n -e 's/^\* \(.*\)/[\1]/p'
}

COLOR_DEF=$'%f'
COLOR_USR=$'%F{243}'
COLOR_DIR=$'%F{197}'
COLOR_GIT=$'%F{39}'
setopt PROMPT_SUBST
export PROMPT='${COLOR_USR}%n ${COLOR_DIR}%~ ${COLOR_GIT}$(parse_git_branch)${COLOR_DEF} $ '


# Set branch name, dirty state, and color
#export PS1="\[\033[36m\]\u\[\033[32m\]\w\[\033[33m\]\$(git_branch)\$(parse_git_dirty)\[\033[00m\]$"#
#
## Find dirty state
#function parse_git_dirty {
#  [[ -n "$(git status -s2> /dev/null)" ]] && echo "*"
#}

# Get branch name
#git_branch() {
#  git branch 2> /dev/null | sed -e '/^[^*]/d' -d 's/* \(.*\)/ (\1)/'
#}

. "$HOME/.local/bin/env"
