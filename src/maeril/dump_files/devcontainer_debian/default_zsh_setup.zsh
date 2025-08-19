ZSH_THEME="frisk"
PIP_BREAK_SYSTEM_PACKAGES=true
export OPENAI_API_KEY="sk-1234asdf"

#compdef maeril
_maeril_completion() {
  eval $(env _TYPER_COMPLETE_ARGS="${words[1,$CURRENT]}" _MAERIL_COMPLETE=complete_zsh maeril)
}
compdef _maeril_completion maeril

# ------------------------------------------------------------------------------
# Custom Keybinding: Rebind Ctrl+L to run `clear`
#
# This creates a ZLE widget to clear the screen using the external `clear`
# command, which also clears scrollback, and then redraws the prompt.
# It is recommended to place this at the end of the .zshrc file.
# ------------------------------------------------------------------------------
function custom_clear_screen_widget() {
    # Execute the external `clear` program
    command clear
    # Redraw the prompt and any text that was on the command line
    zle redisplay
}

# Register the function as a new ZLE widget
zle -N custom_clear_screen_widget

# Bind the Ctrl+L key sequence to the new custom widget
bindkey '^L' custom_clear_screen_widget
