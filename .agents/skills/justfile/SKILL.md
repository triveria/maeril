---
name: justfile
description: "Create or update a justfile, add or rename a recipe, or review task-runner conventions. Use when a project needs a `just` task runner, when a new build/test/lint step must be wired into one, or when deciding how recipes map onto pre-commit hooks and CI."
---

# Justfile Conventions

`just` is the task runner for this project. The justfile is the single entry point for every developer-facing command: setup, build, format, lint, test, clean. If a command is worth documenting in a README, it belongs in a recipe instead.

## When to use this skill

- Adding a new recipe, or renaming/removing an existing one.
- Wiring a new tool (formatter, linter, test runner, bundler) into the project.
- Reviewing whether a justfile matches the project's commit and push gates.
- Bootstrapping a justfile for a new project.

Start from [template.just](./template.just) and delete what does not apply. Do not invent recipes for tools the project does not use.

## Rules

1. **Every recipe has a one-line comment directly above it.** `just --list` prints that comment as the recipe's description. A recipe without a comment is invisible in the default listing.
2. **The default recipe is private and lists recipes.** Use `[private]` plus `@just --list` so a bare `just` is a discovery command, not a build.
3. **Comments describe intent, not the command.** Write "Run the fast unit suite", not "cargo test". The command is already visible in the recipe body.
4. **Prefix with `@` when the command line itself is noise.** Use `@` for discovery and status output; leave it off for commands whose echoed invocation is useful in logs.
5. **One recipe per verb.** `fmt` formats, `lint` checks formatting and lints, `test-*` runs one test layer each. Do not fold unrelated steps into one recipe.
6. **Aggregate gates are recipes, not documentation.** `check` runs everything that must pass before a commit; `all` runs `check` plus the slower suite that gates a push. These names are stable — hooks and CI call them.
7. **`check` mirrors the pre-commit hooks.** If `.pre-commit-config.yaml` gains a hook, `check` gains the matching recipe call in the same change. A gate that exists in only one of the two places will drift.
8. **Recipes are non-interactive.** No prompts, no pagers, no editors. Agents and CI run these.
9. **Dependencies express ordering, not duplication.** Use `recipe: dep` when one recipe must run another first (for example `open: build`). Do not copy a recipe body into another.
10. **Keep paths relative to the repository root.** `just` runs recipes from the justfile's directory, so `./scripts/foo.sh` and `pnpm --dir web/editor ...` are correct; `cd` is not needed.

## Naming

| Pattern    | Meaning                                                |
| ---------- | ------------------------------------------------------ |
| `default`  | Private; lists recipes.                                |
| `setup`    | One-time dependency installation.                      |
| `build`    | Produce the shippable artifact.                        |
| `fmt`      | Rewrite sources in place.                              |
| `lint`     | Check-only; fails on violations, changes nothing.      |
| `test-<x>` | One test layer (`test-core`, `test-wasm`, `test-e2e`). |
| `check`    | Commit gate: `lint` plus the fast test layers.         |
| `all`      | Push gate: `check` plus the slow suite.                |
| `clean`    | Remove generated outputs.                              |
| `open`     | Developer convenience; may depend on `build`.          |

## Checklist before finishing

- [ ] Every recipe has a comment above it.
- [ ] `just --list` shows every recipe with a readable description.
- [ ] `just check` passes.
- [ ] New recipes are reflected in `.pre-commit-config.yaml` or CI if they are gates.
- [ ] No recipe requires interactive input.
