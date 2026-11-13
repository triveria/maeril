---
applyTo: "**/*.md"
---

# Markdown conventions

## Line breaks

- Put every sentence on its own line.
- Never wrap lines at a fixed width (such as 80 characters). Long lines are fine.
- Never break a sentence across several lines.
- Separate paragraphs with a blank line, as usual.
- Applies to prose only. Code blocks, tables and list items keep their natural structure.

## Timeless content

Write documentation as a reference that is equally true whenever it is read.
A reader next week knows nothing about the change that produced the text and does not care about it.

- Describe how things are, not what you just did.
- Do not narrate the task, session or history of the text ("added", "now supports", "newly", "updated to").
- Do not report the status of your own work, such as tests run or not run, what was verified, or what you could not check. That belongs in your reply to the user or in the PR description.
- Avoid time-relative words like "recently", "now", "currently", "new", "previously" and "as of today".
- Before keeping a sentence, ask: would it still be useful to someone reading it a week from now, without any knowledge of this change? If not, leave it out.

Bad: "Added `run-smoke.sh`. No tests were run for it yet."
Good: "`run-smoke.sh` runs the smoke tests against the local stack."
