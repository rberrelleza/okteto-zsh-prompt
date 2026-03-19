# ~/.config/okteto/prompt.zsh

_okteto_context() {
  local script="$HOME/.config/okteto/context.py"
  local config="$HOME/.okteto/context/config.json"
  [[ ! -f "$script" ]] && return
  [[ ! -f "$config" ]] && return

  local mtime
  mtime=$(stat -f %m "$config" 2>/dev/null) || mtime=$(stat -c %Y "$config" 2>/dev/null)

  if [[ "$mtime" == "$_OKTETO_MTIME" && -n "$_OKTETO_PROMPT_CACHE" ]]; then
    echo "$_OKTETO_PROMPT_CACHE"
    return
  fi

  local result
  result=$(python3 "$script" --prompt 2>/dev/null)
  [[ -z "$result" ]] && return

  _OKTETO_MTIME="$mtime"
  _OKTETO_PROMPT_CACHE="$result"
  echo "$result"
}

setopt PROMPT_SUBST
PROMPT='$(_okteto_context)'$'\n''%F{green}%~%f %# '
