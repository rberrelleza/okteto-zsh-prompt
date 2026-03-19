# okteto-prompt

A lightweight zsh prompt plugin that shows the current [Okteto](https://okteto.com) context and namespace in your shell prompt.

```
⎈ okteto.example.com (my-namespace)
~/my/project %
```

## Requirements

- zsh
- python3
- [Okteto CLI](https://www.okteto.com/docs/getting-started/install/)

## Installation

### 1. Clone the repo

```zsh
git clone https://github.com/rberrelleza/okteto-zsh-prompt ~/.config/okteto
```

### 2. Add to ~/.zshrc

Add this single line at the end of your `~/.zshrc`:

```zsh
source ~/.config/okteto/prompt.zsh
```

### 3. Reload your shell

```zsh
source ~/.zshrc
```

## Usage

The prompt updates automatically as you switch contexts:

```zsh
okteto context use https://my-cluster.okteto.com
```

To debug or check the current context manually:

```zsh
# Test the prompt function
_okteto_context

# Run the script directly for plain output
python3 ~/.config/okteto/context.py

# Force a cache refresh
unset _OKTETO_MTIME _OKTETO_PROMPT_CACHE && _okteto_context
```

## How it works

- On each prompt, the zsh function checks the **modification time** of `~/.okteto/context/config.json`
- If the file hasn't changed since last prompt, it returns a **cached result** (effectively zero cost)
- If the file has changed (e.g. after `okteto context use`), it calls the Python script to re-parse the JSON
- The Python script does an exact match on `current-context`, with a partial match fallback

## File structure

```
~/.config/okteto/
├── context.py   # Reads and parses the Okteto config
└── prompt.zsh   # zsh function and PROMPT definition

~/.zshrc         # Sources prompt.zsh
```
