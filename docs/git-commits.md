# Git Commits

This is the commit convention for everyone working in this repository, human or agent. The format is enforced by a `commit-msg` hook (`scripts/commit-msg`), so a non-conforming subject is rejected before the commit exists.

## Subject format

```text
<gitmoji> <type>(<scope>): Capitalized imperative subject
```

- The **gitmoji** comes first and must be the exact emoji assigned to the type below.
- The **type** is one of the eleven listed types. The list is closed.
- The **scope** names the area touched, e.g. `core`, `app`, `canvas`, `chrome`, `io`, `build`, `e2e`, `web`, `docs`, `gitignore`. It must match `[a-z0-9-]+` and is open — pick the path or module the change lives in.
- The **subject** starts with a capital letter, is written in the imperative mood ("Add", not "Added" or "Adds"), and does not end with a period.

Example: `✨ feat(core): Add rectangle insertion transaction`

## Types and gitmoji

The emoji are [gitmoji](https://gitmoji.dev) and are compared byte for byte, so the same glyph always renders in `git log`. Keep the codepoints intact when copying; `U+FE0F` is the emoji presentation selector and must be present where listed.

| Type       | Emoji | Codepoints       | Meaning                                    |
| ---------- | ----- | ---------------- | ------------------------------------------ |
| `feat`     | ✨    | `U+2728`         | Introduce a new feature                    |
| `fix`      | 🐛    | `U+1F41B`        | Fix a bug                                  |
| `refactor` | ♻️    | `U+267B U+FE0F`  | Restructure code without changing behavior |
| `test`     | ✅    | `U+2705`         | Add, update, or fix tests                  |
| `docs`     | 📝    | `U+1F4DD`        | Add or update documentation                |
| `build`    | 📦️    | `U+1F4E6 U+FE0F` | Build output, packaging, dependencies      |
| `ci`       | 👷    | `U+1F477`        | CI and automation configuration            |
| `chore`    | 🔧    | `U+1F527`        | Configuration, tooling, and misc changes   |
| `perf`     | ⚡️    | `U+26A1 U+FE0F`  | Improve performance                        |
| `merge`    | 🔀    | `U+1F500`        | Merge branches                             |
| `revert`   | ⏪️    | `U+23EA U+FE0F`  | Revert a previous change                   |

## Body

A body is optional. Add one only when the _why_ is not obvious from the subject and the diff; do not narrate _how_ the change was made, the diff already shows that. Skip generic filler such as "updated files".

## Merges and reverts

`git merge` and `git revert` write their own subjects, which do not conform to the format and are therefore rejected. Run them with `--no-commit`, then commit explicitly so the message conforms and the full commit gates run:

```console
git merge --no-commit feature-x
git commit -m "🔀 merge(core): Merge feature-x"

git revert --no-commit 1a2b3c4
git commit -m "⏪️ revert(core): Revert rectangle insertion"
```

The extra step is intentional: a merge created with a generated message would skip the pre-commit gates and could land code that never passed them.

## Prohibited commits

- `wip`, `fixup!`, `squash!`, and "checkpoint" commits. Every commit must be able to stand alone.
- Commits with disabled, skipped, or commented-out tests.
- History rewrites: rebasing and squashing are prohibited, and a commit that has already been pushed must not be amended.

## Pushing

Push only when explicitly asked to. Committing is local; publishing is a separate decision.

## Bypassing hooks

Never commit with `--no-verify`. If a hook fails, fix the cause and commit again instead of adding a follow-up "fix lint" commit.
