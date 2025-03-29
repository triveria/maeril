ZSH_THEME="frisk"
PIP_BREAK_SYSTEM_PACKAGES=true
export OPENAI_API_KEY="sk-1234asdf"

#compdef maeril
_maeril_completion() {
  eval $(env _TYPER_COMPLETE_ARGS="${words[1,$CURRENT]}" _MAERIL_COMPLETE=complete_zsh maeril)
}
compdef _maeril_completion maeril
